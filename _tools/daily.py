# -*- coding: utf-8 -*-
"""每日拆解流水线 · Marvis 专用入口

Marvis 不需要理解流程，只需要按顺序跑这四条命令，看输出。

  python _tools/daily.py next                      # 今天该做哪篇（严格顺序锁）
  python _tools/daily.py collect 003 --site https://capacities.io --pricing https://capacities.io/pricing
  python _tools/daily.py build 003                 # 渲染中英报告 + 刷进度墙
  python _tools/daily.py commit 003                # git add/commit/push

每条命令最后一行固定输出 RESULT={...}，Marvis 只需照抄这一行。
任何一步失败，命令会以 exit code 1 结束并打印 ERROR=，Marvis 必须停下，不许继续下一步。
"""
import argparse, json, os, re, subprocess, sys, shutil

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "_tools")
PY = sys.executable


def run(cmd, cwd=None):
    p = subprocess.run(cmd, cwd=cwd or ROOT, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def emit(obj):
    print("RESULT=" + json.dumps(obj, ensure_ascii=False))


def fail(msg):
    print("ERROR=" + msg)
    emit({"ok": False, "error": msg})
    sys.exit(1)


def queue_row(no):
    import csv
    with open(os.path.join(ROOT, "_data", "queue.csv"), encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if str(r.get("no", "")).strip() and int(r["no"]) == int(no):
                return r
    return None


def dir_of(no, slug):
    return os.path.join(ROOT, "%03d-%s" % (int(no), slug))


# ---------- next ----------
def cmd_next(_):
    rc, out = run([PY, os.path.join(TOOLS, "next_task.py"), "--json"])
    if rc != 0:
        fail("选题器跑不通：" + out[-300:])
    try:
        data = json.loads(out.strip().splitlines()[-1])
    except Exception:
        fail("选题器输出不是 JSON：" + out[-300:])
    done = os.path.exists(os.path.join(ROOT, data.get("dir", "_"), "teardown-zh.html")) if data.get("dir") else True
    emit({"ok": True, "step": "next", "state": data.get("state"),
          "no": data.get("no"), "name": data.get("name"), "slug": data.get("slug"),
          "dir": data.get("dir"), "message": data.get("message"),
          "has_report": done})


# ---------- collect ----------
def cmd_collect(args):
    row = queue_row(args.no)
    if not row:
        fail("队列里没有第 %s 号" % args.no)
    d = dir_of(args.no, row["slug"])
    os.makedirs(d, exist_ok=True)
    tmp = os.path.join(ROOT, "_tools", "run", "auto-%s" % row["slug"])
    os.makedirs(tmp, exist_ok=True)

    lib = os.path.join(ROOT, "_tools")
    mapping = {
        "collect-product.mjs": ("/", "product"),
        "collect-ph-reviews.mjs": ("/reviews", "ph"),
        "collect-g2-reviews.mjs": ("/reviews", "g2"),
    }
    urls = ["https://www.producthunt.com/products/" + row["slug"]]
    if args.site:
        urls.append(args.site)
    if args.pricing:
        urls.append(args.pricing)

    for src, (_, tag) in mapping.items():
        p = os.path.join(lib, src)
        if not os.path.exists(p):
            fail("缺采集器 %s，先补" % src)
        s = open(p, encoding="utf-8").read()
        s = re.sub(r'taskSpace\([^)]*\)', 'taskSpace("marvis-daily")', s)
        s = re.sub(r'const SLUG = "[^"]*";', 'const SLUG = "%s";' % row["slug"], s)
        s = re.sub(r'const NAME = "[^"]*";', 'const NAME = "%s";' % row["name"].replace('"', ""), s)
        s = re.sub(r'const OUT = "[^"]*";', 'const OUT = "%s";' % d.replace("\\", "/"), s)
        if tag == "product":
            s = re.sub(r'const URLS = \[[\s\S]*?\];',
                       "const URLS = [\n" + "".join('  "%s",\n' % u for u in urls) + "];", s)
        dst = os.path.join(tmp, src)
        open(dst, "w", encoding="utf-8").write(s)
        uri = "file:///" + dst.replace("\\", "/").replace(" ", "%20")
        rc, out = run(["ego-browser", "nodejs", "-e", 'await import("%s")' % uri])
        if rc != 0 or "WROTE" not in out:
            fail("采集失败（%s）：%s" % (src, (out[:500] + " … " + out[-300:])))

    # 统一命名：<slug>.md 改成 _raw.md，选题器只认 _raw.md
    slug_md = os.path.join(d, row["slug"] + ".md")
    raw_md = os.path.join(d, "_raw.md")
    if os.path.exists(slug_md) and not os.path.exists(raw_md):
        os.replace(slug_md, raw_md)

    got = sorted(os.listdir(d))
    if not any("评论" in x for x in got):
        fail("评论文件没生成，目录里只有：" + ", ".join(got))
    emit({"ok": True, "step": "collect", "dir": os.path.basename(d), "files": got})


# ---------- exp（检查并搬运实测） ----------
VAULT = r"D:\ObsidianVault\03-Resources\product sense\01-拆解"


def find_experience(no, slug, name):
    """在两个位置找实测：_实测表\\<no>-<slug>.md，或 01-拆解 下含产品名的真实体验.md"""
    cands = []
    p1 = os.path.join(VAULT, "_实测表", "%03d-%s.md" % (int(no), slug))
    if os.path.exists(p1):
        cands.append(p1)
    if os.path.isdir(VAULT):
        for f in os.listdir(VAULT):
            if f.endswith(".md") and (name.split()[0].lower() in f.lower()) and ("真实体验" in f or "实测" in f):
                cands.append(os.path.join(VAULT, f))
    best = None
    for p in cands:
        try:
            txt = open(p, encoding="utf-8").read()
        except Exception:
            continue
        filled = txt.count("|  |") < 5 or "我填" in txt
        size = len(txt)
        if size > 2500 and filled:
            if best is None or size > os.path.getsize(best):
                best = p
    return best


def cmd_exp(args):
    row = queue_row(args.no)
    if not row:
        fail("队列里没有第 %s 号" % args.no)
    d = dir_of(args.no, row["slug"])
    os.makedirs(d, exist_ok=True)
    src = find_experience(args.no, row["slug"], row["name"])
    if not src:
        emit({"ok": False, "step": "exp", "found": False,
              "message": "没找到 %s 的实测。请到 Obsidian 的 01-拆解\\_实测表\\%03d-%s.md 里填 20 分钟实测" % (row["name"], int(args.no), row["slug"])})
        sys.exit(2)
    dst = os.path.join(d, "实测.md")
    shutil.copyfile(src, dst)
    emit({"ok": True, "step": "exp", "found": True, "source": src, "copied_to": os.path.basename(dst), "bytes": os.path.getsize(dst)})


# ---------- build ----------
def cmd_build(args):
    row = queue_row(args.no)
    if not row:
        fail("队列里没有第 %s 号" % args.no)
    d = dir_of(args.no, row["slug"])
    if not os.path.exists(os.path.join(d, "content.json")):
        fail("缺 content.json。写卡与文案要按 PIPELINE.md 第 5 步完成后再 build")
    rc, out = run([PY, os.path.join(TOOLS, "build_teardown.py"), os.path.basename(d)])
    if rc != 0 or "残留占位符=0" not in out:
        fail("渲染失败：%s" % out[-400:])
    rc2, out2 = run([PY, os.path.join(TOOLS, "build_wall.py")])
    if rc2 != 0:
        fail("进度墙刷新失败：%s" % out2[-300:])
    emit({"ok": True, "step": "build", "dir": os.path.basename(d),
          "html": [x for x in os.listdir(d) if x.endswith(".html")]})


# ---------- commit ----------
def cmd_commit(args):
    row = queue_row(args.no)
    name = row["name"] if row else args.no
    rc, out = run(["git", "add", "-A"])
    if rc != 0:
        fail("git add 失败：" + out[-300:])
    msg = "第 %s 篇 %s：报告与素材" % (args.no, name)
    rc, out = run(["git", "-c", "core.quotepath=false", "commit", "-m", msg])
    if rc != 0 and "nothing to commit" not in out:
        fail("git commit 失败：" + out[-300:])
    rc, out = run(["git", "push"])
    if rc != 0:
        fail("git push 失败（检查网络或凭证）：" + out[-300:])
    rc, head = run(["git", "rev-parse", "--short", "HEAD"])
    emit({"ok": True, "step": "commit", "commit": head.strip()})


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("next").set_defaults(fn=cmd_next)
    c = sub.add_parser("collect"); c.add_argument("no"); c.add_argument("--site"); c.add_argument("--pricing"); c.set_defaults(fn=cmd_collect)
    e = sub.add_parser("exp"); e.add_argument("no"); e.set_defaults(fn=cmd_exp)
    b = sub.add_parser("build"); b.add_argument("no"); b.set_defaults(fn=cmd_build)
    m = sub.add_parser("commit"); m.add_argument("no"); m.set_defaults(fn=cmd_commit)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
