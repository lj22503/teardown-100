# 历史与在库产品的模板目录（有没有、在哪、多大、能不能拆）

> 规则：有公开模板库的，进 08/11 结构化；没有的，如实写「no / 未核验」，不硬造模板。
> 判断列：`modules_available` = 能否从公开页面拿到模块清单。

| 期号 | 产品 | 有模板库 | 类型 | 规模 | 可拆模块 | 已采样 | 入口 |
|---|---|---|---|---|---|---|---|
| 001 | Notion | yes | 官方模板市场 | 官方称 30,000+；分类计数：Personal Productivity 26,462 / Personal Planner 10,178 / Personal Goals 6,174 / Habit Tracking 3,555 / Student Life 8,064 | no | 2（Weekly Planner / 2026 Monthly Planner） | https://www.notion.com/templates |
| 002 | Obsidian | no | 社区（插件/主题）+ 工具 | 社区插件与主题为主，无官方模板市场；另有 Clipper/Canvas/CLI | n/a | 0 | https://community.obsidian.md/plugins |
| 003 | Capacities | no | 无公开模板库 | /templates 返回 404；对象/模板在应用内 | n/a | 0 | https://capacities.io/templates |
| 004 | Reflect | no | 无公开模板库 | 未找到公开模板页 | n/a | 0 | https://reflect.app/ |
| 005 | HyNote AI | partial | 模板页（7 个）+ 集成目录 | 7 个模板页（FAQ/Resume/Outline/Case Study/SWOT/Brainstorm/Interview）；20+ 集成（ChatGPT/Claude/Notion/Slack/Zoom/Meet/Teams…） | no | 0 | https://hynote.ai/features/faq-template |
| 006 | Claude | partial | Prompt Library / Skills | 官方 prompt library + Skills（能力包） | no | 0 | https://docs.anthropic.com/en/prompt-library |
| 007 | Framer | yes | 官方模板市场 | 20+ 分类；免费/付费；Agent Templates | yes | 3（Brevio / Tearsheet / Asher Vale） | https://www.framer.com/marketplace/templates/ |
| 008 | Cursor | 放弃 | — | 本期未完成，先放弃 | n/a | 0 |  |
| 009 | Figma | yes | 官方社区 + 团队资源库（登录后） | 板块：AI workflows（4 子类，20+ 个）/ Website templates 5 / UI kits 5 / Skills 6+ / Presentations / Assets；搜索 files and templates 100+（2026-11-26 登录实测） | partial | 5（Automated Ads / MockFit / Meta Ads / Match UI kit / Material 3 Expressive） | https://www.figma.com/files/team/1666643033011782866/resources/community |
| 010 | Fathom | no | 资源中心 + 集成目录 | Resource Hub + 集成目录（视频会议/LLM/CRM）+ API + MCP | n/a | 0 | https://www.fathom.ai/resource-hub |
| 011 | ElevenLabs | partial | Voice Library / Agents | voice library + agents（页面 JS 渲染） | no | 0 | https://elevenlabs.io/ |
| 012 | Gamma | yes | 官方模板库 | 超过 100 个模板；19 个分类；列表共 46 页（2026-11-26 登录后实测） | no | 3（Sorbet / Deep Cut / Daktilo Dispatch） | https://gamma.app/templates |
| 013 | Slack | yes | 官方模板库 | 35 个模板 + 14 个分类 + gallery | yes | 6 模块 / 6 适配 | https://slack.com/templates/gallery |
| 014 | Taskade | yes | 官方模板库 | 3,997 项目模板 / 3,169 agent / 2,361 自动化 | yes | 6 模块 / 8 适配 | https://www.taskade.com/templates |

## 说明

- **001 Notion**（yes）：模板详情页的 About this template 是 JS 渲染；2026-11-26 登录后复查仍为空，公开页面拿不到模块清单；用分类计数 + 评分/评论作为结构信号
- **002 Obsidian**（no）：无模板库；模板是用户自建 vault，官方只提供 Templates 核心插件；插件/主题/Clipper/Canvas/CLI 是主要资源
- **003 Capacities**（no）：官网无公开模板库；模板是应用内的对象模板
- **004 Reflect**（no）：无公开模板库
- **005 HyNote AI**（partial）：有模板页但不是模板市场；详情页无模块清单，只做目录级
- **006 Claude**（partial）：不是模板市场：Prompt Library 是提示词模板，Skills 是能力包；两者结构不同，未按模板拆
- **007 Framer**（yes）：详情页有 What's inside / What you get / Who It's For，可结构化
- **008 Cursor**（放弃）：008 原始目录就没有 README，模板层跳过
- **009 Figma**（yes）：公开 /community 的 body 是 SPA（只显示 Loading）；登录团队资源库后可读。部分文件有 What's inside / Key Features，多数只有 About 描述
- **010 Fathom**（no）：无模板库；资源是集成、API/MCP、案例与 use case，不是模板
- **011 ElevenLabs**（partial）：不是模板市场；voice/agent 是资源但不是模板，未按模板拆
- **012 Gamma**（yes）：详情页有分类、风格描述与「使用此模板生成」入口，但没有模块清单；只做适配
- **013 Slack**（yes）：模板页有 Template features，可结构化
- **014 Taskade**（yes）：详情页有 What's Included + 组合计数，可结构化