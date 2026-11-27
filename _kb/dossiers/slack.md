# Slack 深度调研（013）

> 日期：2026-11-26 ｜ 事实来源：官方页 + 官方 sitemap 实测（`_kb/raw/slack-raw.md`，305 行，每条带 URL）
> 本文回答三件事：**① 它是为谁解决什么 ② 它的 AI 是怎么用原子能力拼出来的 ③ 它靠什么被看见**。
> 结尾给「我们能拿走的 5 条」与「事实缺口」。

---

## 0. 一句话判断

**Slack 不是聊天工具，是「把业务动作标准化成消息流原子」的平台；它的 AI 战略不是造模型，而是当 agent 的托管层（双向 MCP + Skills + 权限）。**

三句补充：
1. 它的护城河不在功能，在**接入协议 + 权限模型 + 工作场所占据**——所以 2,600+ 应用愿意接它，而不是它去做 2,600 个功能。
2. 2026 年它的 AI 结构是「**双向 MCP**」：外部 AI 能读写 Slack（Slack MCP Server），Slackbot 也能调你的 MCP server（Slackbot MCP Client）。这是它把自己变成「agent 的家」的关键一步。
3. 它的定价分水岭已经从「席位」变成「**Slackbot 额度**」——AI 时代的计价单位在变。

---

## A. 定位：为谁、解决什么、哪些场景

### A1. 主张的三级跳（都在官网同时存在）

| 阶段 | 官方措辞 | 说明 |
|---|---|---|
| 聊天工具 | "Slack connects your team." | 最早的心智 |
| 工作操作系统 | "Where work happens." / "work OS" | 把频道当工作场所 |
| **Agent 运行底座** | "The platform agents and AI call home." | 2026 的主叙事：不做 agent，做 agent 的家 |

### A2. 客户分层与定价（事实，来自定价页）

| 档位 | 价格（官方） | 卖的是什么 | AI 的差别 |
|---|---|---|---|
| **Free** | $0，永久免费 | 90 天消息历史、最多 10 个 app、1:1 huddle、1:1 外部 DM | Basic AI（摘要/Slackbot 试用/AI 工作流生成/搜索/每日回顾/文件摘要） |
| **Pro** | $8.75/人/月（年付 $7.25） | 无限历史、无限 app、群组 huddle、最多 250 个外部组织 | 同上（Slackbot 仍只是试用） |
| **Business+** | $18/人/月（年付 $15） | 管理/合规：多工作区、细分角色、信息屏障、法定保留、Discovery API、HIPAA | **Slackbot 持续可用** |
| **Enterprise+** | $45/人/月（年付，Contact Sales） | 企业级 AI + 合规：多 SAML、data residency | **Slackbot 无周消息上限** |

**关键事实（推断由此展开）**：
- Free/Pro 的 Slackbot 只是 "limited trial"；Business+/Enterprise+ 才持续可用；只有 Enterprise+ 写 "no weekly message limits"；超额买 Salesforce Flex Credits。（https://slack.com/pricing）
- Workflow Builder 是付费功能（Pro 起）。（https://slack.com/features/workflow-automation）
- 单档独立页 `/pricing/free`、`/pricing/pro`、`/pricing/businessplus`、`/pricing/paid-vs-free` 都在 sitemap 里——**定价页本身被拆成 4 个 SEO 入口**。

### A3. 场景清单（官方 Solutions，sitemap 可数）

- 部门 9 个：Frontline、Engineering、IT、Customer Service、Sales、Project Management、Marketing、HR、Security
- 行业 9 个：制造/汽车/能源、科技、媒体、中小企业、金融服务、零售、公共部门、教育、医疗生命科学
- Use case 11 个：项目管理、客户协作、高效会议、销售管道、内部沟通、项目跟踪、线索管理、团队生产力、员工入职、工时跟踪、快速找答案

---

## B. 信息架构：真的点得到的东西

### B1. 五个 surface（都长在同一个壳里）

| Surface | 职责 | 证据 |
|---|---|---|
| **Channel** | 按主题聚合人/文件/应用/AI 的容器 | https://slack.com/features/channels |
| **Slack Connect** | 把外部组织拉进同一批频道 | https://slack.com/connect |
| **Canvas / List** | 频道内的文档与结构化任务表 | https://slack.com/features/canvas ；/features/task-list |
| **Huddle / Clip** | 音视频会议与异步录制 | https://slack.com/features/huddles ；/features/clips |
| **Slackbot / Agent** | 可被 @ 的 AI 成员 | https://slack.com/features/slackbot |

### B2. 实体关系（为什么它能被 2,600 个 app 接进来）

```
Workspace
└── Channel（容器，权限的边界）
    ├── Message / Thread（对话最小单元）
    ├── Canvas（文档）
    ├── List（结构化数据）
    ├── Workflow（触发器+步骤）
    └── App / Agent（身份，可被 @）
            └── MCP tool / Web API（工具）
```

**关键设计**：Slack 没有为 AI 造一个新界面——**所有 AI 能力都长在已有的容器里**（消息、频道、画布、列表）。这是它能接住 agent 的根本原因：agent 对用户来说就是「频道里一个能 @ 的成员」。

---

## C. AI 是怎么拼出来的（核心）

### C1. 原子能力：从 30 条里收敛成 12 个组合基元

| 基元 | 类型 | 一句话 | 能拼成什么 |
|---|---|---|---|
| Channel | 容器 | 权限边界 + 对话流 | 所有东西的载体 |
| Canvas | 容器 | 可协作文档 | 简报/FAQ/skill 指令载体 |
| List | 容器 | 结构化任务表 | 项目跟踪/CRM/工单 |
| Message/Thread | 动作 | 最小对话单元 | 被 AI 摘要/触发工作流 |
| Huddle | 动作 | 即时音视频 | 会议→笔记→行动项 |
| App | 身份 | 第三方/自建身份 | 任何外部能力 |
| Agent | 身份 | 可被 @ 的成员 | 执行者 |
| Slackbot | 身份+编排 | 团队 AI 队友 | 调工具/建产物 |
| Workflow | 编排 | 触发器+步骤+条件（最多 15 条件） | 自动化 |
| MCP tool | 工具 | 外部能力标准化 | agent 的手脚 |
| Search / Real-Time Search API | 知识 | 读上下文 | agent 的上下文 |
| 权限/合规 | 约束 | scopes/审批/审计 | 能不能做 |

### C2. 拼接公式

> **容器 × 身份 × 权限 × 触发器 × 工具 = 一个工作流**

例子（官方都在用）：
- `Channel + App + OAuth scopes + 事件 + Web API` = 一个频道里的第三方应用
- `Channel + Agent + MCP tool + 权限 + @` = 一个可被叫来干活的 AI 成员
- `Workflow(trigger) + 条件 + 连接器 + 消息步骤` = 一条自动化
- `Huddle + AI 摘要 + Canvas` = 会议纪要流水线

### C3. 三种「封装」——这是 Slack 最值得抄的结构

| 封装 | 面向谁 | 机制 | 为什么重要 |
|---|---|---|---|
| **Template** | 人 | 预配置 channel + canvas + list + workflow 的整套骨架 | 把一个团队的「怎么干活」变成可复制起点 |
| **Slackbot Skills** | 团队方法 | 用 markdown 或 canvas 写指令 → 组织级发布 → 全队一键跑 | **个人工作流 → 组织资产**（这是知识库产品化范式） |
| **Agent + 双向 MCP** | 机器 | Slack MCP Server（外部 AI 读写 Slack）+ Slackbot MCP Client（Slack 调你的 server） | 把 Slack 变成 agent 的家：谁来都能住 |

**一句话**：Slack 的统一能力不是某个功能，而是**「把任意业务动作变成频道里一次可被 @ 的调用」**。

### C4. 与 Taskade 的路线对比（后面 014 会展开）

- **Slack = 协议层**：标准化身份/权限/事件/消息，让别人来适配（横向生态）。
- **Taskade = 模板层**：同一份数据模型，用四种封装（项目/agent/自动化/app）批量复制（纵向程序化）。

---

## D. 流量曝光：它靠什么被看见（全部可数）

### D1. SEO 规模（sitemap 实测，2026-11-26）

| 板块 | 英文 URL 数 | 说明 |
|---|---|---|
| 营销站 | **1,769** | 13 个语种各一份（zh-CN 1,478） |
| ├ /blog/* | 1,179 | **最大单一板块**（内容营销主力） |
| ├ /customer-stories/* | 199 | 采购决策期关键词 |
| ├ /resources/* | 107 | 指南/报告 |
| ├ /templates/* | 50 | 1 gallery + 14 分类 + 35 模板 |
| ├ /solutions/* | 32 | 9 部门 + 9 行业 + 11 use case + 4 其他 |
| ├ /features/* | 23 | 功能页 |
| └ /events/* /trust/* /pricing/* /compare/* | 22 / 17 / 4 / 4 | 尾部 |
| **Marketplace** | **2,881** | 2,871 个第三方应用页 + 9 collection + 首页 |
| **Help Center** | **579** | 578 篇 × 13 语言 |
| **合计（英文）** | **≈5,229** | 再加 12 个语种的重复 |

### D2. 对比页：两套并存

- 产品级：`/compare/slack-vs-teams`、`/compare/slack-vs-email`（带锚点目录 + 6 条理由 + 94%/97min/1.7M 数字）
- 博客级：`/blog/compare/*` **18 条** = 13 个竞品 vs 页 + 4 个 alternatives 页 + 1 个德语法务页

### D3. 渠道组合

| 渠道 | 证据 |
|---|---|
| **PLG 免费档** | 所有页面 CTA 是 "Get started"，无销售介入；免费档含 AI 摘要与 Slackbot 试用 |
| **企业销售** | 每页并行 "Talk to sales"；链接带来源参数（?id=slackbot、?from_teams_compete=1） |
| **Partner/认证** | Partner Program、Partner Offers、Slack Certified |
| **社区/活动/客户故事** | Community、22 个 events 页、199 个客户故事 |
| **Marketplace 生态** | 2,871 个第三方应用页，第三方自带流量回流 |
| **Salesforce 渠道** | 署名「Salesforce 旗下」、Slackbot 进 Lightning、Flex Credits 走 Salesforce 售卖 |

### D4. 增长史（公开可查）

2013-08 发布（24 小时 8,000 客户）→ 2015 每周新增 1 万 DAU → 2018 收购 HipChat/Stride → 2019 DPO 上市（195 亿美元）→ 2020-12 Salesforce 277 亿美元收购 → 2023 ChatGPT 集成 → 2025-05 Agentforce 进 Slack → **2025-06 开始阻止 LLM 长期索引/复制 Slack 数据**。

**判断（[推断]）**：三条腿并行，权重 PLG 自传播 > 大站 SEO > Salesforce 企业渠道。依据：定价页的零销售 CTA、sitemap 的页面结构、企业页与 contact-sales 的多入口。

---

## E. 资源清单（它内置了哪些可复用资产）

| 层 | 资源 | 数量/入口 | 解决什么问题 |
|---|---|---|---|
| **装** | Marketplace 应用 | 2,600+（sitemap 2,871 页）、23 个分类、8 个编辑合集、MCP Registry | 把外部系统接进会话 |
| **抄** | 模板库 | 35 个模板 + 14 个职能分类 + gallery | 不用从零配 channel/canvas/list/workflow |
| **抄** | Agent 模板 | onboarding / support / customer insights | 快速部署一个 agent |
| **学** | 开发者文档 | 359 个 API、121 个事件、129 个 scope、46 个 block element、3,266 个文档 URL | 自己造 app/agent |
| **学** | 官方 samples + CLI + SDK | 8 个 samples、90 个 CLI 命令页、Bolt（JS/Python/Java）、Deno SDK | 跳过搭建直接改 |
| **接** | Slack MCP Server | `https://mcp.slack.com/mcp`（远程 HTTP + OAuth） | 让外部 AI 读写 Slack |
| **接** | Slackbot MCP Client | 4 种鉴权 | 让 Slackbot 调你的服务 |
| **接** | Real-Time Search API | 权限感知、不落地 | 给 agent 上下文 |
| **组织** | Slackbot Skills | markdown/canvas → 组织级发布 | 个人方法变全队能力 |
| **信任** | 客户故事 199 + 认证 | — | 采购评估 |

**资源的组织逻辑**：按「**装 → 抄 → 学 → 接**」四层排，而不是按功能排。这个顺序就是用户上手的顺序。

---

## F. 我们能拿走的 5 条（判断，不是事实）

1. **优先做「协议/插件」，不要做「又一个界面」。** Slack 证明：定义好身份+权限+事件+消息格式，生态会替你长功能。我们的工具应该先做成 MCP server / Skill 插件，去别人的场景里被调用。
2. **把「个人方法」做成「组织资产」。** Slackbot Skills 的机制（markdown 或 canvas 写成指令 → 组织级发布 → 一键跑）就是知识库产品化的标准形态：**规则写成文件、发布成能力、按需调用**。
3. **模板要分两种**：一种是「团队骨架」（channel+canvas+list+workflow 的整套配置），一种是「可发布的技能」（一段指令）。前者卖「开箱即用」，后者卖「经验复制」。
4. **定价单位跟着 AI 走。** Slack 用 Slackbot 额度而不是席位做分水岭。我们的产品也应有一档按「AI 执行量」计价，而不是只按人头。
5. **AI 时代的分发在收紧。** Slack 2025-06 开始阻止 LLM 长期索引 → 平台对 AI 抓取的防御在增强。做 GEO 不能只指望公开抓取，要准备「被授权调用」（MCP/合作/llms.txt）的路径。

---

## G. 事实缺口（不编）

| 缺口 | 状态 |
|---|---|
| DAU/MAU/付费席位/ARR | 官方未披露；只有「10 亿+ 每日消息」「400 万 Connect 用户」「300 万 每日工作流」等间接数 |
| 网站流量/自然搜索占比 | 未取 Similarweb/Ahrefs；sitemap 只能证明页面规模，不能证明流量 |
| Marketplace 准确应用数 | 官方 2,600+ vs sitemap 2,871，不一致（可能含下架） |
| Slackbot 周消息限额具体数值 | 未公布，只写 "no weekly message limits"（Enterprise+） |
| Workflow Builder 免费档可用性 | 官方自相矛盾：功能页说付费功能，定价页 Free 档列出 "AI workflow generation"（可能不是同一能力） |
| 各档转化率/ACV | 无披露 |

---

## 来源

主底稿：`_kb/raw/slack-raw.md`（A–G 七段，每条带 URL）。
关键来源：slack.com/pricing、/features/agentic-platform、/features/slackbot、/features/workflow-automation、/marketplace、/templates/gallery、/compare/slack-vs-teams、api.slack.com、docs.slack.dev（sitemap 计数）、slack.com/sitemap.xml 及 4 个子 sitemap。

---

## 报告

- 中文：`013-slack/teardown-zh.html`
- 英文：`013-slack/teardown-en.html`
