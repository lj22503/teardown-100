# -*- coding: utf-8 -*-
"""生成 17-resource-audit.md：资源/原子/工作流/模板 四层深度审计。"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(BASE, "17-resource-audit.csv"), "r", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

NOTES = {
    "001": "模板市场/Agent/顾问/Connections/Skills 5 条；原子 10、工作流 5 已补；模板模块仍公开不到。",
    "002": "插件/主题/核心模板/Clipper/Canvas/CLI 6 条；原子 9、工作流 5 已补。",
    "003": "Object/AI/每日笔记/App/导入导出 5 条；原子 9、工作流 5 已补。",
    "004": "AI/双链/Reflect Open/E2E/客户端 5 条；原子 9、工作流 5 已补。",
    "005": "AI Skills/7 模板页/20+ 集成/AI Skills/客户端 5 条；原子 10、工作流 5 已补。",
    "006": "Prompt Library/MCP/Projects/Cookbook/Connectors 5 条；原子 9、工作流 5 已补。",
    "007": "模板/插件/组件/Agent/Vectors 5 条 + 19 模块；原子 10、工作流 5。",
    "008": "本期放弃，四层均 0；建议重跑整期。",
    "009": "Community/团队库/插件/Skills/Widgets 5 条 + 25 模块；原子 10、工作流 5。",
    "010": "Resource Hub/集成/API/MCP/摘要模板 7 条；原子 10、工作流 5 已补。",
    "011": "Voice Library/Agents/API/Voice Design/Dubbing 5 条；原子 10、工作流 5。",
    "012": "模板/主题风格/生成格式 3 条；原子 9、工作流 5 已补；详情页无模块。",
    "013": "资源 8 + 模块 21 + 适配 6；原子/工作流本来就全。",
    "014": "资源 17 + 模块 30 + 适配 8；原子/工作流本来就全。",
}

def verdict(r):
    if r["no"] == "008":
        return "放弃"
    res, atoms, wfs, mods = int(r["resources"]), int(r["atoms"]), int(r["workflows"]), int(r["modules"])
    if mods >= 10:
        return "细"
    if atoms >= 8 and wfs >= 3:
        return "中上（可拼）"
    if res >= 3:
        return "中（仅目录）"
    return "薄"

lines = ["# 资源/原子/工作流 深度审计（001–014）", "",
         "> 结论：**013/014 最细；007/009 有模块；001–006、010–012 已补到「资源 + 原子 + 工作流」可拼装级；008 放弃。**",
         "> 判定：有模板模块=细；有原子+工作流=中上（可拼）；只有资源=中（仅目录）。", "",
         "| 期号 | 产品 | 资源 | 类型 | 原子 | 工作流 | 模块 | 适配 | 判定 |",
         "|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    lines.append(f"| {r['no']} | {r['name']} | {r['resources']} | {r['res_types']} | {r['atoms']} | {r['workflows']} | {r['modules']} | {r['fits']} | {verdict(r)} |")
lines.append("")
lines.append("## 逐产品说明")
lines.append("")
for r in rows:
    lines.append(f"### {r['no']} {r['name']}（{verdict(r)}）")
    lines.append("")
    lines.append(f"- 资源 {r['resources']} / 类型 {r['res_types']} / 原子 {r['atoms']} / 工作流 {r['workflows']} / 模块 {r['modules']} / 适配 {r['fits']}")
    lines.append(f"- {NOTES.get(r['no'], '')}")
    lines.append("")
lines.append("## 仍然缺的")
lines.append("")
lines.append("- **模块级**只有 007 Framer、009 Figma、013 Slack、014 Taskade；Notion/Gamma 页面不公开模块，Obsidian/Reflect/Fathom 等没有模板库，这是页面事实。")
lines.append("- **008 Cursor** 整期放弃；四层都是 0。")
lines.append("- **Figma AI workflows** 还有 17 个未解剖（已答应，单独一轮）。")

with open(os.path.join(BASE, "17-resource-audit.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("written 17-resource-audit.md", len(lines), "lines")
