# -*- coding: utf-8 -*-
"""清洗仓库里的 AI 生成声明（AIGC frontmatter）。

公众号发布时会粘 AIGC 声明，不能进仓库卡片。commit 前自动剥掉。
"""
import os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAT = re.compile(r"\A\ufeff?---\r?\nAIGC:[\s\S]*?\r?\n---\r?\n+", re.MULTILINE)


def main():
    fixed = []
    for root, dirs, files in os.walk(REPO):
        if ".git" in root or "_tools/run" in root.replace("\\", "/"):
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            p = os.path.join(root, f)
            try:
                s = open(p, encoding="utf-8").read()
            except Exception:
                continue
            if "AIGC:" not in s:
                continue
            s2 = PAT.sub("", s, count=1)
            if s2 != s:
                open(p, "w", encoding="utf-8").write(s2)
                fixed.append(os.path.relpath(p, REPO))
    if fixed:
        print("已剥离 AIGC 声明：%s" % ", ".join(fixed))
    else:
        print("干净，无需清洗")


if __name__ == "__main__":
    main()
