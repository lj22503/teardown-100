# -*- coding: utf-8 -*-
"""从 08-template-modules.csv 重新生成 09-template-anatomy.md（含历史产品）。
必须在 merge_templates 之后跑。
"""
import csv, os
from collections import OrderedDict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(BASE, "08-template-modules.csv")
with open(src, "r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

groups = OrderedDict()
for r in rows:
    key = (r["product"], r["template_id"], r["template_name"])
    groups.setdefault(key, {"one": r.get("template_one_liner", ""), "comp": r.get("composition", ""), "url": r.get("evidence_url", ""), "mods": []})
    groups[key]["mods"].append((r.get("module_no", ""), r.get("module_name", ""), r.get("module_type", ""), r.get("detail", "")))
    if not groups[key]["comp"] and r.get("composition"):
        groups[key]["comp"] = r["composition"]

lines = ["# 模板解剖：这些模板里到底有哪些模块", "",
         "> 用途：不用点开 URL 也能知道一个模板由哪些模块组成；决定参考哪个之后，再点最后的链接。",
         "> 覆盖：013 Slack / 014 Taskade / 007 Framer（历史期里公开了 What's inside 的模板）。", ""]
for (product, tid, name), g in groups.items():
    lines.append(f"## {product} · {name}")
    lines.append("")
    if g["one"]:
        lines.append(f"**一句话**：{g['one']}")
        lines.append("")
    if g["comp"]:
        lines.append(f"**组合**：{g['comp']}")
        lines.append("")
    mods = sorted(g["mods"], key=lambda x: (len(x[0]), x[0]))
    for no, mname, mtype, detail in mods:
        d = f"：{detail}" if detail else ""
        lines.append(f"{no}. {mname}（{mtype}）{d}")
    lines.append("")
    lines.append(f"模板页：{g['url']}")
    lines.append("")

out = os.path.join(BASE, "09-template-anatomy.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("written:", out, len(groups), "templates")
