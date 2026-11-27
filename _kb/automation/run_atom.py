# -*- coding: utf-8 -*-
"""原子执行器：按 atoms.json 跑单个/一组/全部步骤，带自动快照、失败回滚、日志。
用法：
    python _kb/automation/run_atom.py --list
    python _kb/automation/run_atom.py --atom kb.db
    python _kb/automation/run_atom.py --group kb
    python _kb/automation/run_atom.py --all
    python _kb/automation/run_atom.py --episode 014-taskade --render
"""
import json, os, sys, subprocess, datetime, argparse, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
KB = os.path.dirname(HERE)
ROOT = os.path.dirname(KB)
LOGS = os.path.join(KB, "logs")
sys.path.insert(0, HERE)
import version  # noqa

def load():
    with open(os.path.join(HERE, "atoms.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def find(manifest, atom_id):
    for g, items in manifest["groups"].items():
        for a in items:
            if a["id"] == atom_id:
                return a
    return None

def run_one(manifest, atom, variables, no_snapshot=False):
    cmd = [c.format(**variables) for c in atom["cmd"]]
    os.makedirs(LOGS, exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log = os.path.join(LOGS, f"{ts}-{atom['id'].replace('.', '_')}.log")
    print(f"\n>>> {atom['id']} — {atom.get('name','')}")
    print("    cmd:", " ".join(cmd))
    t0 = datetime.datetime.now()
    with open(log, "w", encoding="utf-8") as lf:
        p = subprocess.run(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=atom.get("timeout", 600))
        lf.write(p.stdout or "")
    dt = (datetime.datetime.now() - t0).total_seconds()
    tail = (p.stdout or "").strip().splitlines()[-3:]
    print("    exit:", p.returncode, f"({dt:.1f}s)", "| log:", os.path.relpath(log, ROOT))
    for line in tail:
        print("   ", line)
    if p.returncode != 0:
        return False
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--atom")
    ap.add_argument("--group")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--episode", help="对某一期跑 episode 组（提供 dir 变量）")
    ap.add_argument("--render", action="store_true", help="配合 --episode：只跑渲染+刷墙")
    ap.add_argument("--var", action="append", default=[], help="k=v，可多次")
    ap.add_argument("--no-snapshot", action="store_true")
    args = ap.parse_args()

    manifest = load()
    variables = {"dir": args.episode or ""}
    for kv in args.var:
        if "=" in kv:
            k, v = kv.split("=", 1)
            variables[k] = v

    if args.list:
        for g, items in manifest["groups"].items():
            print(f"\n[{g}]")
            for a in items:
                print(f"  {a['id']:<26} {a.get('name','')}")
        return

    todo = []
    if args.atom:
        a = find(manifest, args.atom)
        if not a:
            print("找不到 atom:", args.atom); sys.exit(2)
        todo = [a]
    elif args.group:
        todo = manifest["groups"].get(args.group, [])
    elif args.episode:
        ids = ["episode.render", "episode.wall"] if args.render else ["episode.collect_pages", "episode.collect_reviews", "episode.render", "episode.wall"]
        todo = [find(manifest, i) for i in ids]
    elif args.all:
        todo = manifest["groups"]["kb"]
    else:
        print("用 --list / --atom / --group / --all / --episode"); return

    ok = True
    base_snapshot = None
    if any(a and a.get("writes") for a in todo) and not args.no_snapshot:
        base_snapshot = version.snapshot(tag="auto-" + (args.atom or args.group or "episode"))
    for a in todo:
        if not a:
            continue
        if not run_one(manifest, a, variables, args.no_snapshot):
            ok = False
            break

    # 跑完 kb 组后自动 QA
    if ok and (args.group == "kb" or args.all):
        print("\n>>> kb.qa（自动质量闸）")
        p = subprocess.run([sys.executable, os.path.join(HERE, "qa_gate.py")], cwd=ROOT)
        if p.returncode != 0:
            ok = False

    if not ok:
        if base_snapshot:
            print("!! 失败，回滚到:", base_snapshot)
            version.restore(base_snapshot)
        else:
            print("!! 失败（未快照，未回滚）")

    print("\nDONE" if ok else "\nFAILED")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
