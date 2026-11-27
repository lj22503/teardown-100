# -*- coding: utf-8 -*-
"""生成历史产品模板目录：13-template-catalog.csv + 14-template-catalog.md。
只记录「有没有公开模板库、在哪、多大、能不能拆模块」——没有的就写没有。
"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROWS = [
    ["001", "Notion", "yes", "官方模板市场", "https://www.notion.com/templates",
     "/templates/<slug>",
     "官方称 30,000+；分类计数：Personal Productivity 26,462 / Personal Planner 10,178 / Personal Goals 6,174 / Habit Tracking 3,555 / Student Life 8,064",
     "public", "no", "2（Weekly Planner / 2026 Monthly Planner）",
     "模板详情页的 About this template 是 JS 渲染；2026-11-26 登录后复查仍为空，公开页面拿不到模块清单；用分类计数 + 评分/评论作为结构信号",
     "https://www.notion.com/templates"],
    ["002", "Obsidian", "no", "社区（插件/主题）+ 工具", "https://community.obsidian.md/plugins",
     "/plugins/<slug>", "社区插件与主题为主，无官方模板市场；另有 Clipper/Canvas/CLI", "public", "n/a", "0",
     "无模板库；模板是用户自建 vault，官方只提供 Templates 核心插件；插件/主题/Clipper/Canvas/CLI 是主要资源", "https://community.obsidian.md/plugins"],
    ["003", "Capacities", "no", "无公开模板库", "https://capacities.io/templates",
     "", "/templates 返回 404；对象/模板在应用内", "login", "n/a", "0",
     "官网无公开模板库；模板是应用内的对象模板", "https://capacities.io/"],
    ["004", "Reflect", "no", "无公开模板库", "https://reflect.app/",
     "", "未找到公开模板页", "login", "n/a", "0",
     "无公开模板库", "https://reflect.app/"],
    ["005", "HyNote AI", "partial", "模板页（7 个）+ 集成目录", "https://hynote.ai/features/faq-template",
     "/features/<template>",
     "7 个模板页（FAQ/Resume/Outline/Case Study/SWOT/Brainstorm/Interview）；20+ 集成（ChatGPT/Claude/Notion/Slack/Zoom/Meet/Teams…）",
     "public", "no", "0",
     "有模板页但不是模板市场；详情页无模块清单，只做目录级", "https://hynote.ai/features/faq-template"],
    ["006", "Claude", "partial", "Prompt Library / Skills", "https://docs.anthropic.com/en/prompt-library",
     "/prompt-library/<slug>", "官方 prompt library + Skills（能力包）", "public", "no", "0",
     "不是模板市场：Prompt Library 是提示词模板，Skills 是能力包；两者结构不同，未按模板拆", "https://docs.anthropic.com/en/prompt-library"],
    ["007", "Framer", "yes", "官方模板市场", "https://www.framer.com/marketplace/templates/",
     "/marketplace/templates/<slug>", "20+ 分类；免费/付费；Agent Templates", "public", "yes", "3（Brevio / Tearsheet / Asher Vale）",
     "详情页有 What's inside / What you get / Who It's For，可结构化", "https://www.framer.com/marketplace/templates/"],
    ["008", "Cursor", "放弃", "—", "", "", "本期未完成，先放弃", "—", "n/a", "0",
     "008 原始目录就没有 README，模板层跳过", ""],
    ["009", "Figma", "yes", "官方社区 + 团队资源库（登录后）", "https://www.figma.com/files/team/1666643033011782866/resources/community",
     "/files/team/<id>/resources/community; /community/file/<id>",
     "板块：AI workflows（4 子类，20+ 个）/ Website templates 5 / UI kits 5 / Skills 6+ / Presentations / Assets；搜索 files and templates 100+（2026-11-26 登录实测）",
     "login", "partial", "5（Automated Ads / MockFit / Meta Ads / Match UI kit / Material 3 Expressive）",
     "公开 /community 的 body 是 SPA（只显示 Loading）；登录团队资源库后可读。部分文件有 What's inside / Key Features，多数只有 About 描述",
     "https://www.figma.com/files/team/1666643033011782866/resources/community"],
    ["010", "Fathom", "no", "资源中心 + 集成目录", "https://www.fathom.ai/resource-hub",
     "/resource-hub; /integrations/<tool>", "Resource Hub + 集成目录（视频会议/LLM/CRM）+ API + MCP", "public", "n/a", "0",
     "无模板库；资源是集成、API/MCP、案例与 use case，不是模板", "https://www.fathom.ai/resource-hub"],
    ["011", "ElevenLabs", "partial", "Voice Library / Agents", "https://elevenlabs.io/",
     "/voice-library; /agents", "voice library + agents（页面 JS 渲染）", "login", "no", "0",
     "不是模板市场；voice/agent 是资源但不是模板，未按模板拆", "https://elevenlabs.io/"],
    ["012", "Gamma", "yes", "官方模板库", "https://gamma.app/templates",
     "/templates/<slug>", "超过 100 个模板；19 个分类；列表共 46 页（2026-11-26 登录后实测）", "public", "no", "3（Sorbet / Deep Cut / Daktilo Dispatch）",
     "详情页有分类、风格描述与「使用此模板生成」入口，但没有模块清单；只做适配", "https://gamma.app/templates"],
    ["013", "Slack", "yes", "官方模板库", "https://slack.com/templates/gallery",
     "/templates/<slug>", "35 个模板 + 14 个分类 + gallery", "public", "yes", "6 模块 / 6 适配",
     "模板页有 Template features，可结构化", "https://slack.com/templates/gallery"],
    ["014", "Taskade", "yes", "官方模板库", "https://www.taskade.com/templates",
     "/templates/<category>/<slug>", "3,997 项目模板 / 3,169 agent / 2,361 自动化", "public", "yes", "6 模块 / 8 适配",
     "详情页有 What's Included + 组合计数，可结构化", "https://www.taskade.com/templates"],
]

HEADER = ["no", "product", "has_gallery", "gallery_type", "gallery_url", "url_pattern",
          "scale_note", "access", "modules_available", "sampled_templates", "notes", "evidence_url"]

csv_path = os.path.join(BASE, "13-template-catalog.csv")
with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(HEADER)
    w.writerows(ROWS)
print("written:", csv_path, len(ROWS), "rows")

md = ["# 历史与在库产品的模板目录（有没有、在哪、多大、能不能拆）", "",
      "> 规则：有公开模板库的，进 08/11 结构化；没有的，如实写「no / 未核验」，不硬造模板。",
      "> 判断列：`modules_available` = 能否从公开页面拿到模块清单。", "",
      "| 期号 | 产品 | 有模板库 | 类型 | 规模 | 可拆模块 | 已采样 | 入口 |",
      "|---|---|---|---|---|---|---|---|"]
for r in ROWS:
    no, product, hasg, gtype, gurl, pattern, scale, access, modules, sampled, notes, ev = r
    md.append(f"| {no} | {product} | {hasg} | {gtype} | {scale} | {modules} | {sampled} | {gurl} |")
md.append("")
md.append("## 说明")
md.append("")
for r in ROWS:
    no, product, hasg = r[0], r[1], r[2]
    notes = r[10]
    md.append(f"- **{no} {product}**（{hasg}）：{notes}")
md_path = os.path.join(BASE, "14-template-catalog.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md))
print("written:", md_path, len(md), "lines")
