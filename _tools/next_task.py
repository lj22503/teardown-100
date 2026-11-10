# -*- coding: utf-8 -*-
"""每日选题器。给 Marvis 和人共用，避免「靠目录名判断是否完成」跳号。

判定规则（严格顺序锁）：
  1. 按 queue.csv 的编号从小到大走，不许跳号
  2. 某一篇算「完成」的唯一标准：<dir>/teardown-zh.html 存在
  3. 如果最小未完成的那篇有目录但没报告 → 状态「待出报告」，不许去做下一号
  4. 如果连目录都没有 → 状态「待采集」
  5. 如果更前面有缺报告的 → 先报它，不许往后走

用法：
  python _tools/next_task.py          # 人看的中文一行
  python _tools/next_task.py --json   # 机器读
"""
import csv, os, sys, json
sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(ROOT, "_data", "queue.csv")


def load_queue():
    rows = []
    with open(QUEUE, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if str(r.get("no", "")).strip():
                rows.append(r)
    rows.sort(key=lambda r: int(r["no"]))
    return rows


def dir_of(r):
    return "%03d-%s" % (int(r["no"]), r["slug"])


def done(r):
    d = os.path.join(ROOT, dir_of(r))
    return os.path.exists(os.path.join(d, "teardown-zh.html"))


def main():
    rows = load_queue()
    total = len(rows)
    finished = [r for r in rows if done(r)]

    pending = next((r for r in rows if not done(r)), None)
    if pending is None:
        out = {"state": "all_done", "done": len(finished), "total": total,
               "message": "100 篇全部出报告了"}
    else:
        d = os.path.join(ROOT, dir_of(pending))
        has_dir = os.path.isdir(d)
        has_raw = os.path.exists(os.path.join(d, "_raw.md")) or os.path.exists(os.path.join(d, "_raw.md"))
        if has_dir and has_raw:
            state = "need_report"
            msg = "第 %d 篇 %s 素材齐了但缺报告，先出这篇，不许跳到下一号" % (int(pending["no"]), pending["name"])
        elif has_dir:
            state = "need_collect"
            msg = "第 %d 篇 %s 有目录但没采集完，先补采集" % (int(pending["no"]), pending["name"])
        else:
            state = "need_start"
            msg = "今天该做第 %d 篇 %s，从采集开始" % (int(pending["no"]), pending["name"])
        out = {"state": state, "no": int(pending["no"]), "name": pending["name"],
               "slug": pending["slug"], "dir": dir_of(pending),
               "done": len(finished), "total": total, "message": msg}

    # 额外检查：有没有「后面做了、前面空缺」的跳号
    gaps = []
    seen_undone = False
    for r in rows:
        if not done(r):
            seen_undone = True
        elif seen_undone:
            gaps.append(int(r["no"]))
    if gaps:
        out["gaps"] = gaps
        out["gap_warning"] = "跳号：第 %s 篇已出报告，但前面还有没出的" % "、".join(str(g) for g in gaps)

    if "--json" in sys.argv:
        print(json.dumps(out, ensure_ascii=False))
    else:
        print(out["message"])
        print("进度 %d/%d" % (out["done"], out["total"]))
        if out.get("gap_warning"):
            print(out["gap_warning"])


if __name__ == "__main__":
    main()
