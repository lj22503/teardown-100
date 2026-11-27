# -*- coding: utf-8 -*-
"""从 08-template-modules.csv 生成「按模块反查模板」的选型索引 10-template-picker.md。"""
import csv, os
from collections import defaultdict

BASE = r"D:\claudework\teardown-100\_kb"
src = os.path.join(BASE, "08-template-modules.csv")

rows = []
with open(src, "r", encoding="utf-8-sig", newline="") as f:
    for r in csv.DictReader(f):
        rows.append(r)

# 模板适配表（适合谁/场景/怎么用）
fit = {}
fit_path = os.path.join(BASE, "11-template-fit.csv")
if os.path.exists(fit_path):
    with open(fit_path, "r", encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            fit[r["template_id"]] = r

by_type = defaultdict(lambda: defaultdict(list))   # type -> template -> [modules]
templates = {}
comps = {}
for r in rows:
    tkey = (r["product"], r["template_name"], r["evidence_url"])
    by_type[r["module_type"]][tkey].append(r["module_name"])
    if r.get("composition"):
        comps[tkey] = r["composition"]

lines = ["# 按模块反查模板（选型索引）", "",
         "> 用法：先想「我要什么模块」（表单 / 看板 / Agent / 集成 / 生成 / 文档 / 自动化），在这一页找到含该模块的模板，再去 `09-template-anatomy.md` 看它完整结构。",
         "> 数据来源：`08-template-modules.csv`（Taskade 抓官方 What's Included；Slack 抓 Template features）。", ""]

order = ["表单", "视图/看板", "Agent", "集成/同步", "生成/报告", "自动化", "文档/Canvas", "列表/List", "工作流", "门户/App", "界面", "工具", "智能", "分发", "模块"]
for typ in order:
    if typ not in by_type:
        continue
    lines.append(f"## {typ}")
    lines.append("")
    for (product, name, url), mods in sorted(by_type[typ].items(), key=lambda kv: (kv[0][0], kv[0][1])):
        uniq = []
        for m in mods:
            if m not in uniq:
                uniq.append(m)
        comp = comps.get((product, name, url), "")
        extra = f"（组合：{comp}）" if comp else ""
        # 找对应的 template_id（08 表里同一模板的任意一行）
        tid = next((r["template_id"] for r in rows if r["product"] == product and r["template_name"] == name), "")
        f = fit.get(tid, {})
        who = f.get("for_whom", "")
        scen = f.get("scenario", "")
        ctx = ""
        if who or scen:
            ctx = f"｜适合：{who}｜场景：{scen}"
        lines.append(f"- **{product} · {name}**：{', '.join(uniq[:4])}{extra}{ctx}")
        lines.append(f"  - {url}")
    lines.append("")

# 仅适配、无公开模块的模板（例如 Notion）
fit_only = []
ids_with_modules = {r["template_id"] for r in rows}
for tid, f in fit.items():
    if tid not in ids_with_modules:
        fit_only.append(f)
if fit_only:
    lines.append("## 仅适配（页面未公开模块）")
    lines.append("")
    for f in sorted(fit_only, key=lambda x: (x.get("product", ""), x.get("template_name", ""))):
        lines.append(f"- **{f.get('product','')} · {f.get('template_name','')}**｜适合：{f.get('for_whom','')}｜场景：{f.get('scenario','')}")
        if f.get("how_to_use"):
            lines.append(f"  - 怎么用：{f['how_to_use'][:120]}")
        lines.append(f"  - {f.get('evidence_url','')}")
    lines.append("")

# 未解剖清单
all_templates = set()
for r in rows:
    all_templates.add((r["product"], r["template_name"]))
expected = {
    ("Slack", "Bug Tracker"), ("Slack", "Incident Summary"),
    ("Taskade", "ai-project-dashboard-template"), ("Taskade", "expense-tracker"),
}
lines.append("## 未解剖（页面没有结构区，需人工看）")
lines.append("")
for p, n in sorted(expected):
    lines.append(f"- {p} · {n}（该模板页没有 What's Included / Template features，只能点开看）")
lines.append("")

out = os.path.join(BASE, "10-template-picker.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("written:", out, len(lines), "lines")
print("module types:", {k: len(v) for k, v in by_type.items()})
