# Slack 调研底稿（2026-11-26）

> 采集方式：web_fetch / 直连抓取官方页 + 官方 sitemap 计数。中文转述为主，关键句保留英文原文。
> 纪律：每条事实带 URL；抓不到或不确认的写「未核验」。本文不做评价、不写启发。
> 已知失效来源：ProductHunt（Cloudflare 拦截，`013-slack/_raw.md` 中该段不可用）。

---

## A. 定位（为谁 / 解决什么 / 哪些场景）

### A1. 官方一句话主张

| 位置 | 原文 | URL |
|---|---|---|
| 首页 H1 | "All your people and AI agents working together" | https://slack.com/ |
| 首页副标 | "Slack connects your team. Slackbot multiplies what they can do." | https://slack.com/ |
| 中文站副标 | "Slack 联结团队。Slackbot 倍增团队实力。" | https://slack.com/intl/zh-cn/ |
| 平台页 H1 | "The platform agents and AI call home." + "It's the scalable, secure infrastructure purpose-built for adding agents & AI to every business." | https://slack.com/features/agentic-platform |
| Solutions 页 H1 | "Where work happens." / "All the business solutions you need, all in one work OS." | https://slack.com/solutions |
| 企业页 H1 | "Reimagine work for your entire enterprise." / "Slack is reimagining work through radical productivity, bringing people and AI together to help businesses grow." | https://slack.com/enterprise |
| Slackbot 页 H1 | "Slackbot, your AI Teammate for the whole team in Slack" | https://slack.com/features/slackbot |

官方自我定位的措辞演化（同一批页面内并存）：聊天工具 → 协作平台（"work OS"）→ Agent 的运行底座（"platform agents and AI call home"）。第三方定义："cloud-based team communication platform… owned by Salesforce since 2021… freemium model… primarily offered as a business-to-business service"（https://en.wikipedia.org/wiki/Slack_(software)）。

### A2. 客户分层：每一层卖什么

| 档位 | 价格（官方页原文） | 卖的核心 | URL |
|---|---|---|---|
| Free | $0 USD，free forever | 90 天消息历史；最多 10 个 app；1:1 huddles；1:1 外部 DM；Basic AI（摘要/Slackbot 试用/AI 工作流生成/AI 搜索/每日回顾/文件摘要） | https://slack.com/pricing |
| Pro | $8.75 /user/mo 月付（促销 $4.38，3 个月 5 折）；年付 $7.25 | 无限历史、无限 app、群组 huddles、群组外部协作（"up to 250 orgs"）、Basic AI | 同上 |
| Business+ | $18 /user/mo 月付（促销 $9）；年付 $15 | 在 Pro 之上：Slackbot 持续可用、进阶管理/合规（多工作区、细分角色、信息屏障、法定保留、Discovery API、HIPAA 支持等） | 同上 |
| Enterprise+ | $45 /user/mo 年付，"Contact Sales" | "Enterprise-Grade AI"：Slackbot 无周消息上限、Enterprise search、企业级合规、多 SAML | 同上 |

补充口径：
- Slackbot 分档限制（官方 FAQ 原文）："Slack Free and Pro users will have the chance to explore Slackbot's capabilities firsthand through a limited trial experience. Ongoing Slackbot access will continue to be available to Business+ and Enterprise+ customers"（https://slack.com/pricing）。超额可买 "Flex Credits through Salesforce"（同页 FAQ）。
- 模板分档（中文定价页对照表）：Free/Pro "由用户创建"、Business+ 同样是用户创建、Enterprise+ "由管理员创建"（https://slack.com/intl/zh-cn/pricing）。
- Workflow Builder 是付费功能："Workflow Builder is a paid feature included in the Slack Pro, Business+ and Enterprise subscriptions."（https://slack.com/features/workflow-automation）
- 单档独立落地页（SEO 用）：/pricing/free、/pricing/pro、/pricing/businessplus、/pricing/paid-vs-free（sitemap 实测存在）。
- 非营利/教育有折扣（https://slack.com/pricing FAQ）。
- 一线员工（Frontline）为附加组件（https://slack.com/enterprise/frontline）。

### A3. 场景清单（官方 Solutions 全量，来自导航 + sitemap）

按部门（9）：Frontline（/enterprise/frontline）、Engineering（/solutions/engineering）、IT（/solutions/information-technology）、Customer Service（/solutions/customer-service）、Sales（/solutions/sales）、Project Management（/solutions/project-management）、Marketing（/solutions/marketing）、Human Resources（/solutions/human-resources）、Security（/solutions/security）。

按行业（9）：Manufacturing, Auto & Energy（/solutions/manufacturing）、Technology（/solutions/technology）、Media（/solutions/media）、Small Business（/solutions/small-business）、Financial Services（/solutions/financial-services）、Retail（/solutions/retail）、Public Sector（/solutions/public-sector）、Education（/solutions/distance-learning）、Health & Life Sciences（/solutions/healthcare）。

按 use case（11，导航原文）：Manage Projects（/solutions/use-cases/efficient-project-management）、Client Collaboration（collaborating-with-external-partners）、Run Effective Meetings（running-effective-meetings）、Pipeline Management（manage-sales-pipeline）、Internal Communications（improve-internal-communication）、Project Tracking（project-tracking）、Lead Management（manage-leads）、Team Productivity（boost-team-productivity）、Employee Onboarding（onboard-new-employees）、Time Tracking（time-tracking）、Find Answers Faster（find-company-knowledge-faster）。
注：`https://slack.com/solutions/use-cases` 这个 hub URL 本身返回 404，use case 只以子页形式存在（实测）。

sitemap 里另有 4 个不在导航的场景页：/solutions/govslack、/solutions/remote-work、/solutions/task-management、/solutions/frontline/demo（来源：https://slack.com/sitemaps/sitemap_en-us.xml）。

### A4. 官方对外引用的规模数字（营销口径，脚注来源已抄录）

| 数字 | 内容 | 脚注来源 |
|---|---|---|
| 94% | 用户获得正 ROI | Salesforce 内部（slack.com/intl/zh-cn/） |
| 312% | 三年 ROI | 2026 年 Forrester 总体经济影响研究（同上） |
| $5,100 万 | 协作带来的收益 | 同上 |
| 10 亿+ | 每日已发送消息数 | 2026 财年财报发言（同上） |
| 400 万 | Slack Connect 用户每周与外部团队协作 | 2025 财年 Slack 内部数据（同上） |
| 300 万 | 每日工作流数 | 同上 |
| 170 万 | 每周活跃使用的应用数 | 同上 |
| 5 小时 | 使用 Slackbot 每周平均节省时间 | Salesforce 内部（同上） |
| 35% | 用户因自动化额外节省的时间 | 2024 财年客户成功指标（同上） |
| 97 分钟 | 使用 AI 每周可节省时间 | Slack AI 功能试点内部分析（https://slack.com/features/ai） |
| 2,600+ | Marketplace 应用数 | 全站导航 "Browse over 2,600 apps"（https://slack.com/integrations） |
| 290+ | 在 G2 市场报告中领先的报告数 | G2 2026 年秋季市场报告（slack.com/intl/zh-cn/） |

---

## B. 信息架构与表层（surface）

### B1. Surface 清单与一句话职责

| Surface | 一句话职责（官方措辞转述） | URL |
|---|---|---|
| Channels | "flexible, transparent spaces for working together"，按主题聚合人、文件、应用、自动化，可无限创建 | https://slack.com/features/channels |
| Slack Connect | 把外部组织（客户/供应商/代理商）拉进同一批频道与 DM，"moving conversations out of siloed email threads" | https://slack.com/connect |
| Huddles（抱团） | 频道内即时音视频 + 共享屏幕；结束后 AI 自动出笔记、待办、谁说了什么 | https://slack.com/features/huddles |
| Canvas（画板） | 频道/私聊里的文档面，可嵌文件、图片、视频、应用链接，可加工作流，AI 代写 | https://slack.com/features/canvas |
| Lists（列表） | 会话内的任务/项目表，"capture and structure the most important parts of your conversations"，可被工作流读写 | https://slack.com/features/task-list |
| Clips（剪辑） | 音视频录制与剪辑（导航项，独立页 /features/clips 存在） | https://slack.com/features/clips |
| Slackbot | 个人 AI agent："I already know how your business works… I don't just answer questions, I work with every app and agent connected to Slack"，按席位固定成本、不按 token 计费 | https://slack.com/features/slackbot |
| Slack Code / code channels | @ 一个 agent 即开一个 code channel，人 + 队友 + agent 在频道里共同改代码/看 diff | https://slack.com/features/code-channels |
| Native AI（Slack AI） | 频道/线程摘要、每日回顾、AI 搜索、翻译、文件摘要、huddle 笔记、Today 简报（Early Access） | https://slack.com/features/ai |
| Agentforce | Salesforce 的企业 agent 进入 Slack，可 @ 提及，在频道/DM/thread 里执行动作 | https://slack.com/ai-agents |
| Slack CRM | 会话式 CRM：Slackbot 建客户、记通话、推进交易，官方亦称 "Native CRM" | https://slack.com/crm ；https://slack.com/features/crm |
| Enterprise Search | 一个搜索框搜 Slack + 已连接第三方应用 + 自定义数据源（API 接入），权限感知 | https://slack.com/features/enterprise-search |
| Workflow Builder | 无代码/低代码自动化：AI 生成工作流、条件分支、70+ 连接器、可嵌进消息/画布/频道书签 | https://slack.com/features/workflow-automation |
| Slack Marketplace | 2,600+ 应用的目录，含编辑集合与 MCP Registry | https://slack.com/marketplace |
| Slack Atlas | 组织架构/人员目录（源自 2020 收购 Rimeto，2021-06 上线，见 G） | https://slack.com/features/atlas |
| Slackforce Surfaces | 把 Salesforce/外部数据做成频道内可交互视图，"Turn data into action" | https://slack.com/ （新功能区） |
| Work objects（工作对象） | 应用数据在 Slack 内完整交互嵌入，而非仅预览 | https://slack.com/ （新功能区）；https://slack.com/integrations |

### B2. 关键实体与关联

| 实体 | 定义/归属 | 与其他实体的关系 | 证据 |
|---|---|---|---|
| Workspace / Org | 计费与管理的最小单位 | Free/Pro/Business+ 限 1 个工作区，Enterprise+ 无限 | https://slack.com/intl/zh-cn/pricing |
| Channel | 内容与协作的容器 | 内含 message、file、canvas、list、workflow、app、agent；可升级为 Slack Connect 频道 | https://slack.com/features/channels |
| Thread | 消息的从属层级 | 挂在 message 下；AI 可做 thread 摘要 | https://slack.com/features/ai |
| Canvas | 频道内文档 | 可挂 workflow、可被 Slackbot skills 当作指令载体（"with a canvas you own"） | https://docs.slack.dev/ai/slackbot-skills |
| List | 频道内结构化记录集 | 可被 MCP 服务器增删改查（CRUD），可被工作流自动化 | https://docs.slack.dev/ai/slack-mcp-server |
| Workflow | 触发器 + 步骤 + 条件 | 步骤可为「发消息」「调连接器」「生成 AI 回复」「启动 agent 对话」 | https://slack.com/features/workflow-automation |
| App | 第三方/自建集成 | 由 Marketplace 分发；由管理员审批（app approvals）；通过 OAuth scopes 授权 | https://docs.slack.dev/ai/slack-mcp-server |
| Agent | 可被 @ 的成员级实体 | 在 channel/DM/thread 内被 @；可经 Slackbot MCP Client 接入 | https://slack.com/ai-agents |
| Skill（Slackbot skill） | 指令包（markdown 或 canvas） | 创建 → 更新 → 组织级发布 → 加入成员库，四步 | https://docs.slack.dev/ai/slackbot-skills |
| MCP server / client | 双向接口 | Slack MCP server（外部 AI → Slack）；Slackbot MCP client（Slack → 你的 server） | https://docs.slack.dev/ai/slack-mcp-server ；https://docs.slack.dev/ai/slackbot-mcp-client |
| Template | 预配置的 channel+canvas+list+workflow 组合 | "made up of pre-configured channels, canvases, lists, and workflows" | https://slack.com/solutions |

---

## C. 原子能力清单

| # | 原子能力 | 类型 | 做什么 | 能和其他什么组合 | 证据 URL |
|---|---|---|---|---|---|
| 1 | Channel（频道） | 容器 | 按主题的公开/私密空间，聚合消息、文件、应用、AI | Connect 频道、Canvas、Lists、Workflow、Agent @ | https://slack.com/features/channels |
| 2 | Message / Thread | 容器 | 对话最小单元与从属线程 | 被 AI 摘要/搜索/recap 读取；可触发工作流 | https://slack.com/features/ai |
| 3 | Huddle | 动作+容器 | 频道内音视频、共享屏幕；会后自动出笔记与 action items | AI 笔记 → Canvas / List；Clips | https://slack.com/features/huddles |
| 4 | Canvas | 知识容器 | 可协作文档，嵌文件/图片/视频/应用链接，可放工作流 | Slackbot skills 指令载体、频道 FAQ、项目简报 | https://slack.com/features/canvas |
| 5 | List | 容器（结构化数据） | 会话内任务/项目表，可分配、跟踪、自动化 | 工作流读写、MCP CRUD、Slackbot 更新记录 | https://slack.com/features/task-list |
| 6 | Clip | 动作 | 录制/剪辑音视频异步沟通 | 频道、Canvas 嵌入 | https://slack.com/features/clips |
| 7 | Slack Connect | 身份/边界 | 与外部组织共享频道与 DM（Pro 以上至多 250 orgs） | 外部伙伴 starter kit、审批工作流 | https://slack.com/connect |
| 8 | Workflow Builder | 编排 | 触发器 → 步骤 → 条件分支（"up to 15 conditions"），70+ 应用连接器 | AI 步骤、agent 对话步骤、自定义代码步骤 | https://slack.com/features/workflow-automation |
| 9 | AI 工作流生成 | 动作（生成器） | "tell AI what you need and it'll build a workflow for you" | Workflow Builder、模板 | https://slack.com/features/workflow-automation |
| 10 | Generate AI response（AI 步骤） | 动作 | 工作流中插入一步「按 Slack 上下文生成回答」 | 条件分支、连接器 | https://slack.com/features/workflow-automation |
| 11 | 自定义工作流步骤 | 动作（开发者） | 自己写 step 供全公司无代码复用 | Bolt / Deno SDK、CLI | https://docs.slack.dev （samples: custom step for Workflow Builder） |
| 12 | Slackbot | 工具/Agent | 跨应用执行：调研、建工作流、建 dashboard/报表/投票/计算器、更新记录、起草内容 | MCP client、Skills、Slack CRM、语音输入 | https://slack.com/features/slackbot |
| 13 | Slackbot Skills | 知识/封装 | 用 markdown 或 canvas 写指令 → 变成全队一键可跑的能力 | 组织级发布（admin.slackbot.skills.publish） | https://docs.slack.dev/ai/slackbot-skills |
| 14 | Slack Code / code channel | 容器+动作 | 频道内人 + agent 共同读写代码、看 diff/提交 | @agent、Canvas（文档）、GitHub Action | https://slack.com/features/code-channels |
| 15 | Slack CRM | 工具（业务对象） | 会话式 CRM：建客户、记录、推进交易，接 Salesforce | Slackbot、Lists、Salesforce 同步 | https://slack.com/crm |
| 16 | Enterprise Search | 检索 | 搜 Slack + 已连接应用 + 自建系统（Custom Sources API），权限感知 | Slackbot、AI 问答、agent 上下文 | https://slack.com/features/enterprise-search |
| 17 | Slack AI 原生能力 | 动作 | 频道/线程摘要、每日回顾、AI 搜索、翻译、文件摘要、huddle 笔记、Today 简报 | 频道、Canvas、搜索、Huddle | https://slack.com/features/ai |
| 18 | App / Integration | 工具 | 2,600+ 应用把外部系统搬进会话（Jira/Figma/Salesforce/Docusign…） | unfurl、work object、workflow 步骤 | https://slack.com/integrations |
| 19 | Work objects | 数据/界面 | 应用数据在 Slack 内完整交互嵌入，不止预览 | Canvas、频道、CRM | https://slack.com/features/agentic-platform |
| 20 | Block Kit / Work objects（UI 构件） | 界面构件 | 开发者拼装消息与界面的积木（46 个 block elements、22 个 blocks 文档页） | Bolt、Web API | https://docs.slack.dev/block-kit/ |
| 21 | Slack MCP Server | 接口 | 让外部 AI（Claude/Cursor/Codex…）搜消息文件、读频道线程、发/定时/草稿消息、管 Canvas 与 Lists、传文件、列频道 | 任意 MCP client；管理员审批 | https://docs.slack.dev/ai/slack-mcp-server |
| 22 | Slackbot MCP Client | 接口 | 反向：Slack 连你自己的远程 MCP server，Slackbot 自动发现并调用其工具（4 种鉴权：无鉴权/Slack 身份/DCR/手动 OAuth） | Slackbot、Slack app | https://docs.slack.dev/ai/slackbot-mcp-client |
| 23 | Real-Time Search API（原 Data Access API） | 接口 | 以用户权限实时检索、不落地数据，供 LLM 作上下文 | AI 应用、agent、enterprise search | https://docs.slack.dev/apis/web-api/real-time-search-api |
| 24 | Web API / Events / Scopes | 接口 | 359 个 Web API 方法页、121 个事件页、129 个 scope 页 | 一切 app 与 agent | https://docs.slack.dev/sitemap.xml |
| 25 | 权限与治理 | 身份/合规 | SSO（OAuth/SAML/多 SAML）、SCIM、EMM、DLP、EKM、信息屏障、法定保留、Discovery API、审核日志、app approvals | 所有 surface；按档位开关 | https://slack.com/intl/zh-cn/pricing ；https://slack.com/trust |
| 26 | Template | 知识/封装 | 预配置 channel + canvas + list + workflow 的整套骨架 | 可存进公司模板库复用 | https://slack.com/templates |
| 27 | Slack Atlas | 身份目录 | 组织架构与人员画像（可选功能） | 频道成员、搜索、入职模板 | https://slack.com/features/atlas |
| 28 | Agentforce agent | Agent | Salesforce 侧企业 agent，在频道/DM/thread 被 @ 后自主执行 | Slackbot、CRM、workflow | https://slack.com/ai-agents |
| 29 | Slackforce Surfaces | 容器（数据视图） | 把数据变成频道内可交互的「surface」 | Salesforce 数据、Slackbot | https://slack.com/intl/zh-cn/ |
| 30 | 开发者工具链 | 工具 | Slack CLI（90 个命令页）、Bolt（JS/Python/Java）、Deno Slack SDK、GitHub Action、app manifest | 全部上述能力 | https://docs.slack.dev ；https://docs.slack.dev/tools/slack-cli/reference/commands/ |

---

## D. 已封装的工作流（官方成品组合）

官方对模板的定义即「原子组合」："Get a head start on work with out-of-the-box business solutions for every team and function, made up of pre-configured channels, canvases, lists, and workflows."（https://slack.com/solutions）

| # | 名称 | 输入 | 用了哪些原子 | 输出 | URL |
|---|---|---|---|---|---|
| 1 | Project Management starter kit | 一个要启动的项目 | Channel + Canvas + List + Workflow | 项目频道骨架（含任务表与简报画布） | https://slack.com/templates/project-management-starter-kit |
| 2 | Feedback intake & triage | 外部/内部反馈 | 表单/消息触发 + List + 条件工作流 + 频道 | 分派并跟踪的反馈队列 | https://slack.com/templates/feedback-intake-triage |
| 3 | New hire onboarding | 新员工 | Onboarding checklist Canvas + List + Workflow + 频道 | 入职清单与提醒流 | https://slack.com/templates/new-hire-onboarding |
| 4 | Marketing campaign starter kit | 一次 campaign | Channel + Canvas（brief）+ List（deliverables）+ Workflow | 活动作战室 | https://slack.com/templates/marketing-campaign-starter-kit |
| 5 | Bug tracker / Issue log | 缺陷报告 | 频道 + List + 工作流（triage/分派） | 缺陷台账 | https://slack.com/templates/bug-tracker |
| 6 | External partner starter kit | 外部伙伴组织 | Slack Connect + Channel + Canvas | 跨组织协作空间 | https://slack.com/templates/external-partner-starter-kit |
| 7 | Sales deal tracking | 商机 | List + Slackbot/CRM 更新记录 + 频道 | 交易管道视图 | https://slack.com/templates/sales-deal-tracking |
| 8 | Help / service request process | 员工请求 | 表单 + Workflow 条件分支 + List | 服务请求工单流 | https://slack.com/templates/gallery （Featured: Service Request Form Template → /templates/help-requests-process） |
| 9 | 1:1 coaching | 一对一沟通 | Canvas（议程/记录）+ 频道 + 提醒工作流 | 1:1 记录与跟进 | https://slack.com/templates/1-1-coaching |
| 10 | Incident summary | 事故 | Canvas + List + 频道 + 复盘工作流 | 事故报告与行动项 | https://slack.com/templates/incident-summary |
| 11 | OKR | 季度目标 | Canvas + List + 频道 | OKR 跟踪板 | https://slack.com/templates/objective-key-results |
| 12 | Weekly sync agenda | 周会 | Canvas 议程 + 工作流提醒 + Huddle | 周会记录 | https://slack.com/templates/weekly-sync-agenda |
| 13 | Slack Agent Templates（onboarding / support / customer insights） | 一个业务主题 | Agent + 数据连接 + guided setup | 可部署的定制 agent | https://slack.com/ai-agents |
| 14 | Slackbot Skill（把团队最佳实践变技能） | 一段说明或一个 canvas | Slackbot + Skills + 组织发布 | 全队一键可跑的技能 | https://docs.slack.dev/ai/slackbot-skills |
| 15 | Slackbot 现场产物（dashboard / 报表 / 投票 / 计算器 / 模拟） | 一句自然语言请求 | Slackbot + 已连接应用数据 + Canvas/频道固定视图 | 频道内可排序/筛选/固定的实时视图 | https://slack.com/features/slackbot |
| 16 | Code channel 协作流 | @ 一个 coding agent | Code channel + agent + 队友 + diff 视图 | 频道内的代码评审与提交 | https://slack.com/features/code-channels |
| 17 | 条件分支审批/派单 | 一条请求 | Workflow 触发器 + 最多 15 个条件 + 连接器 | 自动路由与审批 | https://slack.com/features/workflow-automation |

补充：模板合集还有按职能的 starter kit（brand-guidelines-hub、event-prep-starter-kit、sales-enablement-hub、quarterly-plan、resources-guide 等，见 sitemap /templates/*）。

---

## E. 资源清单（可复用资产）

| 资源名 | 类型 | 解决什么问题 | 怎么拿到 | URL |
|---|---|---|---|---|
| Slack Marketplace 应用目录 | 应用市场 | 把外部系统接进会话 | 直接浏览/安装；按 23 个分类与 9 个合集筛选 | https://slack.com/marketplace |
| Marketplace 编辑合集（Featured / New & Noteworthy / Brilliant Bots / Essential Apps / Enterprise-Ready Apps / Slack Code Apps / MCP Registry / Daily Tools / Working from Home 等） | 榜单/推荐 | 降低挑选成本，官方按场景/新上架/企业就绪等维度排序 | 目录首页与分类页 | https://slack.com/marketplace （页面内嵌 JSON 的分类与合集数据） |
| Marketplace 专题合集（9 个 collection URL） | 榜单/推荐 | 按生态打包（Office 365、Google Workspace、Atlassian、Salesforce、外部协作、远程办公、快捷键、工作流、workflow automation） | 直接访问 | https://slack.com/marketplace/collection/office365-for-slack 等（完整清单见 sitemap_marketplace_en-us.xml） |
| 模板库（35 个具体模板页 + 14 个分类聚合页 + gallery 精选 10 个） | 模板 | 免去从零配 channel/canvas/list/workflow | https://slack.com/templates/gallery ；分类如 /templates/project-management、/templates/sales | https://slack.com/templates/gallery |
| Slack Agent Templates | Agent 模板 | 按主题（入职/支持/客户洞察）快速部署 agent | 官方引导式 setup | https://slack.com/ai-agents |
| Slackbot Skills | Agent 技能 | 把个人绝活变成组织资产 | markdown 或 canvas → API 发布 | https://docs.slack.dev/ai/slackbot-skills |
| Slack MCP Server | 工具/接口 | 让外部 AI 工具安全读写 Slack | 服务器地址 `https://mcp.slack.com/mcp`（远程 HTTP + OAuth） | https://docs.slack.dev/ai/slack-mcp-server |
| Slack MCP and Skills Plugin | 工具（给 coding agent） | 一条命令给 Claude Code/Cursor/Codex 装上 Slack 开发技能 + MCP | `/plugin marketplace add slackapi/slack-skills-plugin` | https://docs.slack.dev/ai/slack-skills-plugin |
| Slack CLI | 工具 | 脚手架、部署、生命周期管理（90 个命令文档页） | `slack create` / `slack run` / `slack deploy` | https://docs.slack.dev/tools/slack-cli/reference/commands/ |
| Bolt（JS / Python / Java） | SDK | 写 app 与 agent 的主框架 | 官方 samples + 文档 | https://docs.slack.dev |
| Deno Slack SDK | SDK | 跑在 Slack 基础设施上的 workflow app（"Run on Slack"） | `slack deploy` | https://docs.slack.dev （samples 区） |
| 官方 samples / 模板代码（8 个：Support Agent、Starter Agent、MCP-calling agent、Webhook alerts、GitHub Action、GitHub issues、Custom workflow step、Announcement bot） | 示例代码 | 跳过搭建，直接改 | `slack create <tpl>` 或 GitHub slack-samples | https://docs.slack.dev |
| slack-github-action（v4.0.0） | 工具 | CI/部署结果推进频道 | GitHub Actions 市场 | https://docs.slack.dev/tools/slack-github-action |
| Developer Program sandbox | 环境 | 管理员未批 MCP 时先试 | 申请免费 sandbox | https://docs.slack.dev/tools/developer-sandboxes |
| 开发者文档库 | 文档 | 359 个 Web API 方法、121 个事件、129 个 scope、46 个 block element、22 个 block、3,266 个文档 URL | 公开访问 | https://docs.slack.dev ；计数来自 https://docs.slack.dev/sitemap.xml |
| 帮助中心 | 文档 | 终端用户与管理员自助 | 公开访问；578 篇文章 × 13 语言 | https://slack.com/help |
| Slack 认证（Slack Certified） | 认证 | 顾问/管理员资质 | slackcertified.com | https://slackcertified.com/ |
| 客户故事库（199 个页面） | 案例 | 采购评估与对标 | 公开浏览 | https://slack.com/customer-stories |
| 资源库（107 个页面）/ 博客（1,179 篇） | 内容 | 教育型获客 | 公开浏览 | https://slack.com/resources ；https://slack.com/blog |

数量口径说明：
- 应用数量官方口径 "over 2,600 apps"（导航与多个功能页重复出现）；sitemap 内 `/marketplace/<id>-<slug>` 形页面 **2,871** 条（可能是含下架/历史项，未逐个核验）——https://slack.com/sitemaps/sitemap_marketplace_en-us.xml。
- Marketplace 分类/合集：从 https://slack.com/marketplace 页面内嵌 JSON 解析出 **23 个分类/合集 slug**；其中出现的分类名称包括 Analytics、Communication、Customer Support、Design、Developer Tools、File Management、Finance、HR & Team Culture、Marketing、Office Management、Productivity、Project Management、Sales、Security & Compliance、Slack Code Apps、Social & Fun、Voice & Video、Working from Home、AI Apps & Assistants、Brilliant Bots、Daily Tools、Enterprise-Ready Apps、Essential Apps、Featured、MCP Registry、New & Noteworthy（名称去重 26 个，与 slug 数不完全对齐，未逐个核验对应关系）。其中 Featured / New & Noteworthy / Brilliant Bots / Essential Apps / Enterprise-Ready Apps / Slack Code Apps / MCP Registry / Daily Tools 属官方编辑型推荐位，即「榜单机制」。
- 模板：sitemap 内 `/templates/*` 共 **50** 条 = 1 个 gallery + **14 个分类页**（communication、customer-service、engineering、file-management、human-resources、it、marketing、planning、product-management、productivity、project-management、sales、team-culture、team-management，页面标题为 "Templates for X"）+ **35 个具体模板页**（标题为 "X Template"）。分类归属为按页面标题实测，非官方声明。

---

## F. 流量曝光渠道

### F1. SEO 结构（官方 sitemap 实测计数）

主 sitemap 索引 13 个语言版本（en-us、en-gb、es-la、es-es、pt-br、de-de、fr-fr、it-it、zh-cn、zh-tw、en-in、ja-jp、ko-kr）——https://slack.com/sitemap.xml

英文站（sitemap_en-us.xml）**1,769** 条 URL，结构分布：

| 路径段 | 条数 | 说明 |
|---|---|---|
| /blog/* | 1,179 | 内容营销主力（博客为最大单一板块） |
| /customer-stories/* | 199 | 客户案例（采购决策期关键词） |
| /resources/* | 107 | 指南/报告/白皮书 |
| /policy-archives/* | 50 | — |
| /templates/* | 50 | 1 gallery + 14 分类 + 35 模板 |
| /solutions/* | 32 | 场景页（9 部门 + 9 行业 + 11 use case + 4 其他） |
| /features/* | 23 | 功能页（含大小写重复 /features/Agentic-Platform） |
| /events/* | 22 | 活动页 |
| /trust/* | 17 | 安全与合规 |
| /release-notes/* | 8、/downloads/* 5、/pricing/* 4、/compare/* 4、/slack-tips/* 4、/ai-agents 2 | 尾部 |

另有三个独立 sitemap（robots.txt 声明）：
- `https://slack.com/sitemap_marketplace.xml` → 英文 **2,881** 条（2,871 个应用页 + 9 个 collection + 1 个首页）
- `https://slack.com/sitemap_help.xml` → 英文 **579** 条（578 篇帮助文章 + 1 个首页），另 12 个语言版本
- `https://slack.com/sitemaps/blog/news/sitemap.xml`（新闻博客单独一份）

对比页（competitor SEO）两套并存：
- 产品级对比页（导航 "Why Slack?" 下）：`/compare/slack-vs-teams`（含 /contact-sales、/demo-microsoft-365-integration 两个转化子页）、`/compare/slack-vs-email`
- 博客级对比集群 `/blog/compare/*` 共 **18** 条：slack-vs-asana、slack-vs-chatwork、slack-vs-clickup、slack-vs-discord、slack-vs-google-chat、slack-vs-line-works、slack-vs-mattermost、slack-vs-microsoft-teams、slack-vs-monday、slack-vs-stackfield、slack-vs-trello、slack-vs-whatsapp、slack-vs-zoom（13 个竞品 vs 页）+ teams-alternatives、discord-alternatives、google-chat-alternatives、trello-alternatives（4 个 "alternatives" 页）+ 1 个德语法务页

SEO 手法（可核验的部分）：
- 对比页自带锚点目录 "See comparison table"、6 条 reasons、94%/97min/1.7M 三个数字（https://slack.com/compare/slack-vs-teams）
- 单档独立定价页（/pricing/free、/pricing/pro、/pricing/businessplus、/pricing/paid-vs-free）承接 "slack pricing/free plan" 类词
- 模板页是「长尾 + 产品内激活」双重入口（模板可一键落进工作区）
- 帮助中心是独立信息架构（/help/categories/<id>，578 篇），与营销站分离
- 多语言：13 个语言站，URL 模式 `/intl/<locale>/...`（实测 zh-cn 版与 en 版内容一致）
- Marketplace 2,871 个第三方应用页天然贡献长尾（第三方开发者自带流量回流）

### F2. 其他渠道

| 渠道 | 证据 |
|---|---|
| PLG 免费档 | Free $0 永久免费、90 天历史、10 个应用；所有页面 CTA 为 "Get started"（无销售介入）——https://slack.com/pricing |
| 企业销售 | 每页并行 "Talk to sales/Request a demo"，且带来源参数（?id=slackbot、?from_teams_compete=1、?from_enterprise=1、?slug=gallery） |
| Partner 体系 | Partner Program（/partners）、Partner Offers（/partner-offers）、Slack Certified（slackcertified.com） |
| 社区 | Slack Community（/community）、开发者社区（docs 内 changelog 37 页 + 16 个 tag 页） |
| 活动 | 22 个活动页（/events/*）；产品内 "Watch demo" 视频（YouTube 嵌入） |
| 客户故事 | 199 个案例页，按公司规模/行业切分 |
| Marketplace 生态分发 | 第三方开发者在 Slack 目录上架，反向为 Slack 带来应用页长尾（2,871 页） |
| Salesforce 渠道 | 官网署名 "Salesforce 旗下公司"；Slackbot 进入 Salesforce Lightning；Flex Credits 走 Salesforce 售卖（https://slack.com/pricing FAQ） |
| AI/Agent 生态 | 与 Anthropic、OpenAI（ChatGPT app）、Perplexity、Google Cloud（Agentspace）在平台页互背书（https://slack.com/features/agentic-platform） |

### F3. 增长史（公开可查里程碑）

来源统一为 https://en.wikipedia.org/wiki/Slack_(software)（原文引用已内联，抓取时脚注被剥离）：

| 时间 | 事件 |
|---|---|
| 2013 前 | 起源于 Tiny Speck 内部沟通工具（为开发 Glitch 而生），最初基于 IRC |
| 2013-08 | 公开发布；24 小时内 8,000 个客户注册 |
| 2014-2015 | 早期增长：2015-02 官方称每周新增约 1 万 DAU，付费客户超 135,000、覆盖 60,000 个团队 |
| 2018-07-26 | 从 Atlassian 收购 HipChat 与 Stride，2019-02 关停并迁移用户 |
| 2019-06 | 以直接上市（DPO）上市，市值 195 亿美元 |
| 2020-07 | 收购 Rimeto（员工目录）；2021-06 以 "Slack Atlas" 形态上线 |
| 2020-12-01 | 宣布 Salesforce 以约 277 亿美元收购 |
| 2021-07-21 | 收购完成，Slack 成为 Salesforce 旗下公司 |
| 2022-12-05 | Butterfield 离职，Lidiane Jones 接任；2023-11-13 Denise Dresser 接任；2025-12 Dresser 转投 OpenAI，Rob Seaman 任临时 CEO |
| 2023-03 | 与 OpenAI 合作上线 ChatGPT 集成（摘要/问答/起草） |
| 2025-02 | 发生一次被广泛报道的宕机 |
| 2025-05 | Agentforce 进入 Slack（可构建部署任务型 agent） |
| 2025-06 | 开始阻止 LLM 通过 Slack API 长期索引/复制/存储数据 |

### F4. 判断：主要靠什么被看见

[推断] 三条腿并行，权重从大到小：
1. **产品内 PLG + 团队自传播**：免费档无销售介入、模板/应用可一键落进工作区、"Share skills to strengthen your team"（把个人工作流转成全队资产）都是内建传播机制。依据：定价页 CTA 结构、Slackbot 页的 skill 共享叙事、模板的产品内落地说明。
2. **大站 SEO**：1,769 页营销站 + 2,881 页 Marketplace + 579 页帮助中心，其中 blog 1,179 篇是最大单一板块，13 篇竞品 vs 页 + 4 篇 alternatives 页专门吃比较型搜索。依据：三个 sitemap 的实际 URL 分布。
3. **Salesforce 企业渠道**：官网署名、Lightning 内嵌、Flex Credits 走 Salesforce 销售、企业页与 contact-sales 多入口。依据：pricing FAQ、平台页、企业页。

未被官方披露、也不做推测的：自然搜索流量占比、各渠道 CAC、Marketplace 带来的实际注册占比——均未核验。

---

## G. 事实缺口（不编数字）

| 缺口 | 状态 |
|---|---|
| DAU / MAU / 付费席位数 | 未核验。官网只给「10 亿+ 每日消息」「400 万 Connect 用户」「300 万 每日工作流」等间接口径，均标注为 Salesforce 内部/财报数据，无席位总数 |
| ARR / 营收 | 未核验。Salesforce 财报未单独拆分 Slack 收入口径（本次未找到官方拆分数字） |
| 网站流量（月访问、自然搜索占比） | 未核验。本轮未取 Similarweb/Ahrefs 类数据，sitemap 只能证明页面规模，不能证明流量 |
| Marketplace 应用准确总数 | 官方口径 2,600+，sitemap 2,871 条，两者不一致（可能含下架项），未逐个核验 |
| Slackbot 周消息限额的具体数值 | 未核验。定价 FAQ 只说 "no weekly message limits"（Enterprise+）与 "limited trial"（Free/Pro），未公布具体条数 |
| Workflow Builder 免费档可用性 | 冲突未解：功能页 FAQ 说 Workflow Builder 是付费功能（Pro/Business+/Enterprise），但定价页 Free 档又列出 "AI workflow generation"；两者指的可能不是同一能力，未核验 |
| /solutions/use-cases hub 页 | 该 URL 404（只有 11 个子页），官方未提供 use case 汇总页 |
| ProductHunt 榜单/票数 | 抓取被 Cloudflare 拦截（2026-11-24 记录），不可作为事实 |
| 各档位的实际转化率/ACV | 未核验（官方无披露） |
