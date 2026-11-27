# 可复用模式（Patterns）

> 只收**跨产品可迁移的结构**，不收单个产品的功能。
> 每条：结构 → 证据 → 适用条件 → 反例/风险 → 我的用法。

---

## P1. 平台生态模式：把「原子」标准化，让生态替你长功能

**结构**：容器（channel）× 身份（app/bot）× 权限 × 事件总线 × 消息协议 → 任何第三方都能把业务动作塞进同一个界面。

**证据（Slack）**：
- 2,600+ apps 接入（https://slack.com/marketplace ，sitemap 实测 en-US 应用页 2,881 条）
- 平台自述「agent infrastructure for enterprise-ready AI」：Slackbot MCP client + Real-time Search API + Slack-authorized MCP server（https://slack.com/features/agentic-platform）
- 开发者工具：Slack CLI / Bolt / Block Kit（同上）

**为什么成立**：生态方只需要适配一次「身份+权限+事件+消息」，之后每加一个 app，平台的价值线性增长、成本不增。

**适用条件**：① 你已经是高频工作场所（用户每天在里面）② 你能定义一套别人愿意适配的接入标准 ③ 你有治理能力（权限、审计、合规）。

**反例/风险**：没有高频场景就做平台 = 空市场；治理不过关，一个恶意 app 就能毁掉信任。

**我的用法**：不做平台，做**「单点工具的标准化接口」**——把自己的能力包成一个 MCP server / Skill，去别人的平台里当「插件」，而不是自己建平台。

---

## P2. 程序化 SEO 矩阵：一个模板 × 一千个词 = 一千个入口

**结构**：先定义「一种页面模板」，再用「数据 × 关键词」批量生成，每种页面只解决一个具体问题。

**证据（Taskade，sitemap 实测）**：

| 页面类型 | URL 数 | 说明 |
|---|---|---|
| templates | 3,997 | 项目模板页 |
| generate | 4,526 | 「生成 X」工具页 |
| agents | 3,169 | Agent 模板页 |
| automate | 2,361 | 自动化模板页 |
| prompts | 2,205 | 提示词页 |
| convert | 2,118 | 「X 转 Y」页 |
| community apps | 6,135 | 用户作品页（UGC） |
| blog | 1,125 | 内容 |
| marketing | 867 | 营销页 |
| wiki/learn/docs | 1,177 | 帮助与教学 |
| community profiles | 495 | 作者主页（UGC） |
| compare | 197 | 对比页 |
| integrations | 180 | 集成页 |
| ai | 43 | AI 能力页 |
| community（首页） | 7 | — |
| **合计** | **28,602** | 全部来自 sitemap（2026-11-26 逐个实测） |

**结构比总量更重要**：程序化资源页 **18,376 = 64.2%**；UGC app 页 **6,135 = 21.4%**；手写营销内容只占 **14.3%**。
**对比页也要拆开看**：197 页里 155 页是 `free-<竞品>-alternative`、33 页是纯第三方模型对比（`gpt-vs-claude` 这种，与产品无关）、只有 6 页是 `taskade-vs-*`——它不是在打品牌对比，是在**吃搜索量的形状**。

（来源：https://www.taskade.com/sitemap.xml 及其 17 个子 sitemap）

**为什么成立**：长尾词单价低但意图准；模板页天然「一页一答案」，而且用户点进来就能用。

**适用条件**：① 你的产品有「可枚举的使用场景」② 你能批量产出不重复的页面内容 ③ 你有内链结构把权重导到主转化页。

**反例/风险**：薄内容会被算法降权；页面之间高度重复 = 自己跟自己竞争。

**我的用法**：不做 3 万页，做 **30–100 页**：选一个垂直（如「AI 工作流」），按「场景 × 岗位」做 50 页，每页一个可复制的模板/工作流 + 一个可下载件。

---

## P3. AI 原生发现层（GEO 全套）：让 AI 找到你、读懂你、引用你

**结构**（Taskade 的完整动作，按成本从低到高）：

| 动作 | 具体做法 | 解决什么 |
|---|---|---|
| ① `llms.txt` | 站点说明书：TL;DR、事实、FAQ、**「How to Cite 我」的指定引用措辞** | 让 AI 一次读懂你是谁 |
| ② `SKILL.md` | 给 Agent 的操作手册：怎么连、有哪些工具、安全规则 | 让 Agent 知道怎么"用"你 |
| ③ Markdown 出口 | 任意页面加 `Accept: text/markdown` 返回 Markdown | 让抓取更省 token、更准 |
| ④ `.well-known` 元数据 | `api-catalog`、`mcp.json`、`mcp/server-card.json`、`agent-skills/index.json`、`oauth-protected-resource` | 让机器自动发现你的接口 |
| ⑤ MCP server | `https://www.taskade.com/mcp`（OAuth 2.0 + PKCE） | 让 Agent 能调用你 |
| ⑥ robots 态度 | `ai-train=yes, search=yes, ai-input=yes`（Content-Signal） | 明确授权，换被引用 |
| ⑦ 引用指南 | llms.txt 里写死「产品名/公司/一句话/引用句」 | 让 AI 引用时不写错 |

**证据（Taskade）**：https://www.taskade.com/llms.txt（2026-11-18 更新，含 How to Cite Taskade）、https://www.taskade.com/SKILL.md、https://www.taskade.com/robots.txt。

**对比（Slack）**：robots.txt 无 Content-Signal 声明；2025-06 起阻止 LLM 长期索引——**平台越大越倾向收紧，小产品反而可以用"开放授权"换被引用**。

**适用条件**：产品有能力/数据可被调用；否则 llms.txt 只是摆设。

**反例/风险**：只写 llms.txt 不开接口 = 说明书没有产品；开放抓取要防被白嫖（分层：公开层给说明、调用层要授权）。

**我的用法**：给我的知识库/工具站一次做齐三件：`llms.txt`（我是谁 + 怎么引用我）+ `SKILL.md`（怎么用）+ 一个查询/MCP 入口；再补 `.well-known/agent-skills/index.json`，让 Agent 能发现我的技能。

---

## P4. 免费档楔子 + 席位扩张

**结构**：个人免费用到「够用但不够团队」，付费墙卡在协作、权限、合规、数据量上。

**证据（Slack）**：Free 档含 90 天消息历史、最多 10 个 app、1:1 会议与 1:1 外部消息、基础 AI 摘要（https://slack.com/pricing）；付费升级卖的是历史、团队协作、企业治理。

**适用条件**：产品有「一人用 → 拉同事进来」的自然扩散动作。

**反例/风险**：免费档太厚 → 个人永不付费（Fathom 的教训，见 010）。

**我的用法**：免费档只放「一个人能完成的动作」；凡是「需要第二个人」的能力，一律收费。

---

## P5. 模板即产品：把「怎么用」做成可复制的起点

**结构**：模板不是文档，是「预填好数据与流程的实例」，打开即可运行。

**证据**：Taskade 模板 3,997 / agents 3,169 / automations 2,361（sitemap 实测）；Slack template gallery（https://slack.com/templates/gallery）。

**适用条件**：你的产品有「结构化的重复任务」。

**我的用法**：每个工作流都配一个「空白版 + 三个填好的版本」，用户先改再建。

---

## P6. 克隆工厂：把用户作品变成你的内容资产

**结构**：用户一键克隆别人的 app → 生成自己的作品页 + 作者主页 → 全部进 sitemap（UGC SEO）。

**证据（Taskade）**：
- community-apps sitemap 6,135 条（https://www.taskade.com/sitemaps/community-apps.xml）
- community-profiles sitemap 495 条（https://www.taskade.com/sitemaps/community-profiles.xml）
- 导航「Clone：Dashboards / Operations / Commerce / All categories」（https://www.taskade.com/apps）
- App Kit 可免费/付费分发，创作者可提现（https://www.taskade.com/llms.txt）

**适用条件**：产品有「成品可复制」的属性；否则克隆出来是空壳。

**反例/风险**：UGC 质量不可控，需要审核与推荐位。

**我的用法**：把「案例库」做成可克隆的结构（每个案例 = 一个可复制的模板 + 一段判断），案例即内容、内容即入口。

---

## P7. UGC 自带发现层：让每个用户产出都成为 SEO/GEO 节点

**结构**：用户发布的作品，平台自动为它生成 `robots.txt` / `sitemap.xml` / `llms.txt`，并进入全站 sitemap。

**证据（Taskade Publish 说明）**：发布后的 app 有自己的域名（`your-app.taskade.app` 或自定义），"Every indexable app serves robots.txt, sitemap.xml, and llms.txt automatically"（https://www.taskade.com/llms.txt）。

**为什么成立**：用户为了自己的流量，会主动把作品分享出去；平台不花一分钱获得长尾页和 AI 可读入口。

**适用条件**：产品让用户「发布」东西（页面/店铺/作品/知识库）。

**反例/风险**：垃圾 UGC 会污染站点质量；需要质量门槛与索引策略。

**我的用法**：我的知识库/工具如果开放发布，默认给每个作品生成 sitemap + llms.txt + 一段结构化 JSON-LD，而不是只给一个 URL。
