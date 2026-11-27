# -*- coding: utf-8 -*-
"""一次性把 Slack / Taskade 两期的结构层数据写入 _kb/*.csv。
可重复运行：会重写表头 + 这两期的行（不碰其他产品）。
"""
import csv, os

BASE = r"D:\claudework\teardown-100\_kb"
UPDATED = "2026-11-26"

products = [
    dict(no="013", slug="slack", name="Slack", category="B2B 协作 / AI 工作平台",
         one_liner="把团队沟通、协作和 AI agent 放进同一个工作场所：频道承载对话，Slackbot 承载执行",
         icp_primary="团队与企业（从 10 人到 10 万人）",
         icp_secondary="开发者/IT（做集成与治理）；销售与客服团队",
         jtbd="让团队在一个地方沟通，并让 AI 在对话流里直接干活",
         core_scenarios="频道协作 / 内部沟通 / 跨公司协作 / 会议 / 项目跟踪 / 销售管道 / 客户服务 / 招聘入职 / 企业搜索 / 自动化",
         ai_mode="原生（AI-native 平台，Slackbot + MCP + Agentforce）",
         pricing_model="Freemium + 按席位订阅 + 企业年付",
         free_tier="Free：90 天消息历史、最多 10 个 app、1:1 会议、1:1 外部消息、基础 AI 摘要",
         paid_tiers="Pro / Business+ / Enterprise+（按人月；具体价格以定价页为准）",
         atoms_count="15", workflows_count="10",
         primary_channels="PLG 免费档 + 企业销售 + 应用市场目录（2,881 应用页）+ 13 语种 SEO + 对比页",
         moat_hypothesis="工作场所占据 + 生态网络效应：用户越多→app 越多→越难换",
         evidence_urls="https://slack.com/pricing; https://slack.com/features/agentic-platform; https://slack.com/marketplace",
         updated_at=UPDATED),
    dict(no="014", slug="taskade", name="Taskade", category="AI 协作 / 任务与 Agent 平台",
         one_liner="一个工作区里同时有项目、文档、思维导图、AI agent 与自动化；还能一键克隆别人的成品 app",
         icp_primary="小团队 / 一人公司 / 代理机构",
         icp_secondary="创作者、学生、远程团队",
         jtbd="把任务、笔记、AI 执行和自动化放在同一个工作区，且能直接克隆成品开始",
         core_scenarios="项目与任务 / 文档 / 思维导图 / AI agent / 自动化 / 生成与转换 / 社区 app 克隆",
         ai_mode="原生（AI-first：TSK-1 智能层 + AI agents + MCP）",
         pricing_model="Freemium + 订阅（个人/团队/企业档，价格以定价页为准）",
         free_tier="Free $0 永久：2 个成员、3 个 Genesis app、1 个 agent、10 次自动化/月、1 个知识源；无月度 credits（靠邀请获得）",
         paid_tiers="Starter $6；Pro $10（月付 $20）；Business $25；Max $100；Enterprise $250（均为年付折算月价，年付省 50%）",
         atoms_count="23", workflows_count="16",
         primary_channels="程序化 SEO 28,602 页（程序化 64.2% / UGC 21.4% / 手写 14.3%）+ UGC 克隆 6,135 页 + llms.txt / MCP 的 AI 原生发现 + 155 页 free-竞品-alternative",
         moat_hypothesis="模板 × 同一数据模型 × 克隆：一个对象图，四种封装（项目/agent/自动化/app）",
         evidence_urls="https://www.taskade.com/; https://www.taskade.com/agents; https://www.taskade.com/sitemap.xml",
         updated_at=UPDATED),
]

atoms = [
    # Slack
    ("SL-01", "slack", "Channel", "容器", "承载一个话题的持续对话", "message / thread / app / workflow / canvas", "https://slack.com/features/channels"),
    ("SL-02", "slack", "Thread", "容器", "把回复挂在单条消息下，对话不散", "channel / search / app", "https://slack.com/features/channels"),
    ("SL-03", "slack", "Canvas", "容器", "可协作的结构化文档", "channel / message / agent", "https://slack.com/features/canvas"),
    ("SL-04", "slack", "List", "容器", "项目/任务列表，可在频道里跟踪", "channel / workflow", "https://slack.com/features/task-list"),
    ("SL-05", "slack", "Huddle", "动作", "音视频会议与屏幕共享", "channel / canvas / AI 摘要", "https://slack.com/features/huddles"),
    ("SL-06", "slack", "Message", "动作", "发送消息（对话的基础动作）", "所有容器", "https://slack.com/features/channels"),
    ("SL-07", "slack", "App / Bot", "身份", "第三方应用或机器人的账号身份", "channel / event / MCP / workflow", "https://slack.com/marketplace"),
    ("SL-08", "slack", "Slash Command", "动作", "在输入框用一个命令调用 app", "app / workflow", "https://api.slack.com"),
    ("SL-09", "slack", "Workflow Trigger/Step", "动作", "事件触发 + 串行步骤", "canvas / message / app / list", "https://slack.com/features/workflow-automation"),
    ("SL-10", "slack", "MCP Tool", "工具", "把外部能力暴露成 agent 可调工具", "Slackbot / app", "https://slack.com/features/agentic-platform"),
    ("SL-11", "slack", "Real-Time Search API", "知识", "让 agent 读 Slack 内的对话上下文", "agent / MCP", "https://slack.com/features/agentic-platform"),
    ("SL-12", "slack", "Slack Connect", "容器/身份", "跨组织频道与私信", "channel / 权限", "https://slack.com/connect"),
    ("SL-13", "slack", "Code Channel", "容器", "人与 agent 在频道里一起写代码", "channel / app", "https://slack.com/features/code-channels"),
    ("SL-14", "slack", "Block Kit", "工具", "可组合的 UI 组件，给 app 拼界面", "app / message", "https://docs.slack.dev/block-kit/"),
    ("SL-15", "slack", "Slackbot", "身份", "团队里的 AI 队友，可调 MCP 工具", "MCP / 权限 / 频道", "https://slack.com/features/slackbot"),
    # Taskade
    ("TD-01", "taskade", "Workspace", "容器", "组织所有项目/agent/自动化", "project / agent / automation", "https://www.taskade.com/"),
    ("TD-02", "taskade", "Project", "容器", "任务 + 文档 + 数据的集合", "task / view / template", "https://www.taskade.com/templates"),
    ("TD-03", "taskade", "Task", "动作", "最小执行单元（可指派/设截止）", "project / automation / agent", "https://www.taskade.com/"),
    ("TD-04", "taskade", "Note / Doc", "界面（视图）", "文档型视图（project 的一种 view，不是独立对象）", "project / agent 知识", "https://www.taskade.com/SKILL.md"),
    ("TD-05", "taskade", "Mind Map", "界面（视图）", "思维导图视图（project 的一种 view，不是独立对象）", "project / note", "https://www.taskade.com/SKILL.md"),
    ("TD-06", "taskade", "AI Agent", "身份", "有角色 + 工具 + 知识的执行体", "tool / knowledge / automation", "https://www.taskade.com/agents"),
    ("TD-07", "taskade", "Agent Tool / Action", "工具", "agent 可调用的单个动作", "agent / automation", "https://www.taskade.com/agents"),
    ("TD-08", "taskade", "Automation Trigger", "动作", "什么事件让流程开始", "action / agent", "https://www.taskade.com/automate"),
    ("TD-09", "taskade", "Automation Action", "动作", "触发器之后执行的动作", "trigger / agent / task", "https://www.taskade.com/automate"),
    ("TD-10", "taskade", "Knowledge File", "知识", "挂给 agent 的参考资料", "agent / SKILL.md", "https://www.taskade.com/SKILL.md"),
    ("TD-11", "taskade", "Template", "工具", "预填好的实例（项目/agent/自动化）", "project / agent / automation", "https://www.taskade.com/templates"),
    ("TD-12", "taskade", "Genesis App", "容器", "一句话生成的完整应用", "project / agent / automation", "https://www.taskade.com/apps"),
    ("TD-13", "taskade", "Clone", "动作", "克隆社区里的现成 app", "app / template / profile", "https://www.taskade.com/apps"),
    ("TD-14", "taskade", "MCP Server", "工具", "对外暴露可调用的 Taskade 接口", "外部 agent / llms.txt", "https://www.taskade.com/mcp"),
    ("TD-15", "taskade", "SKILL.md", "知识/协议", "给 agent 看的使用手册", "references / MCP", "https://www.taskade.com/SKILL.md"),
    ("TD-16", "taskade", "Integration", "工具", "连接 100+ 外部应用", "agent / automation", "https://www.taskade.com/integrations"),
    ("TD-17", "taskade", "Community Profile", "身份", "克隆作品背后的作者主页", "app / clone", "https://www.taskade.com/sitemaps/community-profiles.xml"),
    ("TD-18", "taskade", "View", "界面", "同一份数据的多种视图（List/Board/Table/MindMap/Docs/Calendar/Gantt/Actionsheet/OrgChart）", "project / field", "https://www.taskade.com/SKILL.md"),
    ("TD-19", "taskade", "App Kit", "分发", "把 app + 项目 + agent + 自动化打包，可克隆/可售卖/可导出", "clone / template / earnings", "https://www.taskade.com/llms.txt"),
    ("TD-20", "taskade", "App User", "身份", "发布 app 的终端用户账号（独立于 Taskade 账号）", "publish / sign-in", "https://www.taskade.com/llms.txt"),
    ("TD-21", "taskade", "Persistent Memory", "知识", "agent 的记忆存成一个 Project，可浏览/编辑/fork", "agent / project", "https://www.taskade.com/llms.txt"),
    ("TD-22", "taskade", "TSK Model Ladder", "智能", "按任务选模型（Auto/Instant/Standard/Thinking/Reasoning），模型是耗材", "agent / eve / automation", "https://www.taskade.com/llms.txt"),
    ("TD-23", "taskade", "Taskade EVE", "身份", "内部 AI builder / meta-agent：把一句话变成 app", "genesis / projects / agents / automations", "https://www.taskade.com/SKILL.md"),
]

workflows = [
    ("WF-SL-01", "slack", "对话里问 → Slackbot 调 MCP → 结果回频道", "一句自然语言问题", "Message + Slackbot + MCP Tool + Channel", "发起 → Slackbot 路由到专用 agent → 工具执行 → 回帖", "答案 / 动作结果（留在对话流）", "全员", "https://slack.com/features/agentic-platform"),
    ("WF-SL-02", "slack", "Huddle 开会 → AI 记录 → 摘要与行动项", "一场会议", "Huddle + AI 摘要 + Canvas/Message", "开会 → 转写 → 摘要 → 发到频道/画布", "会议纪要 + 后续动作", "会议参与者", "https://slack.com/features/huddles"),
    ("WF-SL-03", "slack", "表单 → 审批 → 通知（Workflow Builder）", "一条表单提交", "Workflow Trigger + Step + Message + App", "触发 → 收集 → 审批 → 通知 → 记录", "一条被审批的请求", "运营/HR/IT", "https://slack.com/features/workflow-automation"),
    ("WF-SL-04", "slack", "频道内项目跟踪（List）", "项目任务清单", "List + Channel + Message", "建列表 → 分派 → 更新 → 在频道同步", "可跟踪的项目清单", "项目团队", "https://slack.com/features/task-list"),
    ("WF-SL-05", "slack", "跨公司协作（Connect）", "外部合作伙伴", "Slack Connect + Channel", "建外部频道 → 邀请 → 按频道隔离权限", "与客户/供应商的协作空间", "销售/客户成功", "https://slack.com/connect"),
    ("WF-SL-06", "slack", "对话式 CRM", "与客户的对话", "Channel + Native CRM + App", "对话 → 提取联系人 → 推进商机 → 回写", "CRM 记录与下一步", "销售", "https://slack.com/crm"),
    ("WF-SL-07", "slack", "企业搜索查答案", "一个问题", "Enterprise Search + 各 app 索引", "提问 → 跨系统检索 → 分组结果", "答案 + 来源", "全员", "https://slack.com/features/enterprise-search"),
    ("WF-SL-08", "slack", "人机共建（Code Channel）", "一段需求/代码", "Code Channel + App + Agent", "拉人+拉 agent → 协作 → 记录", "代码与讨论记录", "工程团队", "https://slack.com/features/code-channels"),
    ("WF-SL-09", "slack", "装一个 app → 在频道里用", "第三方能力", "Marketplace App + Channel + Command", "安装 → 授权 → 命令/事件调用", "频道内的新能力", "全员", "https://slack.com/marketplace"),
    ("WF-SL-10", "slack", "Salesforce/Agentforce agent 进 Slack", "一条业务请求", "Agentforce + Slackbot + 数据", "请求 → agent 处理 → 回写记录", "业务动作与记录", "销售/服务团队", "https://slack.com/ai-agents"),
    ("WF-TD-01", "taskade", "从项目模板开始", "一个业务场景", "Template + Project + Task", "选模板 → 克隆 → 改任务 → 指派", "可运行的项目", "团队", "https://www.taskade.com/templates"),
    ("WF-TD-02", "taskade", "配置一个 AI Agent", "一个角色需求", "AI Agent + Agent Tool + Knowledge", "定角色 → 挂工具 → 挂知识 → 试跑", "能执行任务的 agent", "团队/个人", "https://www.taskade.com/agents"),
    ("WF-TD-03", "taskade", "自动化：触发器 → 动作", "一个事件", "Automation Trigger + Action + Agent", "设触发 → 选动作 → 绑定对象", "自动执行的流程", "运营", "https://www.taskade.com/automate"),
    ("WF-TD-04", "taskade", "Genesis 生成完整 app", "一句话需求", "Genesis App + Project + Agent + Automation", "描述 → 生成 → 试用 → 改", "一个可用 app", "个人/小团队", "https://www.taskade.com/apps"),
    ("WF-TD-05", "taskade", "克隆社区 app 改成自己的", "一个现成 app", "Clone + Template + Project", "找 app → 克隆 → 改数据/流程", "自己的版本", "个人/小团队", "https://www.taskade.com/apps"),
    ("WF-TD-06", "taskade", "生成 X（generate 页）", "一个生成需求", "AI 生成 + Template", "选场景 → 填参数 → 生成结构", "初稿结构", "个人", "https://www.taskade.com/generate"),
    ("WF-TD-07", "taskade", "X 转 Y（convert 页）", "一份旧格式内容", "Convert + Project/Doc", "上传/粘贴 → 转换 → 得到新结构", "转换后的结构", "个人/团队", "https://www.taskade.com/convert"),
    ("WF-TD-08", "taskade", "提示词 → agent 使用", "一个 prompt", "Prompts + AI Agent", "选提示词 → 粘进 agent → 执行", "执行结果", "个人", "https://www.taskade.com/prompts"),
    ("WF-TD-09", "taskade", "连接外部应用", "外部系统里的数据", "Integration + Agent/Automation", "授权连接 → 读/写 → 进入工作流", "跨系统数据流", "团队", "https://www.taskade.com/integrations"),
    ("WF-TD-10", "taskade", "外部 agent 调 Taskade（MCP）", "外部 agent 的请求", "MCP Server + SKILL.md", "配置 MCP → agent 调用 → 返回结果", "Taskade 数据被外部 agent 使用", "开发者", "https://www.taskade.com/mcp"),
    ("WF-TD-11", "taskade", "仪表盘/运营/电商 app 克隆", "一个管理场景", "Clone + Dashboard/Operations/Commerce 分类", "选分类 → 克隆 → 接数据", "管理类 app", "小团队", "https://www.taskade.com/apps/categories"),
    ("WF-TD-12", "taskade", "作者主页 → 作品被克隆", "一个可复用作品", "Community Profile + App", "发布作品 → 主页展示 → 他人克隆", "可复制的作品 + 曝光", "创作者", "https://www.taskade.com/sitemaps/community-profiles.xml"),
    ("WF-TD-13", "taskade", "一句话 → Genesis app（EVE 构建）", "一句业务描述", "EVE + Genesis App + Projects + Agents + Automations", "描述 → EVE 规划 → 建界面/数据/agent/自动化 → 发布", "一个托管上线的 app", "业务主/一人公司", "https://www.taskade.com/create"),
    ("WF-TD-14", "taskade", "App Kit 上架 → 他人克隆/购买", "一个原创 app", "App Kit + Clone + Earnings", "发布 kit → 设免费/付费 → 用户克隆 → 创作者提现", "可流通的成品资产", "创作者", "https://www.taskade.com/llms.txt"),
    ("WF-TD-15", "taskade", "公开 agent → 嵌入网站", "一个 agent", "Public Agent + Embed Widget + Visitor Inbox", "发布 → 复制 embed → 访客对话 → 进入收件箱/自动化", "网站上的 AI 客服/助手", "商家/创作者", "https://www.taskade.com/llms.txt"),
    ("WF-TD-16", "taskade", "外部 agent 经 MCP 操作工作区", "外部 agent 的请求", "Hosted MCP + SKILL.md + 工具集", "配置 MCP → OAuth → 调工具读写任务/项目/agent", "外部 agent 能操作 Taskade 数据", "开发者/重度用户", "https://www.taskade.com/SKILL.md"),
]

channels = [
    ("CH-SL-01", "slack", "SEO-本地化矩阵", "同一套营销页 × 13 个语种（en-US 1,769 页 / zh-CN 1,478 页）", "slack.com/intl/<locale>/...", "sitemap 实测：en-US 1,769；zh-CN 1,478；13 个语种子 sitemap", "5", "https://slack.com/sitemaps/sitemap_en-us.xml"),
    ("CH-SL-02", "slack", "SEO-应用目录", "每个 app 一个详情页，进 marketplace sitemap", "slack.com/marketplace/<APP_ID>-<slug>", "sitemap 实测：en-US 2,881 条", "4", "https://slack.com/sitemaps/sitemap_marketplace_en-us.xml"),
    ("CH-SL-03", "slack", "SEO-帮助中心", "按功能/问题建帮助文章页", "slack.com/help/articles/<id>-<slug>", "sitemap 实测：en-US 579 条（另有 13 个语种子 sitemap）", "3", "https://slack.com/sitemaps/sitemap_help_en-us.xml"),
    ("CH-SL-04", "slack", "SEO-对比页", "专门吃「Slack vs X」决策搜索", "slack.com/compare/<a>-vs-<b>", "官网导航直接放「Slack vs Teams」", "5", "https://slack.com/compare/slack-vs-teams"),
    ("CH-SL-05", "slack", "市场目录/生态", "2,600+ apps 把 Slack 带进别人的采购清单", "slack.com/marketplace", "官网自述 2,600+ apps", "4", "https://slack.com/marketplace"),
    ("CH-SL-06", "slack", "PLG 免费档", "免费档做楔子，靠团队扩散升级", "slack.com/get-started", "Free：90 天历史/10 apps/1:1", "5", "https://slack.com/pricing"),
    ("CH-SL-07", "slack", "企业销售与 Partner", "Demo → 销售 → 合作伙伴实施", "slack.com/contact-sales; /partners", "导航设 Partner Program / Partner Offers", "2", "https://slack.com/partners"),
    ("CH-SL-08", "slack", "社区/活动/客户故事", "社区、活动、客户案例做信任", "slack.com/community; /events; /customer-stories", "导航三处入口", "3", "https://slack.com/customer-stories"),
    ("CH-TD-01", "taskade", "SEO-模板矩阵", "每种项目模板一个页面", "taskade.com/templates/<slug>", "sitemap 实测：3,997 条", "5", "https://www.taskade.com/sitemaps/sitemap-templates.xml"),
    ("CH-TD-02", "taskade", "SEO-生成矩阵", "「生成 X」工具页", "taskade.com/generate/<slug>", "sitemap 实测：4,526 条", "4", "https://www.taskade.com/sitemaps/sitemap-generate.xml"),
    ("CH-TD-03", "taskade", "SEO-Agent 模板", "每个 agent 模板一个页面", "taskade.com/agents/<slug>", "sitemap 实测：3,169 条", "5", "https://www.taskade.com/sitemaps/sitemap-agents.xml"),
    ("CH-TD-04", "taskade", "SEO-自动化模板", "每个自动化配方一个页面", "taskade.com/automate/<slug>", "sitemap 实测：2,361 条", "5", "https://www.taskade.com/sitemaps/sitemap-automate.xml"),
    ("CH-TD-05", "taskade", "SEO-提示词", "每个 prompt 一个页面", "taskade.com/prompts/<slug>", "sitemap 实测：2,205 条", "4", "https://www.taskade.com/sitemaps/sitemap-prompts.xml"),
    ("CH-TD-06", "taskade", "SEO-转换页", "「X 转 Y」", "taskade.com/convert/<slug>", "sitemap 实测：2,118 条", "4", "https://www.taskade.com/sitemaps/sitemap-convert.xml"),
    ("CH-TD-07", "taskade", "SEO-对比页", "「vs Notion/Asana/ClickUp」类", "taskade.com/compare/<slug>", "sitemap 实测：197 条", "5", "https://www.taskade.com/sitemaps/sitemap-compare.xml"),
    ("CH-TD-08", "taskade", "UGC-社区 app", "用户克隆作品生成页面，进 sitemap", "taskade.com/apps/all/<slug>", "sitemap 实测：6,135 条", "3", "https://www.taskade.com/sitemaps/community-apps.xml"),
    ("CH-TD-09", "taskade", "UGC-作者主页", "作者主页也进 sitemap", "taskade.com/@<id>", "sitemap 实测：495 条", "3", "https://www.taskade.com/sitemaps/community-profiles.xml"),
    ("CH-TD-10", "taskade", "GEO / AI 原生发现", "llms.txt + SKILL.md + MCP，让 AI 找到并调用", "taskade.com/llms.txt; /SKILL.md; /mcp", "导航专设 For agents 四项；robots 声明 ai-train=yes", "4", "https://www.taskade.com/agents"),
    ("CH-TD-11", "taskade", "内容博客", "博客做长尾与信任", "taskade.com/blog/<slug>", "sitemap 实测：1,125 条", "3", "https://www.taskade.com/sitemaps/sitemap-blog.xml"),
    ("CH-TD-12", "taskade", "学习中心/文档", "learn/wiki/docs 三层教学资产", "taskade.com/learn|/wiki|/docs", "sitemap：learn 435 / wiki 573 / docs 169", "3", "https://www.taskade.com/sitemaps/sitemap-learn.xml"),
    ("CH-TD-13", "taskade", "GEO-llms.txt", "给 AI 的站点说明书，含 TL;DR、事实、FAQ 与「How to Cite Taskade」指定引用措辞", "taskade.com/llms.txt", "2026-11-18 更新；单文件覆盖全站", "5", "https://www.taskade.com/llms.txt"),
    ("CH-TD-14", "taskade", "GEO-.well-known 元数据", "api-catalog / mcp.json / mcp server-card / agent-skills index / oauth metadata", "taskade.com/.well-known/*", "至少 5 个机器可读端点（llms.txt 末段列出）", "4", "https://www.taskade.com/llms.txt"),
    ("CH-TD-15", "taskade", "GEO-Markdown 出口", "任意页面加 Accept: text/markdown 即返回 Markdown", "任意 taskade.com 页面", "llms.txt 明确说明", "4", "https://www.taskade.com/llms.txt"),
    ("CH-TD-16", "taskade", "UGC-发布 app 自带发现层", "用户发布的每个 app 自动带 robots.txt / sitemap.xml / llms.txt", "your-app.taskade.app", "官方 Publish 说明；每个客户 app 都是发现节点", "5", "https://www.taskade.com/llms.txt"),
    ("CH-TD-17", "taskade", "SEO-替代品页（结构化）", "197 页 compare 里：155 页 free-<竞品>-alternative、33 页纯模型对比、6 页 taskade-vs-*", "taskade.com/compare/free-<competitor>-alternative", "纯吃「免费替代品/模型对比」搜索量，不是品牌对比", "4", "https://www.taskade.com/sitemaps/sitemap-compare.xml"),
]

resources = [
    ("RS-SL-01", "slack", "Slack Marketplace apps", "应用", "需要某个第三方能力（CRM/监控/审批）", "slack.com/marketplace", "直接安装；或照着做自己的 app", "4", "4", "A", "https://slack.com/marketplace"),
    ("RS-SL-02", "slack", "Template gallery", "模板", "不知道一个工作流怎么开始", "slack.com/templates/gallery", "抄一个模板改成自己的流程", "5", "5", "A", "https://slack.com/templates/gallery"),
    ("RS-SL-03", "slack", "Slackbot skills", "Agent", "想让 AI 在频道里执行固定任务", "slack.com/features/slackbot", "把任务写成 skill，挂给 Slackbot", "4", "4", "A", "https://slack.com/features/slackbot"),
    ("RS-SL-04", "slack", "Block Kit", "SDK/组件", "要在对话框里做复杂交互", "docs.slack.dev/block-kit", "用组件拼消息界面", "3", "3", "A", "https://docs.slack.dev/block-kit/"),
    ("RS-SL-05", "slack", "Slack CLI + Bolt", "SDK/工具", "要开发/部署一个 app", "api.slack.com", "用 Bolt 起项目，CLI 管生命周期", "3", "2", "A", "https://api.slack.com"),
    ("RS-SL-06", "slack", "Slack-authorized MCP server", "协议/接口", "要让 agent 读到 Slack 上下文", "slack.com/features/agentic-platform", "授权后把对话数据给 agent 用", "3", "2", "A", "https://slack.com/features/agentic-platform"),
    ("RS-SL-07", "slack", "Real-Time Search API", "接口", "要实时查 Slack 里的信息", "slack.com/features/agentic-platform", "接进自己的 agent/检索", "3", "2", "A", "https://slack.com/features/agentic-platform"),
    ("RS-SL-08", "slack", "Help Center", "文档", "遇到具体操作问题", "slack.com/help", "查文章；也可学它的问题分类做自己的帮助中心", "3", "5", "A", "https://slack.com/help"),
    ("RS-TD-01", "taskade", "Project 模板 3,997", "模板", "某个业务场景不知道怎么搭", "taskade.com/templates", "克隆→改字段→接数据", "5", "5", "A", "https://www.taskade.com/sitemaps/sitemap-templates.xml"),
    ("RS-TD-02", "taskade", "Agent 模板 3,169", "Agent", "要一个能干活的 agent，不想从零配", "taskade.com/agents", "选模板→改提示词/工具/知识", "5", "4", "A", "https://www.taskade.com/sitemaps/sitemap-agents.xml"),
    ("RS-TD-03", "taskade", "自动化模板 2,361", "自动化", "重复流程要自动化", "taskade.com/automate", "克隆配方→换触发与动作", "5", "4", "A", "https://www.taskade.com/sitemaps/sitemap-automate.xml"),
    ("RS-TD-04", "taskade", "社区 app 6,135", "应用", "要一个现成可用的 app", "taskade.com/apps", "克隆→改→用", "4", "4", "A", "https://www.taskade.com/sitemaps/community-apps.xml"),
    ("RS-TD-05", "taskade", "作者主页 495", "身份/案例", "想找某个作者的其他作品", "taskade.com/@<id>", "按作者追作品", "3", "5", "A", "https://www.taskade.com/sitemaps/community-profiles.xml"),
    ("RS-TD-06", "taskade", "Generate 页面 4,526", "工具页", "要按场景直接生成一个结构", "taskade.com/generate", "选场景→生成→改", "4", "4", "A", "https://www.taskade.com/sitemaps/sitemap-generate.xml"),
    ("RS-TD-07", "taskade", "Convert 页面 2,118", "工具页", "要把旧格式转成新结构", "taskade.com/convert", "用现成转换页", "3", "4", "A", "https://www.taskade.com/sitemaps/sitemap-convert.xml"),
    ("RS-TD-08", "taskade", "Prompts 2,205", "提示词", "不知道怎么写指令", "taskade.com/prompts", "抄提示词→改变量", "4", "5", "A", "https://www.taskade.com/sitemaps/sitemap-prompts.xml"),
    ("RS-TD-09", "taskade", "Integrations 173（6 类）", "集成", "要接外部系统", "taskade.com/integrations", "看它接了哪些、怎么分类，照做自己的", "3", "4", "A", "https://www.taskade.com/integrations"),
    ("RS-TD-10", "taskade", "SKILL.md", "协议/文档", "要让 agent 知道怎么用你的产品", "taskade.com/SKILL.md", "照这个格式给自己的产品写一份", "5", "5", "A", "https://www.taskade.com/SKILL.md"),
    ("RS-TD-11", "taskade", "MCP server", "接口", "要让外部 agent 调用你的能力", "taskade.com/mcp", "照它的 MCP 设计自己的", "4", "3", "A", "https://www.taskade.com/mcp"),
    ("RS-TD-12", "taskade", "llms.txt", "协议/文档", "要让 AI 搜索/agent 正确理解你的站", "taskade.com/llms.txt", "给自己的站写一份 llms.txt", "5", "5", "A", "https://www.taskade.com/llms.txt"),
    ("RS-TD-13", "taskade", "App Kit 市场（免费/付费）", "应用/资产", "要一个成品 app，且愿意为它付费", "taskade.com/apps", "克隆→改→用；或照它的打包方式卖自己的成品", "5", "4", "A", "https://www.taskade.com/llms.txt"),
    ("RS-TD-14", "taskade", "公开 Agent 页 + Embed Widget", "Agent/组件", "把 AI 助手挂到自己网站", "Publish → Embed（Bubble/Modal/Sidebar/AskAI/Inline）", "照它的 5 种形态做自己的挂件", "4", "4", "A", "https://www.taskade.com/llms.txt"),
    ("RS-TD-15", "taskade", "TSK 模型阶梯 + TSK-Bench", "模型/基准", "不想被单模型绑死，且要知道哪个模型更适合", "taskade.com/tsk；tsk1.json", "照「按任务路由模型」的思路设计自己的模型层", "4", "3", "A", "https://www.taskade.com/llms.txt"),
    ("RS-TD-16", "taskade", "OpenAPI 规范（v1/v2）", "接口规范", "要让外部系统/agent 稳定调用", "taskade.com/api/documentation/v1|v2/json", "照它的 spec 组织自己的 API", "3", "3", "A", "https://www.taskade.com/llms.txt"),
    ("RS-TD-17", "taskade", "agent-skills 索引（.well-known）", "协议/索引", "要让 agent 发现并安装你的技能", "taskade.com/.well-known/agent-skills/index.json", "给自己的 skills 建一份可发现索引", "5", "5", "A", "https://www.taskade.com/llms.txt"),
]

def write_csv(name, header, rows):
    path = os.path.join(BASE, name)
    # 保护：01 已含历史时不被覆盖；02/03 已含历史（>60 行）时也不覆盖
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8-sig", newline="") as f:
            existing = list(csv.reader(f))
        if name == "01-products.csv" and len(existing) > 3:
            print("skip", name, "（已有", len(existing) - 1, "行，保留现状）")
            return
        if name in ("02-atoms.csv", "03-workflows.csv") and len(existing) > 61:
            print("skip", name, "（已有", len(existing) - 1, "行，保留现状）")
            return
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(list(r))
    print(name, len(rows), "rows")

write_csv("01-products.csv",
          ["no","slug","name","category","one_liner","icp_primary","icp_secondary","jtbd","core_scenarios","ai_mode","pricing_model","free_tier","paid_tiers","atoms_count","workflows_count","primary_channels","moat_hypothesis","evidence_urls","updated_at"],
          [[p[k] for k in ["no","slug","name","category","one_liner","icp_primary","icp_secondary","jtbd","core_scenarios","ai_mode","pricing_model","free_tier","paid_tiers","atoms_count","workflows_count","primary_channels","moat_hypothesis","evidence_urls","updated_at"]] for p in products])

write_csv("02-atoms.csv", ["atom_id","product","atom_name","atom_type","what_it_does","composable_with","evidence_url"], atoms)
write_csv("03-workflows.csv", ["workflow_id","product","workflow_name","input","atoms_used","steps","output","who_uses","evidence_url"], workflows)
write_csv("04-channels.csv", ["channel_id","product","channel_type","mechanics","url_pattern","scale_note","replicable_score","evidence_url"], channels)
write_csv("05-resources.csv", ["resource_id","product","resource_name","resource_type","problem_solved","how_to_access","reuse_form","reuse_score","migration_cost","evidence_strength","evidence_url"], resources)
