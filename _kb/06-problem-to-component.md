# 问题 → 组件（Problem → Component）

> 用法：**先看你遇到的是哪类问题，再看别人用什么组件解决，最后回 `02-atoms` / `03-workflows` / `05-resources` 看实现细节与出处。**
> 每条格式：问题 → 可复用组件（产品·组件）→ 怎么用 → 证据。
> 只收「有出处 + 我能用」的条目；纯概念不进这张表。

---

## A. 让 AI 进入「已经有人工作的地方」

| # | 问题 | 可复用组件 | 怎么用 | 证据 |
|---|---|---|---|---|
| A1 | AI 做完了，但用户还要切到另一个界面看结果 | **Slackbot + MCP client**（把外部 app/agent 接进 Slackbot，结果回到对话流） | 把 agent 当成一个「会说话的同事」放进频道：提问在频道、结果回频道，不另开页面 | https://slack.com/features/agentic-platform |
| A2 | 团队有 10 个工具，AI 不知道去哪个系统查 | **Slack-authorized MCP server + Real-Time Search API**（给 agent 一份「Slack 内上下文」的授权数据入口） | agent 不复制数据，拿授权去读：先查上下文，再行动 | https://slack.com/features/agentic-platform |
| A3 | 想给团队做一个「懂业务」的 AI，但不想自己训模型 | **Taskade AI Agent = 提示词 + 工具 + 知识**（三件套配置） | 先定角色与边界（提示词），再挂工具（动作），再挂知识（文件）——三层缺一不可 | https://www.taskade.com/agents |
| A4 | AI 只会聊天，不会动手 | **Agent tools / actions**（把「查、写、改、发」变成可调用动作） | 每个工具只做一件事，用工作流把工具串起来 | https://www.taskade.com/agents |

---

## B. 把重复动作变成自动流程

| # | 问题 | 可复用组件 | 怎么用 | 证据 |
|---|---|---|---|---|
| B1 | 每周固定要发提醒/汇总/审批 | **Workflow Builder**（触发器 → 步骤 → 消息/记录） | 先画「什么事件触发」，再排 3–5 步；超过 7 步就拆成两条 | https://slack.com/features/workflow-automation |
| B2 | 业务动作分散在多个系统，人手搬运 | **Automation = trigger → action**（Taskade） | 一个 trigger 只配一条主链路；分支用条件，不要堆 | https://www.taskade.com/automate |
| B3 | 不知道哪些流程值得自动化 | **官方自动化模板库**（Taskade 2,361 条 / Slack 模板库） | 用模板反推：先抄一条跑通，再改成自己的 | https://www.taskade.com/sitemaps/sitemap-automate.xml |

---

## C. 找信息 / 建知识库

| # | 问题 | 可复用组件 | 怎么用 | 证据 |
|---|---|---|---|---|
| C1 | 信息散在聊天、文档、邮件里 | **Enterprise Search**（跨系统统一搜索入口） | 搜索框放在最显眼处，结果按「人/文件/消息」分组 | https://slack.com/features/enterprise-search |
| C2 | 知识库没人维护、AI 读不到 | **Skill = SKILL.md + references/**（把「怎么干」和「资料」分层） | 规则写进 SKILL.md，资料放 references，按需读取，不整包塞上下文 | https://www.taskade.com/SKILL.md |
| C3 | 想让 AI 找到你的站/库 | **llms.txt + MCP server + SKILL.md**（AI 原生发现层） | 给 AI 一份「本站怎么用」的说明书 + 一个可调用入口 | https://www.taskade.com/llms.txt |

---

## D. 冷启动：让用户第一天就能出结果

| # | 问题 | 可复用组件 | 怎么用 | 证据 |
|---|---|---|---|---|
| D1 | 用户面对空白页不知道从哪开始 | **模板库**（Taskade：projects 3,997 / agents 3,169 / automations 2,361；Slack：template gallery） | 模板不是「示例」，是「预填好的结构」——打开就有内容 | https://www.taskade.com/templates |
| D2 | 用户想直接要一个成品，不想自己搭 | **Genesis / App Factory**（一句话生成一个完整 app，可克隆别人的） | 先给成品，再让用户改；改的过程就是上手过程 | https://www.taskade.com/apps |
| D3 | 冷启动没有内容/数据 | **社区克隆 + 作者主页**（community apps 6,135 + profiles 495） | 让用户的作品成为你的内容资产（UGC SEO） | https://www.taskade.com/sitemaps/community-apps.xml |

---

## E. 对外协作（客户/供应商/外部团队）

| # | 问题 | 可复用组件 | 怎么用 | 证据 |
|---|---|---|---|---|
| E1 | 和外部公司协作要来回发邮件 | **Slack Connect**（跨组织频道/私信） | 把「外部人」拉进同一个频道，权限按频道隔离 | https://slack.com/connect |
| E2 | 客户不想注册你的产品 | 分享链接/客户视图（需按产品核验，Taskade share/clone 待核） | 先给「只读/可评论」的入口，再谈注册 | 待核验 |

---

## F. 数据与工具接入

| # | 问题 | 可复用组件 | 怎么用 | 证据 |
|---|---|---|---|---|
| F1 | 要接 10 个 SaaS，逐个开发 | **应用市场 + 标准化接入**（Slack 2,600+ apps；Taskade 100+ integrations） | 先做「一个标准接入协议」，再让别人来适配你 | https://slack.com/marketplace |
| F2 | 开发者不愿意为你的平台写代码 | **CLI + SDK + Block Kit**（Slack CLI / Bolt / 组件库） | 把「做一个 app」压到 1 小时以内，生态才会长 | https://slack.com/features/agentic-platform |

---

## G. 分发与增长

| # | 问题 | 可复用组件 | 怎么用 | 证据 |
|---|---|---|---|---|
| G1 | 没有预算投广告 | **程序化 SEO 矩阵**（Taskade ≈3.2 万 URL：模板/生成/转换/对比/集成/社区） | 先找「有人搜、没人做好」的词，再批量做「一页解决一个问题」 | 见 `04-channels.csv` |
| G2 | 品牌弱，搜索搜不到 | **对比页**（Slack /compare/slack-vs-teams；Taskade 197 条 compare） | 每张对比页只回答一个「X vs Y」的决策 | https://slack.com/compare/slack-vs-teams |
| G3 | AI 搜索里找不到你 | **llms.txt + MCP + SKILL.md**（GEO 三件套） | 给 AI 可读的站点说明 + 可调用工具 | https://www.taskade.com/llms.txt |

---

## H. 交付：从「工具」变成「结果」

| # | 问题 | 可复用组件 | 怎么用 | 证据 |
|---|---|---|---|---|
| H1 | 用户要的是结果，不是功能 | **容器化交付**（channel/canvas/list 承载产出物，agent 只负责生成） | 把结果落进一个「可继续编辑的容器」，而不是一次性回复 | https://slack.com/features/canvas |
| H2 | 一次交付后没有复购 | **模板 → 克隆 → 定制**（Taskade 克隆工厂） | 标准品免费/低价，定制收费 | https://www.taskade.com/apps |

---

## I. AI 时代的新问题（2026 新增，来自 013/014 两期）

| # | 问题 | 可复用组件 | 怎么用 | 证据 |
|---|---|---|---|---|
| I1 | AI 记不住上次的上下文，每次从零开始 | **Persistent Memory 存成 Project**（Taskade：agent 记忆 = 一个可浏览/编辑/fork 的项目） | 记忆不要放黑盒，放成结构化数据：可看、可改、可迁移 | https://www.taskade.com/llms.txt |
| I2 | 想让 AI 引用你，但它不知道你是谁/怎么引用 | **llms.txt + 「How to Cite 我」+ `.well-known` 元数据** | 给 AI 一份说明书，直接写死引用措辞 | https://www.taskade.com/llms.txt |
| I3 | 模板卖一次就没了，没有复利 | **App Kit：可克隆 + 可售卖 + 可导出（.tsk / GitHub）** | 把「模板」升级成「可流通资产」，创作者分成 | https://www.taskade.com/llms.txt |
| I4 | 用户发布的作品没有流量，平台也拿不到长尾 | **发布即带 robots/sitemap/llms.txt** | 每个用户作品都是一个发现节点 | https://www.taskade.com/llms.txt |
| I5 | 模型换代就要重写产品 | **模型阶梯（按任务路由模型）+ BYOK** | 产品抽象在「任务→模型的路由」，不在某个模型 | https://www.taskade.com/llms.txt |

---

> 维护规则：每拆一个新产品，往里补 3–8 条；**同一条问题下出现第 3 个组件时，去 `07-patterns.md` 升级成「模式」**。
