# -*- coding: utf-8 -*-
"""知识库版本：快照 / 回滚 / 列表 / 对比。
用法：
    python _kb/automation/version.py snapshot --tag before-change
    python _kb/automation/version.py list
    python _kb/automation/version.py restore --to 20261126-100500
    python _kb/automation/version.py diff --from <ts> --to <ts>
"""
import os, sys, json, shutil, hashlib, datetime, argparse, csv

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HIST = os.path.join(BASE, "history")
CHANGELOG = os.path.join(BASE, "CHANGELOG.md")

FILES = [
    "01-products.csv", "02-atoms.csv", "03-workflows.csv", "04-channels.csv",
    "05-resources.csv", "06-problem-to-component.md", "07-patterns.md",
    "08-template-modules.csv", "09-template-anatomy.md", "10-template-picker.md",
    "11-template-fit.csv", "12-template-fit.md",
    "13-template-catalog.csv", "14-template-catalog.md",
    "15-template-taxonomy.csv", "16-template-taxonomy.md",
    "17-resource-audit.csv", "17-resource-audit.md",
    "index.json", "SKILL.md", "llms.txt", "README.md",
    "db/kb.sqlite",
]
DIRS = ["by-product", "raw", "data"]

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(65536), b""):
            h.update(b)
    return h.hexdigest()

def counts():
    out = {}
    for f, key in [("01-products.csv", "products"), ("02-atoms.csv", "atoms"),
                   ("03-workflows.csv", "workflows"), ("04-channels.csv", "channels"),
                   ("05-resources.csv", "resources"), ("08-template-modules.csv", "template_modules"),
                   ("11-template-fit.csv", "template_fit"), ("13-template-catalog.csv", "template_catalog"),
                   ("15-template-taxonomy.csv", "template_taxonomy")]:
        p = os.path.join(BASE, f)
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8-sig", newline="") as fh:
                out[key] = max(0, len(list(csv.reader(fh))) - 1)
    return out

def snapshot(tag=""):
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")[:19]
    dest = os.path.join(HIST, ts)
    os.makedirs(dest, exist_ok=True)
    manifest = {"ts": ts, "tag": tag, "created_at": datetime.datetime.now().isoformat(timespec="seconds"),
                "files": {}, "counts": counts()}
    for rel in FILES:
        src = os.path.join(BASE, rel)
        if not os.path.exists(src):
            continue
        dst = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        manifest["files"][rel] = {"sha256": sha(src), "size": os.path.getsize(src)}
    for d in DIRS:
        s = os.path.join(BASE, d)
        if not os.path.isdir(s):
            continue
        for root, _, fs in os.walk(s):
            for f in fs:
                src = os.path.join(root, f)
                rel = os.path.relpath(src, BASE)
                dst = os.path.join(dest, rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
                manifest["files"][rel] = {"sha256": sha(src), "size": os.path.getsize(src)}
    with open(os.path.join(dest, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    line = f"- {manifest['created_at']} `{ts}` {tag} | " + ", ".join(f"{k}={v}" for k, v in manifest["counts"].items()) + "\n"
    header = "# 知识库变更记录\n\n> 每次快照一行；回滚用 `python _kb/automation/version.py restore --to <ts>`。\n\n"
    if not os.path.exists(CHANGELOG):
        with open(CHANGELOG, "w", encoding="utf-8") as f:
            f.write(header)
    with open(CHANGELOG, "a", encoding="utf-8") as f:
        f.write(line)
    prune(keep=30)
    print("snapshot:", ts, "files:", len(manifest["files"]), "tag:", tag)
    return ts

def prune(keep=30):
    if not os.path.isdir(HIST):
        return
    snaps = sorted([d for d in os.listdir(HIST) if os.path.isdir(os.path.join(HIST, d))])
    for old in snaps[:-keep]:
        shutil.rmtree(os.path.join(HIST, old), ignore_errors=True)
        print("pruned:", old)

def latest():
    if not os.path.isdir(HIST):
        return None
    snaps = sorted([d for d in os.listdir(HIST) if os.path.isdir(os.path.join(HIST, d))])
    return snaps[-1] if snaps else None

def restore(ts):
    src = os.path.join(HIST, ts)
    man = os.path.join(src, "manifest.json")
    if not os.path.exists(man):
        print("找不到快照:", ts); return 1
    with open(man, "r", encoding="utf-8") as f:
        m = json.load(f)
    # 先给当前状态留一份，避免回滚本身不可逆
    snapshot(tag="auto-before-restore-" + ts)
    for rel in m["files"]:
        s = os.path.join(src, rel)
        d = os.path.join(BASE, rel)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copy2(s, d)
    print("restored:", ts, "files:", len(m["files"]))
    return 0

def list_snaps():
    if not os.path.isdir(HIST):
        print("（无快照）"); return
    for d in sorted(os.listdir(HIST)):
        p = os.path.join(HIST, d, "manifest.json")
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                m = json.load(f)
            print(d, "|", m.get("tag", ""), "|", ", ".join(f"{k}={v}" for k, v in m.get("counts", {}).items()))

def diff(a, b):
    ma = json.load(open(os.path.join(HIST, a, "manifest.json"), encoding="utf-8"))
    mb = json.load(open(os.path.join(HIST, b, "manifest.json"), encoding="utf-8"))
    print("counts:", a, ma.get("counts"), "->", b, mb.get("counts"))
    fa, fb = ma["files"], mb["files"]
    for k in sorted(set(fa) | set(fb)):
        if k not in fa:
            print("  + ", k)
        elif k not in fb:
            print("  - ", k)
        elif fa[k]["sha256"] != fb[k]["sha256"]:
            print("  ~ ", k)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("snapshot"); s.add_argument("--tag", default="")
    sub.add_parser("list")
    r = sub.add_parser("restore"); r.add_argument("--to", required=True)
    d = sub.add_parser("diff"); d.add_argument("--from", dest="a", required=True); d.add_argument("--to", dest="b", required=True)
    args = ap.parse_args()
    if args.cmd == "snapshot":
        snapshot(args.tag)
    elif args.cmd == "list":
        list_snaps()
    elif args.cmd == "restore":
        sys.exit(restore(args.to))
    elif args.cmd == "diff":
        diff(args.a, args.b)
