# Taskade 调研底稿（2026-11-26）

> 采集方式：全部页面用 `Accept: text/markdown` 请求官方站点取得 Markdown 原文（官方 `llms.txt` 明确支持该请求头），另用各分区 sitemap 实测页数。
> 采集口径：只记原文与可数事实；无出处写「未核验」；推断一律标 `[推断]`。
> 采集范围：官网营销页 27 个、帮助中心索引（435 篇）、4 篇官方文档全文、4 个 App Kit 详情页、17 个 sitemap。

## 0. 路径核验（原任务给的路径已有失效）

| 任务给的 URL | 实际结果 | 现站真实路径 |
|---|---|---|
| `/use-cases` | **404** | 无此目录页；场景分散在 `/apps/categories`（72 类）与 `/learn/projects/for-*` |
| `/solutions` | **404** | 同上 |
| `/ai-agents` | 未用此路径 | 现为 `/ai/agents`（介绍页）与 `/agents`（Agent 模板库） |
| `/automation` | 未用此路径 | 现为 `/ai/automations`（介绍页）、`/automate`（配方库）、`/learn/automation`（文档） |
| `/templates` | 200 | 仍在，另有 `/templates/categories`、`/apps`（App Factory） |
| `/blog`、`/pricing`、`/features`、`/ai` | 200 | 保留 |
| 帮助中心 | 不在 `help.taskade.com` | `https://www.taskade.com/learn`（435 篇），开发者文档 `/docs`（169 篇），Wiki `/wiki`（573 篇） |

关键变化：站点已从「任务/笔记工具」整体重构为 **AI app builder（Taskade Genesis）**，导航第一层是 `Create / Connect / Clone / Pricing`。
证据：https://www.taskade.com/ ；https://www.taskade.com/about ；https://www.taskade.com/llms.txt

---

## A. 定位（为谁 / 解决什么 / 哪些场景）

### A1 官方一句话主张（原文 + URL）

- 首页 `<title>`：`Turn Business Processes Into Live Apps | Taskade Genesis`
  https://www.taskade.com/
- 首页首屏 H1：`AI Business App Builder: Taskade turns one prompt into apps, AI agents, and automated workflows in one living workspace.`（副行：`Apps that remember. Agents that reason. Workflows that keep running.`）
  https://www.taskade.com/
- 官方给 AI 读的自述（llms.txt 首段）：`Taskade is an AI-native workspace. Taskade Genesis turns one prompt into a live, hosted app. Each app runs on Workspace DNA: Projects hold the data, AI agents add intelligence, and automations act across 100+ integrations.`
  https://www.taskade.com/llms.txt
- 官方「该怎么引用我」指定主句：`Taskade Genesis turns a plain-language prompt into a live business app with connected project data, AI agents, and automations.`
  https://www.taskade.com/llms.txt
- About 页自我归类：`Agentic workspaces — Coordinate agents and humans together. The artifact is the running business.`；把 Slack / Notion / Asana / Linear 归为 `Human workspaces — Coordinate humans. Agents are bolted on.`
  https://www.taskade.com/about
- About 页用的类比（与本系列 013 期直接相关）：`In 2014, humans hit the same wall… Then Slack gave humans persistent rooms, integrations to real tools, and memory that did not reset every morning. Agents are now where humans were in 2013 — brilliant in isolation, useless without a workspace.`
  https://www.taskade.com/about
- 定价页 H1：`Choose your plan` / 副：`Build AI apps, agents, and automations in real time.`
  https://www.taskade.com/pricing
- 竞争对手页主张：`Taskade vs 150+ AI Tools, Compared`
  https://www.taskade.com/compare

### A2 客户分层与各档买什么

官方在产品内把买家分成 6 档（Free / Starter / Pro / Business / Max / Enterprise），每档都给了「谁买」的一句话：

| 档位 | 官方定位原话 | 买到的核心差异 | URL |
|---|---|---|---|
| Free | `For your first apps` | 3 个 app、1 个 agent、10 次自动化/月、2 个成员、250MB；无月度 credits（靠邀请/分享获得） | https://www.taskade.com/pricing |
| Starter | `For growing projects` | 10,000 credits、无限 app、3 个 agent、350 runs/月、3 人、去水印 | https://www.taskade.com/pricing |
| Pro | `For creators who ship` | 50,000 credits、无限 agent、1,000 runs/月、10 人、10 个自定义域名、100GB、MCP | https://www.taskade.com/pricing |
| Business | `For agencies and client work` | 150,000 credits、无限域名、白标+SEO、app analytics、10,000 runs/月、无限人、SAML | https://www.taskade.com/pricing |
| Max | `For heavy AI workloads` | 400,000 credits、4× Business 的 AI 请求上限、自动充值至 $1,000 | https://www.taskade.com/pricing |
| Enterprise | 未写副标，主打 SCIM / 专属 onboarding / 批量价 | 1.1M credits、SCIM、volume credit pricing | https://www.taskade.com/pricing |

另有一层「卖给 app 卖家」的身份：`Sell Your App as an App Kit`、`Earn From Your App Kits`、`Community Profiles: Publish Apps, Own Your Page`——把用户变成分发者。
https://www.taskade.com/llms.txt ；https://www.taskade.com/learn/genesis/sell-app-kits ；https://www.taskade.com/learn/account/community-profiles

### A3 场景清单（官方口径，列全）

官方没有 `/use-cases` 页，场景由三套互相平行的分类承载：

**(1) App Factory：72 个分类 = 48 类型 + 12 团队 + 12 行业**（每类都标了 App Kit 数量）
https://www.taskade.com/apps/categories

- 按类型（48）：Best 24、Dashboards 541、Boards 210、Commerce 185、Trackers 680、Invoices 211、CRMs 274、Inventory 149、Booking 200、Portals 225、Tools 1,284、Personal 304、Calendars 98、Projects 483、Planners 273、Budgets 89、Forms 226、Habits 74、Websites 226、Quick Apps 1,181、Notes 103、Schedules 132、Chatbots 154、Videos 117、Reports 227、Workflows 973、Intelligence 121、Entertainment 173、Courses 110、Quizzes 91、Games 183、Blogs 63、Portfolios 69、Calculators 331、Directories 164、Wikis 133、Forums 81、Photos 100、Helpdesks 113、Timesheets 63、Newsletters 63、Events 204、Recruiting 81、Maps 71、Puzzles 52、Diagrams 90、Generators 391、Converters 208
- 按团队（12）：Finance 621、Sales 461、Operations 998、Marketing 539、Content 367、HR 306、Support 178、Research 96、Design 231、Product 164、Engineering 269、Legal 166
- 按行业（12）：Retail 455、Health 284、Agency 287、Startups 211、Hospitality 332、Education 689、Property 208、Construction 203、Nonprofit 265、Logistics 126、Manufacturing 132、Field Service 232

**(2) 模板库分类：页面称 87 分类，sitemap 实测同为 87 个分类段**
https://www.taskade.com/templates/categories
页面原文：`Browse the Taskade template library across 87 categories`；但该页只渲染 15 个分类链接（JSON-LD `numberOfItems: 15`），其余靠分页/子分类存在。实测 `sitemap-templates.xml` 共 3,997 条：`/templates/<cat>/<slug>` 形式之外，一级页面 89 条 = 87 个分类落地页 + `/templates` + `/templates/categories`，分类段去重后正好 87 个，与文案一致。

**(3) 帮助中心的「Taskade for X」人群页**（官方写作的场景，非营销目录）
https://www.taskade.com/learn/projects/for-writers ；`for-students` ；`for-project-managers` ；`for-freelancers` ；`for-remote-teams` ；`for-product-management`

**(4) Agent 模板分类（9 类）**：Featured / Project Management / Productivity / Marketing / Translator / Content / Workflow / Research / Personal
https://www.taskade.com/agents

**(5) 自动化配方分类（9 类）**：Featured / AI Agent Automation / AI Workflow Automation / Logic Automations / Trigger Automations / Agentic Process Automation / Action Automations / AI Models in Workflows / Agentic Automation
https://www.taskade.com/automate

### A4 定价表（官方定价页 + 对比矩阵，2026-11-26）

| 项 | Free | Starter | Pro | Business | Max | Enterprise |
|---|---|---|---|---|---|---|
| 年付折算月价 | $0 | $6 | $10 | $25 | $100 | $250 |
| 年付总额 | $0 | $72 | $120 | $300 | $1,200 | $3,000 |
| 工作区成员 | 2 | 3 | 10 | 无限 | 无限 | 无限 |
| Live apps | 3 | 无限 | 无限 | 无限 | 无限 | 无限 |
| AI credits/月 | 需赚取 | 10K | 50K | 150K | 400K | 1.1M |
| 自动化 runs/月 | 10 | 350 | 1,000 | 10,000 | 10,000 | 10,000 |
| 自定义 Agent | 1 | 3 | 无限 | 无限 | 无限 | 无限 |
| 自定义域名 | — | — | 10 | 无限 | 无限 | 无限 |
| 存储 | 250MB | 5GB | 100GB | 1TB | 1TB | 1TB |
| 版本历史 | 7 天 | 30 天 | 1 年 | 5 年 | 5 年 | 5 年 |
| Webhook 触发 | — | — | ✅ | ✅ | ✅ | ✅ |
| Hosted MCP | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| 去水印 | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| 自有品牌色/SEO | — | — | — | ✅ | ✅ | ✅ |
| BYOK | — | — | OpenAI/Anthropic/Google | +xAI/DeepSeek/Mistral/OpenRouter | 同 Business | 同 Business |
| TSK 档位 | Instant | +Standard/Thinking | +Standard/Thinking | +Reasoning | +Reasoning | +Reasoning |
| SAML / SCIM | — | — | — | SAML | SAML | SAML + SCIM |

来源：https://www.taskade.com/pricing （价格与矩阵）；https://www.taskade.com/llms.txt （Plan entitlements that matter，官方称已对 entitlement matrix 核对）

补充事实：
- 年付省 50%：`Choose annual billing to save 50% compared with monthly billing on Pro, Business, Max, and Enterprise.` https://www.taskade.com/pricing
- Pro 月付 $20 有明确出处：`Pro costs $10 per month billed annually or $20 with monthly billing.` https://www.taskade.com/llms.txt
- 一次性硬限制：`Taskade does not run a student, education, or nonprofit discount program.` https://www.taskade.com/llms.txt
- 2026-09-08 起内置 Send Email 只能发给自己已验证地址，发外部要走 Gmail / Outlook 连接器 https://www.taskade.com/llms.txt
- 已发布 app 的访客不收钱：`Published Taskade Genesis apps run free for visitors.` https://www.taskade.com/llms.txt
- credits 按月计费周年日刷新，非自然月 1 号 https://www.taskade.com/llms.txt

---

## B. 信息架构与表层

### B1 全站导航（2026-11 实际结构）

一级：`Create`（建）· `Connect`（接）· `Clone`（克隆）· `Pricing`，另加 `Login / Sign up`。
「Build with AI」四个入口直接对应四种产物：
- Apps — `The default. Builds a complete app` → `/create?mode=genesis`
- AI Agents — `An AI agent with tools and knowledge` → `/create?mode=agents`
- Automations — `A flow that runs on a trigger` → `/create?mode=automation`
- Projects — `Tasks, docs, and workspace data` → `/create?mode=project`

二级分组：
- Templates：Agents `/agents` · Automations `/automate` · Projects `/templates`
- Connect：Connect Hub `/connect` · Integrations `/integrations` · Developer API `/docs` · Help Center `/learn` · Blog `/blog` · Customer Reviews `/reviews`
- Clone：Dashboards `/apps/dashboards` · Operations `/apps/operations` · Commerce `/apps/commerce` · All categories `/apps/categories`
- **For agents**：`SKILL.md` `/SKILL.md` · `MCP server` `/mcp` · `MCP setup guide` `/docs/mcp/hosted-mcp` · `llms.txt` `/llms.txt`
- 底部：Downloads `/downloads` · Changelog `/changelog` · App Factory `/apps`

来源：https://www.taskade.com/ （导航原文）；https://www.taskade.com/pricing （同导航，可复现）

> 注意：导航里有一整组 **For agents**，是给 AI 客户端（Claude / Cursor / Codex / VS Code）准备的入口，不是给人看的。首页还有一段 `Let your AI agent work in Taskade — Copy setup prompt: Set up Taskade for me. Read and follow https://www.taskade.com/SKILL.md`。

### B2 每个 surface 一句话职责

| Surface | 一句话职责（官方原文压缩） | URL |
|---|---|---|
| Taskade Genesis | 一句话提示词生成一个有数据、有 agent、有自动化、可发布的 app | https://www.taskade.com/create |
| Projects | 结构化数据层（Memory），一份数据多种视图 | https://www.taskade.com/learn/projects |
| Views（9 种） | List / Board / Table / Mind Map / Docs / Gantt / Calendar / Actionsheet / Org Chart，同一数据模型 | https://www.taskade.com/learn/projects/project-views |
| Custom Fields | 每个节点的带类型属性（enum/date/number 等） | https://www.taskade.com/learn/projects/custom-fields |
| AI Agents | 可训练的 AI 队友：指令 + 知识 + 记忆 + 工具 | https://www.taskade.com/learn/agents |
| Agent Tools | agent 能调用的动作库（研究/文档/AI/工作区/外部 app/自定义） | https://www.taskade.com/learn/agents/agent-tools |
| AI Teams | 多 agent 同群协作，四种模式 Auto/Everyone/Manual/Orchestrate | https://www.taskade.com/learn/agents/ai-teams |
| Automations | 触发器 + 动作 + 分支/循环/过滤，durable 执行 | https://www.taskade.com/learn/automation |
| Taskade EVE | 元 agent：建 app、建 agent、连自动化、管工作区，有审批与持久记忆 | https://www.taskade.com/learn/agents/eve-assistant |
| TSK Model Ladder | 用「任务档位」而不是厂商型号选模型（Auto/Instant/Standard/Thinking/Reasoning） | https://www.taskade.com/learn/agents/thinking-modes |
| Templates | 项目模板库（结构 + 可带 agent/自动化） | https://www.taskade.com/templates |
| Agent 模板库 | 现成 agent 按角色/行业 | https://www.taskade.com/agents |
| 自动化配方库 | 现成 trigger→action 流程，按集成/用途 | https://www.taskade.com/automate |
| App Factory | 社区已发布 app 的目录，可看 DNA、可克隆（免费/付费 App Kit） | https://www.taskade.com/apps |
| Integrations | 173 个连接器，6 类，双向 trigger/action | https://www.taskade.com/integrations |
| Publish / Custom Domain | app 发布到自有地址或自有域名，含 SSL | https://www.taskade.com/learn/genesis/publishing |
| App Users / GenesisAuth | 给已发布 app 加内置邮箱登录，独立的终端用户体系 | https://www.taskade.com/learn/genesis/app-users |
| Wiki | 概念级参考（不是操作手册），面向研究者 | https://www.taskade.com/wiki |
| Learn | 帮助中心，435 篇操作文档 | https://www.taskade.com/learn |
| Docs | 开发者文档：REST v1 / Action v2 / MCP / webhooks / SDK | https://www.taskade.com/docs |
| TSK-Bench | 公开的 AI 任务榜（模型在真实 app build 上的得分） | https://www.taskade.com/tsk |
| Generate / Convert | 4,526 个免费生成器页 / 2,118 个免费转换器页 | https://www.taskade.com/generate ；https://www.taskade.com/convert |

### B3 关键实体与关联

官方自己给的实体关系是 **3 层 × 3 面 = 9 格**（About 页原文）：

```
Projects（Memory：存状态）    → Lists / Tables(视图) / Custom Fields
Agents（Intelligence：读+判断）→ Commands / Knowledge / Tools
Workflows（Execution：触发+执行）→ Triggers / Actions / Integrations
```

原文：`Every Taskade Genesis app is composed of exactly 9 cells. 3 layers, 3 facets each. Same structure at every scale, from a personal todo to an 8,000-node enterprise system.`
https://www.taskade.com/about

另一处官方给的层级（JSON-LD Organization description）：`Each app has four layers: projects for data, AI agents, automations with 100+ integrations, and a generated app interface` —— 在 3 层之上多了一层「生成的 app 界面」。
https://www.taskade.com/

实体链（按官方文档拼接）：

```
Workspace（每个 workspace 有独立 DNA：projects+agents+automations）
  └─ Project（数据容器；1..9 视图；Custom Fields；可被 agent 当知识）
       └─ Task / Subtask / Note（列表项；可加 due date / assignee / 评论 / add-on）
  └─ AI Agent（指令 + Knowledge + Memory + Tools + Commands）
       └─ Tool（内置工具 / 复用某条 automation 作为自定义工具 / HTTP）
  └─ Automation（Trigger → 分支/循环/过滤 → Action → Integration）
       └─ 可作为 agent 的 tool；也可由 agent 决定触发
  └─ App（生成的界面层，引用上述 project/agent/automation）
       ├─ Publish → 自有 URL / 自定义域名 / iframe / 密码
       ├─ App Users（终端用户身份）
       └─ App Kit（可整包克隆/售卖，含 .tsk 导出）
Template = 一个 Project（可捆绑 agent/automation）的可复制快照
App Kit  = Project + Agent + Automation + App UI 的四件套封装
```

证据：https://www.taskade.com/about （3×3）；https://www.taskade.com/llms.txt （App Kit 定义）；https://www.taskade.com/learn/agents/agent-tools （automation 可作 agent tool）；https://www.taskade.com/learn/projects/connect-memory-to-agents （project 连给 agent）

---

## C. 原子能力清单（≥15 条）

类型沿用知识库受控词表：容器 / 动作 / 工具 / 知识 / 身份。
（`界面`、`智能`、`分发` 三个补充值标在备注里，因现有词表已用过这三个值。）

| # | 原子能力 | 类型 | 做什么 | 能和其他什么组合 | 证据 URL |
|---|---|---|---|---|---|
| 1 | Workspace | 容器 | 顶层隔离单元，每个 workspace 有独立 projects+agents+automations（官方：`Every workspace gets its own memory, intelligence, and execution`） | 成员/角色；多 workspace 做客户隔离（Free 仅 1 个） | https://www.taskade.com/pricing |
| 2 | Project（数据容器） | 容器 | 存结构化数据；可被 agent 当知识源；可被 automation 增删改 | 视图 / 字段 / agent 知识 / 模板 / automation | https://www.taskade.com/learn/projects/databases |
| 3 | Task / Subtask / Note | 容器 | 最小记录单元，带 due date、assignee、评论、提醒、附件 | 视图 / automation 触发器（Task Added/Completed/Assigned/Due）/ 字段 | https://www.taskade.com/learn/projects/tasks |
| 4 | View（9 种视图） | 界面（补充类型） | 同一份数据换 9 种呈现：List、Board、Table、Mind Map、Docs、Gantt、Calendar、Actionsheet、Org Chart | 数据模型 / 字段 / 分享 / 模板 | https://www.taskade.com/learn/projects/project-views |
| 5 | Custom Fields | 容器 | 给每个节点加带类型属性（enum/date/number…），官方称 100+ field types | 视图 / automation（`Custom Field Updated` 触发器）/ agent 读表 | https://www.taskade.com/learn/projects/custom-fields ；https://www.taskade.com/about |
| 6 | AI Agent | 身份 | 一个有角色的 AI 队友：指令 + 知识 + 记忆 + 工具 + slash 命令 | 项目 / 自动化 / 公共页 / AI Teams / MCP | https://www.taskade.com/learn/agents/custom-agents |
| 7 | Agent Commands / Slash Commands | 动作 | agent 的可调用能力清单（官方示例：summarize / categorize / generate） | 知识 / 工具 / 自动化步骤 | https://www.taskade.com/about ；https://www.taskade.com/learn/projects/slash-commands |
| 8 | Agent Knowledge | 知识 | 训练数据源：文件、项目、网页、YouTube、云盘；Free 1 个源，付费 50 个/agent | 工具 / 记忆 / 公共 agent | https://www.taskade.com/learn/agents/knowledge |
| 9 | Agent Tools（内置工具库） | 工具 | 6 组工具：Research（搜索/读页/摘要/YouTube 转写）、Documents（文件转文本/存 Media）、AI steps（Ask AI/Write/Categorize）、Workspace（建改项目任务字段评论/问其他 agent）、External apps（Slack/Gmail/Sheets/HubSpot/Stripe…18+）、Custom | 每个工具可设 Automatic / Manual Approval | https://www.taskade.com/learn/agents/agent-tools |
| 10 | Persistent Memory | 知识 | agent 记忆以 Project 形式存在，可浏览、编辑、搜索、fork | 任何 agent / EVE / 跨会话检索 | https://www.taskade.com/learn/agents/knowledge ；https://www.taskade.com/learn/genesis/eve-memory |
| 11 | AI Teams | 身份（编排） | 多 agent 同群：Auto（路由）/ Everyone（全问）/ Manual（点名）/ Orchestrate（规划） | 每个 agent 各自知识/工具；Pro+ 才开 | https://www.taskade.com/learn/agents/ai-teams |
| 12 | Taskade EVE（元 agent） | 身份 | 从一句提示词建 app / project / agent / 自动化，能列计划、问问题、跑工具、请求人工批准 | 全站 surface；持久记忆；slash 命令 | https://www.taskade.com/learn/agents/eve-assistant |
| 13 | Automation Trigger | 动作 | 四类触发：Taskade 内部（Task/Project/Comment/Field/Media）、外部 app（Gmail/Slack/GitHub/Notion…）、时间（Schedule）、入站（Webhook/Mailhook/Form）；另有 `Agent Tool`、`Agent Public Chat Ended` | 分支/循环/过滤 → 动作 → 集成 | https://www.taskade.com/learn/automation/triggers |
| 14 | Automation Action | 动作 | 五类动作：Workspace（建项目/加任务/指派/移动/更新字段）、AI（Ask AI/生成/摘要/问 agent/分类）、Web&Files（抓页/HTTP/搜索/转写/转文件）、Control Flow（Branch/Loop/Filter/Delay/Array Transform）、173 集成 | 可返回结构化 JSON 供后续步骤取字段 | https://www.taskade.com/learn/automation/actions ；https://www.taskade.com/llms.txt |
| 15 | 控制流（Branch/Loop/Filter/Wait/Approval） | 动作 | 分支路由、按条目循环、过滤、暂停等人审批、延时 | 任意 trigger 与 action 之间 | https://www.taskade.com/learn/automation/branch-action ；`/loop-action` ；`/approval-step` |
| 16 | Integration（173 个连接器） | 工具 | 6 类：AI Agents 8、Connectors 63、Automations 43、Knowledge 8、Migrate 36、Extend 15；多数双向（trigger 拉事件，action 推数据） | agent 工具 / 自动化步骤 / app 数据源 | https://www.taskade.com/integrations |
| 17 | Webhook / Mailhook（入站） | 动作 | 给外部一个私有地址，事件到了就触发流程；Pro+ 才可 webhook 触发 | 任意 action；HTTP Request 反向出站 | https://www.taskade.com/learn/automation/webhooks ；https://www.taskade.com/learn/automation/mailhook |
| 18 | Hosted MCP Server + MCP Client 连接器 | 工具/协议 | 外部 AI 客户端（Claude/Cursor/VS Code）读写你的 workspace；反向也能让自动化调用远端 MCP 工具 | 付费档全含；Action API v2 | https://www.taskade.com/mcp ；https://www.taskade.com/learn/connect/mcp-client |
| 19 | Media / 文件处理 | 工具 | 上传、图片生成、文件转文本、扫描件识别、YouTube 转写、存回 Media | agent 工具 / 自动化步骤 / app 上传入口 | https://www.taskade.com/learn/agents/media-tab ；https://www.taskade.com/learn/genesis/scanned-documents |
| 20 | Template（项目模板） | 容器（分发） | 一份可复制的 project 结构，可捆 agent 与自动化 | 任意 project；可分享、可定时套用 | https://www.taskade.com/learn/projects/use-templates |
| 21 | App Kit / .tsk 导出 | 分发（补充类型） | 把「app 界面 + projects + agents + automations」打成一包，别人一键克隆；Pro+ 可导出 .tsk 文件搬走 | 克隆 / 售卖 / GitHub 导出 | https://www.taskade.com/llms.txt ；https://www.taskade.com/learn/genesis/tsk-export |
| 22 | Publish + Custom Domain | 身份（发布） | app 拿到 `*.taskade.app` 或自有域名（含 SSL），可 iframe 嵌入、密码保护 | App Users / SEO Health / 版本历史 | https://www.taskade.com/learn/genesis/publishing ；`/custom-domains` |
| 23 | App Users / GenesisAuth | 身份 | 给已发布 app 加独立于 Taskade 账号的邮箱登录与用户管理（invite/suspend/remove） | 记录归属、门户、会员制 app；所有档都含 | https://www.taskade.com/learn/genesis/app-users ；`/genesis-auth` |
| 24 | App Secrets + 外呼代理 | 工具 | 把密钥存在客户端代码之外，经 Taskade 代理调外部 API | 任意 app / HTTP 步骤 | https://www.taskade.com/learn/genesis/app-secrets |
| 25 | TSK Model Ladder | 智能（补充类型） | 把模型选择抽象成任务档位：TSK-Auto / Instant / Standard / Thinking / Reasoning，模型换代用户无感 | EVE / agent / 自动化 AI 步骤 / 建 app 提示框 | https://www.taskade.com/learn/agents/thinking-modes ；https://www.taskade.com/learn/genesis/tsk-1 |
| 26 | BYOK（自带模型 key） | 工具 | 用自己的 OpenAI/Anthropic/Google（Business+ 加 xAI/DeepSeek/Mistral/OpenRouter）跑 agent 与自动化 AI 步骤 | 降低 credits 消耗；超量只收小额 step fee | https://www.taskade.com/learn/connect/byok-ai-integration |
| 27 | Custom Agent Tool（拿自动化当工具） | 动作 | 把任意一条 automation 注册成 agent 的一个工具，无限扩展工具面 | agent / AI Teams / 公共 agent（可限制访客可用工具） | https://www.taskade.com/learn/agents/agent-tools |
| 28 | Community Profile / Creator 页 | 身份 | 发布者自己的主页，聚合其 App Kits；可售卖并结算 | App Kit / 付费克隆 / Earnings | https://www.taskade.com/apps/creators ；https://www.taskade.com/learn/account/community-profiles |
| 29 | Import（30+ 工具迁移） | 动作 | 从 Notion/Trello/Asana/Monday/ClickUp/Todoist/Obsidian/Evernote/Roam/Logseq/Workflowy/Miro… 一键导入，保留层级 | 导入即成为 project，可挂 agent/自动化 | https://www.taskade.com/learn/import |

> 关于「笔记 / 思维导图」：2026 版站点上 **Docs 与 Mind Map 是 project 的两种视图**，不是独立对象。官方原文 `All project views · 1 data model`（100+ field types）。历史页面名（to-do list / mind map）仍留在应用商店名与旧 blog 里。
> https://www.taskade.com/about ；https://www.taskade.com/learn/projects/project-views

---

## D. 已封装的工作流（官方成品组合）

### D1 App Kit（App Factory 里可直接克隆的成品，官方给出精确配方）

| # | 名称 | 输入 | 用了哪些原子 | 输出 | URL |
|---|---|---|---|---|---|
| 1 | Invoice Generator Pro | 16 张示例发票 / 8 个客户 / 10 条付款条件；新发票产生 | 3 Projects + 1 Agent（Billing Assistant）+ 3 Automations（Invoice Archive、Morning chase email、Invoice Generation Flow） | 每张逾期发票一段催款草稿；按逾期天数分组的欠款视图；按客户的对账单（已付/未结/逾期/合计） | https://www.taskade.com/apps/all/invoice-generator-pro-xya5kq1dkmwji5il |
| 2 | Simple Store Manager Pro | 新订单事件 | 2 Projects + 1 Agent（Store Assistant）+ 4 Automations（New Order Notification、Client Status Sync、Daily chase email + 1） | 周报（对比上周）、按周营收、逾期订单追讨清单 | https://www.taskade.com/apps/all/simple-store-manager-pro-ppofwm5t450i4cmh |
| 3 | Neon CRM Dashboard Pro | 每次通话/邮件/会议记录 | 2 Projects + 1 Agent（Client Coach）+ 3 Automations（Weekly client export by email、New Client Onboarding、Morning client follow-ups） | 每个客户的互动时间线、带截止日的下一步、每日呼叫清单 | https://www.taskade.com/apps/all/neon-crm-dashboard-pro-h8wjwd7pgzidhxmb |
| 4 | Project Portal Pro | 项目进度、文件、客户消息 | 3 Projects + 1 Agent（Portal Assistant）+ 3 Automations（Weekly Client Update Reminder、Project Milestone Tracker、File Upload Notification） | 客户可登录的门户；一键发出每周书面更新 | https://www.taskade.com/apps/all/project-portal-pro-l4hnpvbdossel5j2 |
| 5 | Maintenance Tracker Dashboard Pro | 资产清单 + 到期日 + 工单完成事件 | 3 Projects + 1 Agent（Maintenance Assistant）+ 2 Automations（Daily Maintenance Digest、Service Completion Logger） | 资产到期看板、成本报表（30/90/180 天）、每日摘要 | https://www.taskade.com/apps/all/maintenance-tracker-dashboard-pro-rumr8ncn2iwy9dt7 |

> 结构规律（抽这 5 个 App Kit 得出的可数事实）：都是 `2–3 个 Project + 1 个 Agent + 2–4 条 Automation + 1 个生成界面`。同一 app 有 **free 版与 Pro 版两个条目**（Pro 版克隆需付费档），Pro 版之间用「加一列报表 / 加一条追款自动化」做差异。
> 例：`Invoice Generator Pro is a Pro kit… Invoice Generator is the free edition from the same creator.`

### D2 官方在 About 页给出的「一次表单提交触发全 9 格」的完整链路（唯一带完整推理链的官方样例）

输入：用户在 app 里提交表单
1. Webhook 收到 32 个带类型字段，表单 schema 直接映射 Custom Fields　→ Triggers + Custom Fields
2. Agent 用内嵌评分细则（作为 knowledge）跑 `categorize` 命令打分分类　→ Commands + Knowledge + Tools
3. 建入库记录（结构化列表项）　→ Lists
4. 同一节点在表视图里成为一行（看板/报表）　→ Tables
5. HTTP 返回结构化 JSON（score / status / reason）给调用方　→ Actions + Integrations

原文结论：`9 / 9 cells active. Complete Taskade Genesis app.`
https://www.taskade.com/about

### D3 官方给的跨工具工作流样例（llms.txt FAQ 原文）

`New email in Gmail → AI agent classifies intent → Routes urgent to Slack DM → Creates task in Taskade → Updates HubSpot contact`
用到的原子：Gmail trigger + Agent(action) + Slack action + Add Task + HubSpot action
https://www.taskade.com/llms.txt

### D4 官方按场景写成的「成品配方」文档（每篇即一条可复现工作流）

| 名称 | 输入 | 原子 | 输出 | URL |
|---|---|---|---|---|
| Help Desk 带 AI 工单分类 | 客户来信/表单 | AI Forms / Gmail trigger + Agent 分类 + 建 task + 回信 | 分好类的工单队列 | https://www.taskade.com/learn/genesis/help-desk |
| 审批流 + 每日提醒 | 一个待批请求 | Form/Webhook + Approval step + Delay + 通知集成 | 被批准/驳回并留痕的请求 | https://www.taskade.com/learn/genesis/approval-workflow |
| SOP 库（员工逐条确认） | SOP 文档 | Project + Custom Fields + App Users | 可勾选确认的 SOP 台账 | https://www.taskade.com/learn/genesis/sop-library |
| 文档录入（扫描件/照片 OCR） | 扫描件、照片 | 文件上传 + 文件转文本 + Agent 抽字段 + 建记录 | 结构化记录 | https://www.taskade.com/learn/genesis/document-intake |
| 发票与收据自动化 | 发票邮件/文件 | Mailhook / 上传 + AI 抽取 + 建记录 + 存档 | 台账 + 提醒 | https://www.taskade.com/learn/genesis/invoice-automation |
| 客户门户 | 项目数据 + 客户身份 | App + App Users + 自定义域名 + agent | 客户自助门户 | https://www.taskade.com/learn/genesis/build-customer-portal |
| 内部工具 | 业务规则 | App + Projects + Agent + Automation | 内部可用的工具 | https://www.taskade.com/learn/genesis/build-internal-tool |
| 带条件逻辑的表单 | 用户填写 | Form + Branch/Filter + 建记录 + 通知 | 按条件分流的表单 | https://www.taskade.com/learn/genesis/build-form-with-logic |
| Vibe Workflow（用话描述业务流程生成自动化） | 一段流程描述 | EVE + Automation 生成器 | 可运行的 flow | https://www.taskade.com/learn/genesis/vibe-workflows |
| 预约/排课 | 客户选时段 | Booking 模板 + Calendar 集成 + App Users | 可预订的 app | https://www.taskade.com/learn/genesis/booking-system |

### D5 模板侧的成品（示例，全部可 `Use Template`）

- AI Sales Agent Studio（销售模板分类下，含预训练 agent）https://www.taskade.com/templates/sales/ai-sales-agent-studio
- Taskade Featured Kits Collection（一个模板捆绑 folders + projects + AI agents + automations，一步装进工作区）https://www.taskade.com/templates/featured/taskade-kits-collection
- 模板官方定义即「结构 + 预训练 agent + 自动化流 + 示例内容」四件套 https://www.taskade.com/templates

---

## E. 资源清单（可复用资产）

### E1 总表

| 资源名 | 类型 | 解决什么问题 | 怎么拿到 | URL |
|---|---|---|---|---|
| 项目模板库 | 模板 | 不想从空白页开始，要一套现成结构 | `Use Template` 复制进工作区；可改可再分享 | https://www.taskade.com/templates |
| Agent 模板库 | Agent | 不想从零调教 agent，要现成角色 | 选用/克隆；可改指令与知识 | https://www.taskade.com/agents |
| 自动化配方库 | 自动化配方 | 不知道某个集成能干什么，要现成 trigger→action | 套用后改连接器与字段 | https://www.taskade.com/automate |
| App Factory（App Kits） | 应用/成品 | 要一个能跑的 app，含数据+agent+自动化 | 打开即看 DNA，一键克隆（免费或付费 kit） | https://www.taskade.com/apps |
| 集成目录 | 集成 | 要把已有 SaaS 接进来 | 在自动化里加步骤 / 给 agent 开工具 | https://www.taskade.com/integrations |
| 提示词库（站点级） | 提示词 | 不知道该怎么写提示词 | 直接复制 | https://www.taskade.com/llms.txt （Prompt Library 各篇）；sitemap 实测 2,205 页 |
| 免费生成器 | 工具页 | 要一次性产出（排课表、考题、HTML、脚本、命名） | 网页即用 | https://www.taskade.com/generate （4,526 页） |
| 免费转换器 | 工具页 | 把 PDF / YouTube / 手写笔记 / 网页转成结构化产物 | 网页即用 | https://www.taskade.com/convert （2,118 页） |
| Wiki | 知识库 | 想搞懂 agent/自动化/生产力体系的概念 | 公开阅读 | https://www.taskade.com/wiki （573 篇） |
| Learn 帮助中心 | 文档 | 操作怎么做 | 公开阅读，支持 `.md` 与 `llms.txt` | https://www.taskade.com/learn （435 篇） |
| 开发者文档 + OpenAPI | 接口规范 | 要写集成/自动化 | 公开；REST v1 GA、Action v2 Beta | https://www.taskade.com/docs ；`/api/documentation/v1/json` |
| MCP Server（托管） | 协议/接口 | 让 Claude/Cursor/VS Code 直接操作工作区 | OAuth 2.0 或 PAT 接入 | https://www.taskade.com/mcp |
| SKILL.md | 协议/文档 | 让 agent 知道怎么用 Taskade | 一条 prompt 让 agent 自读 | https://www.taskade.com/SKILL.md |
| Agent skills 索引 | 协议/索引 | 批量安装技能 | `npx skills add https://www.taskade.com` | https://www.taskade.com/.well-known/agent-skills/index.json |
| 开源仓库 | SDK/工具 | 自建/本地 MCP、CLI、技能包 | GitHub 公开 | https://github.com/taskade （mcp / skills / cli / awesome-vibe-coding） |
| TSK-Bench 数据集 | 模型/基准 | 比较模型在真实 build 任务上的表现 | 公开 JSON | https://www.taskade.com/tsk/tsk1.json |
| 品牌素材包 | 资产 | 做内容/媒体用 | 免费下载 | https://www.taskade.com/press |
| 导入器（30+） | 工具 | 从竞品搬数据 | 一键导入 | https://www.taskade.com/learn/import |
| 客户端 | 应用 | 桌面/手机/浏览器扩展 | 下载 | https://www.taskade.com/downloads |
| 创作者收益体系 | 分发 | 把自己的 app 变成可售 App Kit | Publish → Let others clone → Free/Paid | https://www.taskade.com/learn/genesis/sell-app-kits |

### E2 模板库：分类与数量（实测）

- sitemap 实测：`sitemap-templates.xml` = **3,997 条 URL**，去重后 **87 个分类段**（另有 `/templates`、`/templates/categories` 两个一级页）。
- 官网口径：`Browse the Taskade template library across 87 categories`；但 `/templates/categories` 页只渲染 15 个分类链接（JSON-LD `numberOfItems: 15`）。
- 数量最多的 10 个分类（sitemap 反推）：content 129、to-do-list 121、sales 102、standard-operating-procedure 100、budgets 95、marketing 94、e-commerce 92、meetings 86、table 85、task-management 85。
- 分类页单页展示量不等：`Featured Templates 30 ITEMS`、`ChatGPT Templates 58 ITEMS`（agents 侧为 30/43/43/49/43/82），说明是「分类页 + 分页」而非一次性全量。
- URL 结构：`/templates/<category>/<template-slug>`；分类索引 `/templates/categories`。
https://www.taskade.com/templates/categories ；https://www.taskade.com/sitemaps/sitemap-templates.xml

### E3 Agent 模板 / 自动化配方 / App Kit 的数量与分类（实测）

| 资源 | sitemap 实测页数 | sitemap 一级段（含非分类页） | 分类（官方页列出的 9 类） | URL |
|---|---|---|---|---|
| Agent 模板 | **3,169** | 67 | Featured、Project Management、Productivity、Marketing、Translator、Content、Workflow、Research、Personal | https://www.taskade.com/agents |
| 自动化配方 | **2,361** | 106 | Featured、AI Agent Automation、AI Workflow Automation、Logic、Trigger、Agentic Process、Action、AI Models、Agentic Automation | https://www.taskade.com/automate |
| App Kits | **6,135** | 72（官方 JSON-LD `numberOfItems: 72`） | 48 类型 + 12 团队 + 12 行业（见 A3） | https://www.taskade.com/apps/categories |
| 提示词页 | 2,205 | — | — | https://www.taskade.com/sitemaps/sitemap-prompts.xml |
| 生成器页 | 4,526 | 93 | — | https://www.taskade.com/generate |
| 转换器页 | 2,118 | 56 | — | https://www.taskade.com/convert |

官方对 App Kit 规模的两种说法（并存，口径不同）：
- 定价页 Free 档：`Clone 1,000+ free app kits`（免费 kit 数）
- 定价页/JSON-LD Free offer：`500+ community templates`
- sitemap 实测社区 app 详情页 **6,135** 条
https://www.taskade.com/pricing ；https://www.taskade.com/sitemaps/community-apps.xml

### E4 集成清单（173 个，6 类）

| 类别 | 数量 | 代表连接器 | 作用 |
|---|---|---|---|
| Connectors | 63 | Slack、Discord、Microsoft Teams、WhatsApp Business、GitHub、Stripe、Notion、HubSpot、Gmail、Salesforce、Jira、Linear、Airtable、Telegram… | 双向：trigger 拉事件，action 推数据 |
| Automations | 43 | AI Forms、Task Added、Webhooks、Schedule… | 流程内建触发与步骤 |
| Migrate | 36 | Notion、Asana、ClickUp、Trello、Monday、Zapier、Make、Pabbly… | 迁移与桥接 |
| Extend | 15 | Chrome、Firefox、Edge、Brave、桌面、嵌入、Developer API、MCP | 把 Taskade 推进别的工具里 |
| AI Agents | 8 | Ask Agent Team、Ask Agent with Structured Output、Add Knowledge to Agent、Search Web Action… | 给 agent 加能力 |
| Knowledge | 8 | PDF、DOCX、XLSX、CSV… | 给 agent 喂原始文档 |

原文：`173 integrations across 6 categories`
https://www.taskade.com/integrations

连接器粒度示例（官方标注的「有用动作」）：
- Stripe Checkout Sessions —— 从自动化生成 checkout URL，app 内收款不用写服务端 https://www.taskade.com/integrations/stripe
- GitHub Export to Existing Repo —— 把 app 推进已有仓库、开 PR、保留既有文件 https://www.taskade.com/integrations/github
- Google Calendar Events & Free/Busy —— 排期类 app 的基础 https://www.taskade.com/integrations/google-calendar
- Salesforce / Notion 的增删改查与「新页面出现」触发 https://www.taskade.com/integrations/salesforce ；https://www.taskade.com/integrations/notion-automation
- 没有连接器时的三条兜底：入站 webhook、出站 HTTP、MCP https://www.taskade.com/integrations

---

## F. 流量曝光渠道

### F1 SEO：URL 模式与实测页数（这是最大的一块）

`sitemap.xml` 索引 17 个子 sitemap，实测合计 **28,602 条 URL**：

| 子 sitemap | 条数 | URL 模式 | 说明 |
|---|---|---|---|
| community-apps.xml | **6,135** | `/apps/all/<slug>-<id>`、`/app/<slug>-<id>` | 社区 App Kit 详情页（UGC 目录） |
| generate.xml | **4,526** | `/generate/<category>/<slug>` | 免费 AI 生成器页（程序化），一级段 93 |
| templates.xml | **3,997** | `/templates/<category>/<slug>` | 模板页（程序化），分类段 87 |
| agents.xml | **3,169** | `/agents/<category>/<slug>` | Agent 模板页（程序化），一级段 67 |
| automate.xml | **2,361** | `/automate/<category>/<slug>` | 自动化配方页，一级段 106 |
| prompts.xml | 2,205 | 提示词页 | 程序化 |
| convert.xml | 2,118 | `/convert/<category>/<slug>` | 免费转换器页，一级段 56 |
| blog.xml | 1,125 | `/blog/<slug>` | 长文博客 |
| marketing.xml | 867 | 各类落地页 | 含 `/ai/*`、`/apps/*`、`/wiki` 等 |
| wiki.xml | 573 | `/wiki/<slug>` | 概念型词条（打「什么是 X」类搜索） |
| community-profiles.xml | 495 | 创作者主页 | UGC |
| learn.xml | 435 | `/learn/<section>/<article>` | 帮助中心 |
| compare.xml | 197 | `/compare/<slug>` | 对比页 |
| integrations.xml | 180 | `/integrations/<name>` | 每个连接器一页 |
| docs.xml | 169 | `/docs/<section>` | 开发者文档 |
| ai.xml | 43 | `/ai/<topic>` | AI 能力落地页 |
| community.xml | 7 | — | — |

> 「一级段」= sitemap 里该路径下第一级目录去重数，会把分类页与非分类页（如 `/templates/categories`）算进去，所以可能大于官方宣称的分类数；templates 的 87 是去重后的纯分类数，与文案一致。

https://www.taskade.com/sitemap.xml

三个值得记录的 SEO 特征：

1. **对比页里混了大量与自身无关的「模型 vs 模型」页**。`/compare` 实测 197 条，按 slug 拆：`free-<竞品>-alternative` **155 页**、`taskade-vs-*` **6 页**、纯第三方 `X vs Y` **33 页**、其余 2 页（`taskade-alternatives`、`outline`）。第三方那 33 页是 `gpt-vs-claude`、`gemini-vs-deepseek`、`glm-vs-gpt`、`qwen-vs-kimi`、`opus-vs-sonnet`、`gpt-6-1-sol-vs-claude-opus-5-5`、`mistral-vs-llama` 这类，与 Taskade 产品无关，只吃「X vs Y」的搜索量。
   https://www.taskade.com/compare
2. **`free-<竞品>-alternative` 是一个统一的页面模板 × 150+ 竞品名**，包括 `free-slack-alternative`、`free-notion-alternative`、`free-asana-alternative`、`free-clickup-alternative`、`free-lovable-alternative`、`free-zapier-alternative`。
   https://www.taskade.com/compare
3. **博客走超长文**。2026-11 的首页文章标注阅读时长 55–104 分钟（如 `Best AI Homework Helpers in 2026` 102 min、`AI Quiz Generators` 104 min），标题多为「Best N 个 X」清单式，且配历史图片（如 1949 年 NACA 人工计算员照片、1818 年 Bodoni 字样书），明显是给搜索与 AI 摘要吃的资料型内容。
   https://www.taskade.com/blog

### F2 面向 AI 的「被发现」层（GEO）

这一层是常规 SaaS 里少见的，官方把它做成了导航分组「For agents」：

- `https://www.taskade.com/llms.txt` —— 官方自称「Canonical AI-facing summary and index」，带 TL;DR 引文块、Quick Facts、FAQ、How to Cite 段落（Last-Updated: 2026-11-18）
- `https://www.taskade.com/SKILL.md` —— 一份给 AI agent 的操作说明；首页有「Copy setup prompt: Set up Taskade for me. Read and follow https://www.taskade.com/SKILL.md」
- `https://www.taskade.com/mcp` —— 托管 MCP endpoint，Claude / Cursor / VS Code 可直接接入（首页并列四个客户端的安装入口）
- 任意页面 `Accept: text/markdown` 返回 Markdown（本底稿即用此法采集）；`/docs`、`/learn`、`/wiki`、`/blog` 另有 `.md` 副本
- `.well-known` 全套：`agent-skills/index.json`、`mcp.json`、`mcp/server-card.json`、`api-catalog`、`oauth-protected-resource/mcp`
- `llms-full.txt` 官方说明「redirects here. There is one canonical file, not two」
- 每个已发布 app 自动带 `robots.txt`、`sitemap.xml`、`llms.txt`：`Every indexable app serves robots.txt, sitemap.xml, and llms.txt automatically.`

https://www.taskade.com/llms.txt

### F3 产品自带的病毒/分发结构

| 机制 | 官方原文/事实 | URL |
|---|---|---|
| 克隆即用 | Free 档 `Clone 1,000+ free app kits`；每个克隆计入 Free 的 3 个 app 额度 | https://www.taskade.com/pricing |
| 免费版/付费版成对 | 同一 app 出 free 与 Pro 两个条目，Pro 克隆需付费档 | https://www.taskade.com/apps/all/invoice-generator-pro-xya5kq1dkmwji5il |
| 卖 App Kit 抽成体系 | `Let others clone` 设为 Free 或 Paid；只有原创 app 可售；收益从 Earnings 提 | https://www.taskade.com/learn/genesis/sell-app-kits |
| 克隆给 credit | `Earn Credits When Others Clone` | https://www.taskade.com/learn/account/clone-creator-credits |
| 邀请给 credit | `Earn AI Credits by Inviting Friends`；Free 无月度 credits，只能靠邀请/分享赚 | https://www.taskade.com/learn/account/referrals |
| 创作者主页 | `Community Profiles: Publish Apps, Own Your Page`（sitemap 495 个） | https://www.taskade.com/learn/account/community-profiles |
| 公共 agent 页 + 嵌入 | 每个公开 agent 一个 `https://www.taskade.com/a/{name}-{id}` 页，可 iframe / 5 种 widget 嵌到外部网站 | https://www.taskade.com/llms.txt |
| 已发布 app 自带发现层 | 每个 app 自动产出 robots/sitemap/llms.txt；Business+ 有 SEO Health 评分与 app analytics | https://www.taskade.com/llms.txt |
| 合作伙伴/联盟 | `Earn From Your App Kits`、`partnerships` | https://www.taskade.com/learn/account/partnerships |

### F4 口碑/第三方阵地（有出处）

- `Capterra 4.7 · 67 reviews`；`Product Hunt 4.7 · 108 reviews`；`Trustpilot 4.6 · 745 reviews`（官方自述 last checked 2026-08-11 / 2026-09-12）
  https://www.taskade.com/reviews ；https://www.taskade.com/llms.txt
- JSON-LD award：`Product Hunt #1 Product of the Day`、`G2 High Performer`
  https://www.taskade.com/about
- 官方列出的媒体报道：TechCrunch、PC Mag、CNET、Fast Company、Forbes、LifeHacker、TechRepublic、Cloudwards、Digital Project Manager、Small Business Trends（自称 46 篇）
  https://www.taskade.com/press
- 官方自有社媒矩阵（JSON-LD sameAs）：X、LinkedIn、YouTube、GitHub、Reddit r/taskade、Instagram、TikTok、Product Hunt、G2、Capterra、Trustpilot、Crunchbase、GitLab、Linktree
  https://www.taskade.com/about

### F5 增长史（公开可查里程碑，全部带来源）

| 时间 | 事件 | 来源 |
|---|---|---|
| 2017 | 成立，创始 John Xie（CEO）、Dionis Loire、Stan Chang（CTO）；总部旧金山 | https://www.taskade.com/about |
| 2019 | 入选 Y Combinator S19 | https://www.ycombinator.com/companies/taskade |
| 2019-10-24 | TechCrunch：`YC grad Taskade raises $5M to take on Notion with a more collaborative productivity platform` | https://techcrunch.com/2019/10/24/yc-grad-taskade-raises-5m-to-take-on-notion-with-a-more-collaborative-productivity-platform/ |
| 2022-12-12 | Taskade AI 上线：`AI becomes contextually aware of projects and tasks. The journey to Genesis begins.` | https://www.taskade.com/about |
| 2023 | 18+ 个 AI 版本：AI Agents、Custom AI Agents (GPTs)、AI Agents Roundtable（多 agent） | https://www.taskade.com/about |
| 2024 | Workspace DNA（Memory/Intelligence/Execution）成型；Automation v2 durable execution；Agent Teams；Knowledge Manager | https://www.taskade.com/about |
| 2025 | Genesis 发布 + Platform V6（Aurora 设计系统）：一句提示词生成 app | https://www.taskade.com/about |
| 2026 | 平台化：API、MCP v2、100+ 集成、agent 发布、Telegram 自动化；官方称 `80 releases in 5 months` | https://www.taskade.com/about |
| 2026（现状） | 官方公布：`150,000+ Taskade Genesis apps built`、`500K+ AI agents deployed`、`3M+ automation executions` | https://www.taskade.com/press |

规模旁证：`numberOfEmployees 10–50`（JSON-LD）；员工规模与 6,135 个社区 app、28,602 个 URL 的产出量形成明显反差。
https://www.taskade.com/about

### F6 判断：主要靠什么被看见

**[推断]** 主引擎是 **程序化 SEO + 免费工具页 + UGC 目录**，而不是投放或社区口碑；第二引擎是 **面向 AI 助手的 GEO 层**。

依据：
1. 结构比例（实测相加 = 28,602，与总表一致）：程序化资源页 **18,376 页（64.2%）** = templates 3,997 + generate 4,526 + agents 3,169 + automate 2,361 + convert 2,118 + prompts 2,205；UGC 社区 app **6,135 页（21.4%）**；其余全部营销/文档内容（blog 1,125 + marketing 867 + wiki 573 + community profiles 495 + learn 435 + compare 197 + integrations 180 + docs 169 + ai 43 + community 7）合计 **4,091 页（14.3%）**。手写页面是少数。
2. 帮助中心只有 435 篇，而 `/generate` 有 4,526 页——明显是「一个模板 × N 个关键词」的机器生成结构（每页一个 category 段、每页最多 30 条）。
3. `/compare` 197 页里 33 页是纯第三方模型对比（`gpt-vs-claude`、`qwen-vs-kimi`），与产品无关，只可能出于吃搜索量。
4. 免费档设计成「必须邀请/分享才能拿到 credits」（`Free has no monthly credits`），而免费档又能克隆 1,000+ kit —— 增长靠用户自传播而非广告。
5. 导航里专设「For agents」并维护 llms.txt / SKILL.md / MCP / `.well-known` 全套，说明意图是在 AI 回答里被引用（官方 llms.txt 直接给出「How to Cite Taskade」话术）。
6. 无任何官方投放/联盟佣金比例的公开证据；affiliate 只有创作者售卖 App Kit 这一种（未核验佣金比例）。

**[推断]** 转化路径设计为「免费工具页/模板页 → 免登录试用 → 克隆 app → 撞到 Free 的 3 app / 1 agent / 10 runs 限制 → 升级」；限制点（3 apps、1 agent、10 automation runs、250MB、2 人）都在定价页被明码标出，属于主动设卡。

---

## G. 事实缺口（不要编）

1. **月付价**：官方只说年付省 50%，并明示 Pro 月付 $20。Starter / Business / Max / Enterprise 的月付挂牌价未在页面文本中出现（只有年付折算价），标未核验。
2. **真实自然搜索流量 / 关键词数**：无 SimilarWeb/Ahrefs 类第三方数据可引，未核验。本文只能给页数，不能给流量。
3. **用户数 / 付费用户数 / ARR**：官方只给 `150,000+ apps built`、`500K+ AI agents deployed`、`3M+ automation executions` 三个累计量，未给用户数、付费转化率与营收；这三个数字的统计口径与截止日期也未写明（press 页仅标 © 2017-2026）。
4. **融资总额**：只查到 2019 年 TechCrunch 报道的单轮 $5M；之后是否有新融资，官网 About 只列投资机构 logo（Y Combinator、Grishin Robotics、Fellows Fund、Altair Capital、TRAC VC、ZVC）与天使名单，无金额与轮次。
5. **模板分类数口径**：官方文案称 87 分类、sitemap 实测也是 87 个分类段（可交叉验证），但 `/templates/categories` 页只渲染 15 个分类链接、JSON-LD 也写 `numberOfItems: 15`。剩余 72 个分类只有落地页、没有进索引页（推测靠 SPA 内部分页），为什么不在索引页露出，未核验。
6. **App 数量口径冲突**：免费档文案 `1,000+ free app kits`、JSON-LD `500+ community templates`、sitemap 实测 6,135 个社区 app 页。可能分别是「免费 kit 数 / 模板数 / 全部 app 页数」，但官方没有一处把三者对齐。
7. **Product Hunt 首次发布的时间与 upvote 数**：只拿到 `#1 Product of the Day` 与 108 条评论，具体 launch 页与日期未核验。
8. **G2 评分与评论数**：About 的 JSON-LD 只写 `G2 High Performer`，未给分数；本次未抓 G2 页面，未核验。
9. **`second brain`**：首页已不提；该说法只存在于帮助文档 `/learn/genesis/second-brain`，且是「把 Taskade 当第二大脑」的用法页，不是产品主张。历史定位词（to-do list / mind map）只保留在应用商店名与旧 blog 里。
10. **`Genes`/`Genesis` 的命名拆分**：官方现在一律用 `Taskade Genesis`（AI app builder）+ `Taskade EVE`（元 agent）+ `TSK-1`（System Kernel）。任务描述里的「genesis」对应的是 `/create?mode=genesis` 与 `learn/genesis/*`，没有独立域名页。
11. **团队规模与产出量的因果**：10–50 人如何维护 28,602 个页面与 6,135 个 app，官方未说明是否有 UGC/外包/自动生成分工，未核验。
12. **访客侧 app 的收费能力边界**：官方说 app 对访客免费、Stripe 可收款，但 app 交易抽成/手续费未提及，未核验。
