# Taskade 深度调研（014）

> 日期：2026-11-26 ｜ 事实来源：官方 `llms.txt`（2026-11-18 更新）、`SKILL.md`、官网/定价/导航、官方 sitemap 实测
> 本文回答三件事：**① 它是为谁解决什么 ② 它的 AI 是怎么用原子能力拼出来的 ③ 它靠什么被看见**。
> 结尾给「我们能拿走的 5 条」与「事实缺口」。

---

## 0. 一句话判断

**Taskade 不是任务工具，是一台「把业务流程一句话变成可运行 app」的机器：Projects 存数据、Agents 做判断、Automations 跑执行、Genesis App 当界面——官方把这套叫 Workspace DNA。**

三句补充：
1. 它的组合逻辑不是"功能列表"，而是**四层同构**：同一个对象图，用「项目 / agent / 自动化 / app」四种方式封装。所以它既能卖模板，也能卖 agent，也能卖 app。
2. 它的分发结构是三合一的：**程序化 SEO（≈3.2 万页）+ UGC 克隆工厂（6,135 个 app + 495 个作者页）+ AI 原生发现层（llms.txt / SKILL.md / MCP / .well-known）**。
3. 它把「成品」做成了可流通资产：App Kit 可克隆、可售卖、可导出 `.tsk`、可导出 GitHub——**模板生意的终局是资产市场**。

---

## A. 定位：为谁、解决什么、哪些场景

### A1. 官方定义（原文）

- "Taskade is an AI-native workspace. **Taskade Genesis turns one prompt into a live, hosted app.** Each app runs on **Workspace DNA**: Projects hold the data, AI agents add intelligence, and automations act across 100+ integrations."（https://www.taskade.com/llms.txt）
- "The user is usually a **business owner, not a developer**."（https://www.taskade.com/SKILL.md）
- 公司：TASKCADE INC.，2017 年成立，Y Combinator S19，旧金山。（llms.txt "How to Cite Taskade"）

### A1.5. 它怎么给自己定位（About 页，直接拿 Slack 做类比）

- 原文大意：**2014 年人撞墙了，Slack 给了「持久房间 + 真工具 + 不重置的记忆」；2026 年 agent 需要同样的东西。**
- 它把 Slack / Notion / Asana / Linear 统一归为 **"Human workspaces — agents are bolted on"**（人的工作区，agent 是外挂的），自己定位成 **"Agentic workspaces"**（agent 原生的工作区）。
- 官方给的产品结构是 **3 层 × 3 面 = 9 格**：
  - Projects：Lists / Tables / Fields
  - Agents：Commands / Knowledge / Tools
  - Workflows：Triggers / Actions / Integrations
  （About 页有一次表单提交打满这 9 格的完整链路，是全站唯一带完整推理链的官方样例）
- **注意**：2026 版站点上「笔记 / 思维导图」是 project 的两种**视图**，不是独立对象（`02-atoms.csv` 已按此修正）。

### A2. 客户分层与定价（llms.txt 官方口径）

| 档位 | 年付折算月价 | 关键额度（官方矩阵） |
|---|---|---|
| **Free** | $0，永久 | 2 成员、**3 个 Live app**、1 agent、**10 次自动化/月**、250MB、1 个知识源；**无月度 credits**（只能靠邀请/克隆赚） |
| **Starter** | **$6** | 3 成员、10K credits/月、350 次自动化/月、3 个 agent、5GB、去水印、Hosted MCP |
| **Pro** | **$10**（月付 $20） | 10 成员、50K credits、1,000 次自动化、无限 agent、10 个自定义域名、webhook、`.tsk`/GitHub 导出、BYOK（OpenAI/Anthropic/Google） |
| **Business** | **$25** | 无限成员、150K credits、10K 次自动化、无限域名、品牌色/SEO、agent 白标、SAML、TSK-Reasoning |
| **Max** | **$100** | 无限成员、400K credits、同 Business 上限 |
| **Enterprise** | **$250** | 无限成员、1.1M credits、SAML + SCIM |

- 年付对 Pro/Business/Max/Enterprise **省 50%**（月付价 = 年付折算价 × 2，Pro 月付 $20 有官方原文）。
- 无学生/教育/非营利折扣（官方明确）。
- 计费逻辑：**订阅 + credits**（构建与 AI 工作消耗）；Free 无月度 credits，靠邀请/克隆赚——**用"送 credits"换拉新**。

### A3. 场景清单（官方口径）

- llms.txt 明列可建：CRM、客户门户、仪表盘、发票流程、预约 app、追踪器、知识库、聊天机器人、落地页、店铺、表单、计算器。
- **App Factory 有 72 个分类**（48 类型 + 12 团队 + 12 行业，每类标注 app 数量）——这是它承载"场景"的真实结构（`/apps/categories`）。
- 模板库按角色/流程/行业分；自动化模板按集成分。

> 注意：`/use-cases`、`/solutions` 这类目录页在 2026 版站点**不存在（404）**，场景全部由 `/apps/categories` 的 72 类 app kits 与 `/learn/projects/for-*` 人群页承载。

---

## B. 信息架构：真的点得到的东西

### B1. 五个 surface

| Surface | 职责 | 证据 |
|---|---|---|
| **Projects** | 结构化数据（任务树 + 自定义字段 + 10 种视图） | https://www.taskade.com/templates |
| **AI Agents** | 有指令、知识、持久记忆、工具、命令的 agent | https://www.taskade.com/agents |
| **Automations** | 触发器 + 动作 + 分支/循环/过滤 + 100+ 集成 | https://www.taskade.com/automate |
| **Genesis App** | 一句话生成、由 Taskade 托管的 React app（读写上面三层） | https://www.taskade.com/create |
| **App Kits / App Factory** | 成品 app 的可克隆/可售卖市场（含作者页） | https://www.taskade.com/apps |

### B2. 实体关系（官方 URL 形状即证据）

```
Workspace (/spaces/{spaceId})
├── Project (/d/{projectId})
│     ├── Task（行）
│     └── Field（列：Text/Number/Date/Select…）
│     └── View（List/Board/Table/MindMap/Docs/Calendar/Gantt/Actionsheet/OrgChart）
├── Agent (/agent/{agentId})
│     ├── Instructions
│     ├── Knowledge（文件/项目/网页/YouTube/云盘，付费档 50 个）
│     ├── Persistent Memory（存成 Project，可浏览可编辑）
│     └── Tools（内置 + 自定义 + Skills 按需加载）
├── Automation (/flows/{flowId})
├── App（Genesis，读写以上三者）
└── App Kit（/app/{slug}-{id}?action=clone）
```

**关键设计**：**agent 的记忆不是黑盒，而是「存成一个 Project」**——可浏览、可编辑、可搜索、可 fork。这是它把「AI 记忆」变成「工作区数据」的核心一招。

---

## C. AI 是怎么拼出来的（核心）

### C1. 官方架构：Workspace DNA + Living Loop

| 层 | 组件 | 角色 |
|---|---|---|
| **Memory（记忆）** | Projects | 结构化数据库，存储并记住上下文 |
| **Intelligence（智能）** | AI Agents | 基于知识与工具做判断 |
| **Execution（执行）** | Automations | 触发 → 动作，跨 100+ 集成 |
| **Interface（界面）** | Genesis App | 读写以上三层的 React 界面 |

**Living Loop（官方原话）**：Memory 提供上下文 → Intelligence 做决定 → Execution 产出结果 → **结果回流成新的 Memory**。
（https://www.taskade.com/llms.txt "What Is Workspace DNA?"）

### C2. 原子能力：从 18 条里收敛成 8 个基元

| 基元 | 类型 | 一句话 | 能拼成什么 |
|---|---|---|---|
| Project / Task / Field | 数据 | 行 + 列 + 视图 | 任何业务数据表 |
| View | 界面 | 同一数据的多种看法 | 看板/日历/甘特/导图 |
| AI Agent | 身份 | 指令 + 知识 + 记忆 + 工具 | 任何岗位助手 |
| Agent Tool / Skill | 工具 | agent 可调的动作 | 让 agent 会"动手" |
| Knowledge Source | 知识 | 文件/项目/网页/视频 | 让 agent 懂业务 |
| Automation Trigger/Action | 编排 | 事件 → 动作（分支/循环/过滤） | 任何重复流程 |
| Genesis App | 容器 | 一句话生成的界面 | 把三层包成产品 |
| App Kit | 分发 | 可克隆/可售卖的成品 | 资产市场 |

### C3. 拼接公式

> **数据（Project/Task/Field）× 智能（Agent：指令+知识+工具+记忆）× 执行（Automation）× 界面（Genesis App）= 一个 Living App**

四种入口，同一个对象图：

| 入口 | 建什么 | 谁用 |
|---|---|---|
| **Projects** | 任务/文档/数据 | 人直接操作 |
| **AI Agents** | 能判断的助手 | 人问、自动化调 |
| **Automations** | 会自己跑的流程 | 系统触发 |
| **Genesis App** | 一句话生成的整包产品 | 终端客户 |

### C4. 三个"封装层"（这是最值得抄的）

| 封装 | 机制 | 意义 |
|---|---|---|
| **Template** | 预填好数据/流程的实例（3,997 项目模板 / 3,169 agent / 2,361 自动化） | 从「空白页」变成「改一改」 |
| **App Kit** | 把 app + 项目 + agent + 自动化打包，可克隆、可免费/付费分发、可导出 `.tsk`、可导出 GitHub | **成品变成可流通资产**；创作者可赚钱 |
| **MCP / SKILL.md** | 外部 agent 通过 MCP 读写工作区；SKILL.md 教它怎么用 | 产品变成「别的 agent 的一个工具」 |

### C5. 智能层：TSK 模型阶梯（不绑单模型）

TSK-Auto（默认，按任务选模型）/ TSK-Instant / TSK-Standard / TSK-Thinking / TSK-Reasoning；Pro+ 可 BYOK（OpenAI/Anthropic/Google，Business 再加 xAI/DeepSeek/Mistral 等）。
**意义**：模型是耗材，产品是"任务到模型的路由"。这是 2026 年 AI 产品该有的抽象。

---

## D. 流量曝光：它靠什么被看见（全部可数）

### D1. 程序化 SEO：17 个 sitemap，**28,602** 条 URL（逐个实测）

| 页面类型 | URL 数 | 说明 |
|---|---|---|
| templates | 3,997 | 项目模板 |
| generate | 4,526 | 「生成 X」工具页 |
| agents | 3,169 | Agent 模板 |
| automate | 2,361 | 自动化配方 |
| prompts | 2,205 | 提示词 |
| convert | 2,118 | 「X 转 Y」 |
| **community apps** | **6,135** | 用户可克隆作品（UGC） |
| blog | 1,125 | 内容 |
| marketing | 867 | 营销页 |
| wiki / learn / docs | 573 / 435 / 169 | 教学与帮助 |
| community profiles | 495 | 作者主页（UGC） |
| compare | 197 | 对比页（结构见下） |
| integrations | 180 | 集成页 |
| ai | 43 | AI 能力页 |
| community（首页） | 7 | — |
| **合计** | **28,602** | 来源：https://www.taskade.com/sitemap.xml 及 17 个子 sitemap |

**结构占比（这是关键，不是总量）**：
- **程序化资源页 18,376 页 = 64.2%**（templates/agents/automate/prompts/convert/generate）
- **UGC app 页 6,135 页 = 21.4%**（community apps + profiles）
- **手写营销内容只占 14.3%**（blog/marketing/learn/wiki/docs/compare 等）

**对比页的真相（197 页拆开看）**：
- **155 页是 `free-<竞品>-alternative`**（如 free-notion-alternative、free-zapier-alternative）
- **33 页是纯第三方模型对比**（gpt-vs-claude、qwen-vs-kimi、glm-vs-gpt 这类，与 Taskade 产品无关）
- **只有 6 页是 `taskade-vs-*`**
→ 这不是"品牌对比"，是**纯吃搜索量**的结构：用户搜"免费 XX 替代品"和"XX vs YY"，它都有页接住。

### D2. AI 原生发现层（GEO）——这是它最超前的一层

| 动作 | 具体做法 | 证据 |
|---|---|---|
| 给 AI 的站点说明书 | `llms.txt`（2026-11-18 更新），含 TL;DR、事实、FAQ、**How to Cite Taskade（指定引用措辞）** | https://www.taskade.com/llms.txt |
| 给 Agent 的操作手册 | `SKILL.md`（连接方式、工具清单、安全规则） | https://www.taskade.com/SKILL.md |
| 可调用入口 | Hosted MCP `https://www.taskade.com/mcp`（OAuth 2.0 + PKCE） | 同上 |
| 机器可读元数据 | `.well-known`：api-catalog、mcp.json、mcp/server-card.json、agent-skills/index.json、oauth-protected-resource | llms.txt 末段 |
| 任意页面变 Markdown | 请求头 `Accept: text/markdown` | llms.txt |
| 规范与基准 | OpenAPI JSON（v1/v2）、TSK-Bench 数据集 | llms.txt |
| robots 态度 | `ai-train=yes, search=yes, ai-input=yes`（Content-Signal 声明） | https://www.taskade.com/robots.txt |

**判断（[推断]）**：Taskade 把「被 AI 引用」当成一条正式渠道在做——不只写内容，而是**把机器可读接口做全 + 直接告诉 AI 该怎么引用它**。这是 2026 年 GEO 的完整范式。

### D3. UGC 克隆工厂：用户作品变成内容资产

- 6,135 个社区 app 页 + 495 个作者页进 sitemap（`/apps/all/<slug>`、`/@<id>`）
- App Kit 可免费/付费分发，创作者能拿到收益（Earnings）
- **用户发布的每个 app 自动带 robots.txt / sitemap.xml / llms.txt**（官方 Publish 说明）
→ 每个客户的应用都是一个新的搜索/AI 发现节点。

### D4. 其他渠道

| 渠道 | 证据 |
|---|---|
| 免费档楔子 | Free 永久免费（2 成员/3 app/1 agent/10 次自动化） |
| 对比页矩阵 | 197 条 compare（工作区/自动化/app builder 三类对手） |
| 内容/教学 | blog 1,125 + learn 435 + wiki 573 |
| 开源与开发者 | GitHub：MCP server、skills、CLI、Awesome Vibe Coding |
| 评价资产 | Capterra 4.7/5（67）、Product Hunt 4.7（108）、Trustpilot 4.6（745）（2026-08/09 核对） |
| 增长史 | 2017 成立（旧金山，10–50 人）、YC S19、2019-10 TechCrunch 报道 $5M、2022 Taskade AI、2024 Workspace DNA 成型、2025 Genesis + Platform V6、2026 「80 releases in 5 months」；官方累计量：150,000+ apps built / 500K+ agents / 3M+ executions |

### D3.5. 产品自带的分发闭环（比"免费档"更细的一层）

| 机制 | 官方做法 | 作用 |
|---|---|---|
| **克隆给 credits** | "Earn Credits When Others Clone" | 让作品被复制 = 作者得奖励 |
| **邀请给 credits** | Free 无月度 credits，只能靠邀请/分享赚 | 把"额度"变成拉新货币 |
| **克隆即用** | Free 可克隆 1,000+ free app kits；每次克隆占 Free 的 3 个 app 额度 | 用户一上手就在"用别人的成品"，同时撞额度 |
| **免费/付费成对** | 同一 app 出 free 与 Pro 两个条目 | 用免费版获客、Pro 版变现 |
| **卖 App Kit 抽成** | 原创 app 可设 Paid，创作者提现 | 把创作者变成渠道 |
| **公共 agent 页 + 嵌入** | 每个公开 agent 一个页 + 5 种 widget | 用户把 AI 挂到自己网站，反向带流量 |
| **已发布 app 自带发现层** | 每个 app 自动 robots/sitemap/llms.txt | 用户作品成为发现节点 |

**判断（[推断]）**：这是一套"**用额度做货币、用克隆做传播、用成品做商品**"的闭环——比单纯免费档更狠。

---

## E. 资源清单（它内置了哪些可复用资产）

| 层 | 资源 | 数量/入口 | 解决什么问题 |
|---|---|---|---|
| **抄** | 项目模板 | 3,997（/templates） | 业务场景从哪开始 |
| **抄** | Agent 模板 | 3,169（/agents） | 想直接要一个能干的助手 |
| **抄** | 自动化模板 | 2,361（/automate） | 重复流程怎么配 |
| **抄** | 提示词库 | 2,205（/prompts） | 不会写指令 |
| **抄** | 生成/转换工具页 | 4,526 + 2,118 | 直接产出结构 |
| **拿** | 社区 App（可克隆） | 6,135（/apps） | 要一个现成 app |
| **拿** | 作者主页 | 495（/@id） | 追某个创作者的作品 |
| **拿** | App Kit（免费/付费） | /apps/{category}、clone 链接 | 成品直接买/克隆 |
| **接** | 集成 | **173 个（6 类，实测）/ 官方口径 100+** | 接外部系统 |
| **接** | MCP / API / webhook | hosted MCP、REST v1、Action v2 | 外部 agent/系统调用 |
| **学** | 帮助中心 | 400+ 篇（/learn） | 操作问题 |
| **学** | SKILL.md / llms.txt | 单文件 | 给 agent 看的产品说明 |

**资源的组织逻辑**：按「**抄 → 拿 → 接 → 学**」排；「抄」的体量最大（模板/agent/自动化/提示词），「拿」是可流通资产。

---

## F. 我们能拿走的 5 条（判断，不是事实）

1. **用「四层」定义产品，而不是用「功能」定义。** Workspace DNA（数据/智能/执行/界面）是一套可直接借用的分层：任何 AI 产品都可以先问「我的 Memory / Intelligence / Execution / Interface 分别是什么」。
2. **Living Loop 是复利结构**：执行结果回流成数据 → 数据让下一次判断更准。做知识库/agent 产品时，**必须设计「结果如何写回记忆」**，否则每用一次都从零开始。
3. **模板的终局是资产市场。** Template → App Kit（可克隆/可售卖/可导出）→ 创作者分成。这比"卖模板"高一层：你在建一个可以流通的资产层。
4. **GEO 不是写文章，是把机器可读接口做全。** llms.txt（含引用指南）+ SKILL.md + `.well-known` + MCP + OpenAPI + Markdown 出口——Taskade 把这套做成了标准动作。我们的产品至少要补 `llms.txt` + `SKILL.md` + 一个 MCP 入口。
5. **让用户的产出自动带 SEO/GEO。** 用户发布 app 自动获得 robots/sitemap/llms.txt——UGC 直接变成发现节点。我们做任何"用户作品"类产品，都应该把这一层默认打开。

---

## G. 与 Slack 的路线对比（013 vs 014）

| 维度 | Slack | Taskade |
|---|---|---|
| 本质 | **协议层**：标准化身份/权限/事件/消息 | **模板层**：同一数据模型 × 四种封装 |
| 生态方式 | 市场目录（2,600+ apps）让别人接进来 | App Kit / 克隆（6,135）让成品流出去 |
| AI 架构 | 双向 MCP + Skills（agent 的家） | Workspace DNA + Living Loop（agent 是四层之一） |
| SEO | 本地化大站（13 语种 × 1,769）+ 目录 + 帮助 | 程序化矩阵（≈32,600）+ UGC + GEO |
| 定价分水岭 | Slackbot 额度 | credits + 付费档功能门 |
| 共同点 | 都把「模板/技能」当作封装；都在把 AI 做成"平台的一部分"而不是"一个按钮" | |

---

## H. 事实缺口（不编）

| 缺口 | 状态 |
|---|---|
| MAU/付费用户/ARR | 未披露。官方只有三个累计量（press 页）：**150,000+ Genesis apps built、500K+ AI agents deployed、3M+ automation executions**（未写统计截止日） |
| 网站月流量/自然搜索占比 | 未取 Similarweb/Ahrefs；sitemap 只能证明页面规模（28,602），不能证明流量 |
| App 数量口径 | **三个口径并存**：1,000+ free kits / 500+ community templates / sitemap 6,135——官方未对齐 |
| 各档月付挂牌价 | 官方只说「年付省 50%」；除 Pro $20（llms.txt 明示）外，其余档月付价未核验 |
| 融资 | 只查到 2019-10-24 TechCrunch 单轮 $5M，之后无公开金额 |
| 6,135 个社区 app 的活跃度/质量分布 | 未核验 |

---

## 来源

主底稿：`_kb/raw/taskade-raw.md`（研究员版；本文以官方 llms.txt / SKILL.md 为主）。
关键来源：https://www.taskade.com/llms.txt（2026-11-18）、https://www.taskade.com/SKILL.md、/pricing、/agents、/templates、/automate、/apps、/mcp、/robots.txt、https://www.taskade.com/sitemap.xml 及 17 个子 sitemap（2026-11-26 实测计数）。

---

## 报告

- 中文：`014-taskade/teardown-zh.html`
- 英文：`014-taskade/teardown-en.html`（补齐中）
