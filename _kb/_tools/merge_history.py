# -*- coding: utf-8 -*-
"""把历史 001–012 的回填行并入 01-products.csv（按 no 去重，保留 013/014 当前行）。
用法：python _tools/merge_history.py   （history 文件不存在时安全退出）
"""
import csv, os

BASE = r"D:\claudework\teardown-100\_kb"
CUR = os.path.join(BASE, "01-products.csv")
HIS = os.path.join(BASE, "raw", "history-products-rows.csv")

if not os.path.exists(HIS):
    print("history csv 不存在，跳过：", HIS)
    raise SystemExit(0)

with open(CUR, "r", encoding="utf-8-sig", newline="") as f:
    cur_rows = list(csv.reader(f))
header, cur = cur_rows[0], cur_rows[1:]

with open(HIS, "r", encoding="utf-8-sig", newline="") as f:
    his_rows = list(csv.reader(f))
his_header, his = his_rows[0], his_rows[1:]

if his_header != header:
    print("警告：表头不一致，按列名对齐")
    idx = {h: i for i, h in enumerate(his_header)}
    his = [[(r[idx[h]] if h in idx and idx[h] < len(r) else "") for h in header] for r in his]

# 保留 no >= 013 的行，历史行替换 001–012
keep = [r for r in cur if r and r[0].isdigit() and int(r[0]) >= 13]
merged = his + keep
merged.sort(key=lambda r: r[0])

with open(CUR, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(merged)

print("merged:", len(his), "history +", len(keep), "current =", len(merged), "rows")
for r in merged:
    print(" ", r[0], r[1], "|", r[3], "|", r[4][:40])
