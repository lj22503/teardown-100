# -*- coding: utf-8 -*-
"""把历史 001–012 的原子/工作流并入 02/03（幂等：按 product 删除后再追加）。"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")
HIST = {"notion","obsidian","capacities","reflect-notes","hynote-ai","claude","framer","figma","fathom","elevenlabs","gamma-3"}

def merge(target, source):
    tp = os.path.join(BASE, target); sp = os.path.join(DATA, source)
    if not os.path.exists(sp):
        print("skip", source); return
    with open(tp, "r", encoding="utf-8-sig", newline="") as f:
        old = list(csv.reader(f))
    header = old[0]
    with open(sp, "r", encoding="utf-8-sig", newline="") as f:
        new = list(csv.reader(f))
    nh = new[0]
    assert nh == header, (target, nh, header)
    kept = [r for r in old[1:] if r and len(r) == len(header) and r[1] not in HIST]
    out = kept + [r for r in new[1:] if r and len(r) == len(header)]
    with open(tp, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(out)
    print(f"{target}: {len(old)-1} -> {len(out)} (+{len(out)-(len(old)-1)})")

merge("02-atoms.csv", "history-atoms.csv")
merge("03-workflows.csv", "history-workflows.csv")
