# -*- coding: utf-8 -*-
"""把 _kb 的五张 CSV 汇总成一个 Excel 工作簿（中文 sheet 名、冻结表头、自动列宽）。
同时把五张表以 UTF-8 BOM 另存到 _kb/_csv_bom/，供 Excel 直接双击打开。
CSV 被占用时（Excel 打开中）不覆盖原文件，只写备份目录。
"""
import csv, os, shutil

BASE = r"D:\claudework\teardown-100\_kb"
BOM_DIR = os.path.join(BASE, "_csv_bom")
os.makedirs(BOM_DIR, exist_ok=True)

TABLES = [
    ("01-products.csv",  "产品主档"),
    ("02-atoms.csv",     "原子能力"),
    ("03-workflows.csv", "工作流成品"),
    ("04-channels.csv",  "流量渠道"),
    ("05-resources.csv", "资源清单"),
    ("08-template-modules.csv", "模板解剖"),
    ("11-template-fit.csv", "模板适配"),
    ("13-template-catalog.csv", "模板目录"),
    ("15-template-taxonomy.csv", "标签结构"),
]

def read_csv(name):
    path = os.path.join(BASE, name)
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.reader(f))

# 1) xlsx
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

wb = Workbook()
wb.remove(wb.active)
head_fill = PatternFill("solid", fgColor="1F4E79")
head_font = Font(color="FFFFFF", bold=True, size=10)
for fname, sheet in TABLES:
    rows = read_csv(fname)
    ws = wb.create_sheet(sheet)
    for r in rows:
        ws.append(r)
    if not rows:
        continue
    for c in range(1, len(rows[0]) + 1):
        cell = ws.cell(row=1, column=c)
        cell.fill = head_fill
        cell.font = head_font
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:{get_column_letter(len(rows[0]))}{len(rows)}"
    # 列宽：按内容长度估，上限 60
    for c in range(1, len(rows[0]) + 1):
        lens = [len(str(row[c-1])) for row in rows[:200] if len(row) >= c]
        width = min(60, max(8, int(max(lens) * 1.6) if lens else 12))
        ws.column_dimensions[get_column_letter(c)].width = width
    # 正文自动换行 + 顶对齐
    for row in ws.iter_rows(min_row=2, max_row=min(len(rows), 300)):
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True)

xlsx_path = os.path.join(BASE, "知识库.xlsx")
wb.save(xlsx_path)
print("xlsx:", xlsx_path, os.path.getsize(xlsx_path), "bytes")

# 2) UTF-8 BOM CSV 备份
for fname, _ in TABLES:
    rows = read_csv(fname)
    out = os.path.join(BOM_DIR, fname)
    with open(out, "w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f).writerows(rows)
    print("bom csv:", out)

# 3) 尝试把原 CSV 也改成 BOM（被占用则跳过）
for fname, _ in TABLES:
    src = os.path.join(BASE, fname)
    rows = read_csv(fname)
    tmp = src + ".tmpbom"
    with open(tmp, "w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f).writerows(rows)
    try:
        os.replace(tmp, src)
        print("replaced with BOM:", fname)
    except OSError as e:
        os.remove(tmp)
        print("locked, kept original:", fname, "->", e.__class__.__name__)
