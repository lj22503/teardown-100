# -*- coding: utf-8 -*-
"""从 11-template-fit.csv 重新生成人读版 12-template-fit.md（含历史产品）。
必须在 merge_templates 之后跑，否则只有 013/014。
"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(BASE, "11-template-fit.csv")
with open(src, "r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

lines = ["# 模板适配表：适合谁 / 什么场景 / 怎么用", "",
         "> 用法：先按「适合谁 + 场景」筛，再去看 `08-template-modules.csv` / `09-template-anatomy.md` 的模块，最后点模板链接。",
         "> 适合谁 / 场景 多数是人工判断（`fit_basis` 已标）；怎么用 / 价值 优先用官方原文。", "",
         "| 模板 | 产品 | 适合谁 | 什么场景 | 怎么用（节选） | 组合 | 链接 |",
         "|---|---|---|---|---|---|---|"]
for r in rows:
    how = (r.get("how_to_use") or "").replace("|", "／")
    if len(how) > 70:
        how = how[:70] + "…"
    lines.append(f"| {r.get('template_name','')} | {r.get('product','')} | {r.get('for_whom','')} | {r.get('scenario','')} | {how} | {r.get('composition','')} | {r.get('evidence_url','')} |")
lines.append("")
lines.append("## 逐个模板")
lines.append("")
for r in rows:
    lines.append(f"### {r.get('product','')} · {r.get('template_name','')}")
    lines.append("")
    if r.get("what_it_is"):
        lines.append(f"- **是什么**：{r['what_it_is']}")
    lines.append(f"- **适合谁**：{r.get('for_whom','')}（{r.get('fit_basis','')}）")
    lines.append(f"- **什么场景**：{r.get('scenario','')}")
    if r.get("composition"):
        lines.append(f"- **组合**：{r['composition']}")
    if r.get("how_to_use"):
        lines.append(f"- **怎么用**：{r['how_to_use']}")
    if r.get("value"):
        lines.append(f"- **为什么用它**：{r['value']}")
    lines.append(f"- **模板页**：{r.get('evidence_url','')}")
    lines.append("")

out = os.path.join(BASE, "12-template-fit.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("written:", out, len(rows), "templates")
