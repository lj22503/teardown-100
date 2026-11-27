# -*- coding: utf-8 -*-
"""把历史产品的模板数据（data/history-template-*.csv）合并进 08/11 主表。
幂等：先删掉 08/11 里 template_id 命中历史集合的行，再追加。
"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")

def read(p):
    with open(p, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    return rows[0], rows[1:]

def merge(target, source):
    tp = os.path.join(BASE, target)
    sp = os.path.join(DATA, source)
    if not os.path.exists(sp):
        print("skip (no source):", source); return
    h, rows = read(tp)
    sh, srows = read(sp)
    if sh != h:
        print("!! 表头不一致:", source); return
    ids = {r[0] for r in srows if r}
    kept = [r for r in rows if r and len(r) == len(h) and r[0] not in ids]
    srows = [r for r in srows if r and len(r) == len(h)]
    out = kept + srows
    with open(tp, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(h)
        w.writerows(out)
    print(f"{target}: {len(rows)} -> {len(out)} (+{len(srows)}, -{len(rows)-len(kept)})")

merge("08-template-modules.csv", "history-template-modules.csv")
merge("11-template-fit.csv", "history-template-fit.csv")
