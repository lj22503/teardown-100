# -*- coding: utf-8 -*-
"""同步 GitHub 主页（lj22503/lj22503）的连载入口：进度 N/100 + 最新一篇链接。

Marvis 每次 commit 后都要跑一次：python _tools/build_profile.py
"""
import os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = r"D:\claudework\_profile"
PROFILE_REMOTE = "git@github.com:lj22503/lj22503.git"
BASE = "https://github.com/lj22503/teardown-100"


def run(cmd, cwd):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def ensure_clone():
    if not os.path.isdir(os.path.join(PROFILE, ".git")):
        os.makedirs(os.path.dirname(PROFILE), exist_ok=True)
        rc, out = run(["git", "clone", PROFILE_REMOTE, PROFILE], os.path.dirname(PROFILE))
        if rc != 0:
            print("ERROR=克隆主页仓库失败：" + out[-300:])
            sys.exit(1)
    else:
        run(["git", "pull", "--ff-only"], PROFILE)


def scan():
    """返回 (已完成数, 最新一篇 no/name/slug, 总数)"""
    import csv
    rows = list(csv.DictReader(open(os.path.join(REPO, "_data", "queue.csv"), encoding="utf-8-sig")))
    rows.sort(key=lambda r: int(r["no"]))
    done = []
    for r in rows:
        d = os.path.join(REPO, "%03d-%s" % (int(r["no"]), r["slug"]))
        if os.path.exists(os.path.join(d, "teardown-zh.html")):
            done.append(r)
    latest = done[-1] if done else None
    return len(done), latest, len(rows)


def main():
    ensure_clone()
    readme = os.path.join(PROFILE, "README.md")
    if not os.path.exists(readme):
        print("ERROR=主页仓库没有 README.md")
        sys.exit(1)

    n, latest, total = scan()
    if not latest:
        print("SKIP 还没有任何完成篇目")
        return
    line = ("进度 **%d / %d** → [teardown-100](%s) ｜ 最新一篇：[%s](%s/tree/main/%03d-%s)"
            % (n, total, BASE, latest["name"], BASE, int(latest["no"]), latest["slug"]))

    s = open(readme, encoding="utf-8").read()
    pat = re.compile(r"进度 \*\*\d+ / \d+\*\* → \[teardown-100\]\([^)]*\).*")
    if pat.search(s):
        s2 = pat.sub(line, s, count=1)
    else:
        s2 = s.rstrip() + "\n\n" + line + "\n"
    if s2 == s:
        print("RESULT={\"ok\": true, \"changed\": false, \"progress\": \"%d/%d\"}" % (n, total))
        return

    open(readme, "w", encoding="utf-8").write(s2)
    rc, out = run(["git", "add", "-A"], PROFILE)
    if rc != 0:
        print("ERROR=git add 失败：" + out[-200:])
        sys.exit(1)
    rc, out = run(["git", "commit", "-m", "更新连载进度：%d/%d，最新 %s" % (n, total, latest["name"])], PROFILE)
    if rc != 0 and "nothing to commit" not in out:
        print("ERROR=git commit 失败：" + out[-200:])
        sys.exit(1)
    rc, out = run(["git", "push"], PROFILE)
    if rc != 0:
        print("ERROR=push 主页失败：" + out[-200:])
        sys.exit(1)
    print("RESULT={\"ok\": true, \"changed\": true, \"progress\": \"%d/%d\", \"latest\": \"%s\"}"
          % (n, total, latest["name"]))


if __name__ == "__main__":
    main()
