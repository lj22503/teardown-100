# 模板解剖：这些模板里到底有哪些模块

> 用途：不用点开 URL 也能知道一个模板由哪些模块组成；决定参考哪个之后，再点最后的链接。
> 覆盖：013 Slack / 014 Taskade / 007 Framer（历史期里公开了 What's inside 的模板）。

## slack · Project Management Template

1. Project overview（文档/Canvas）
2. Task tracker（列表/List）
3. Weekly check-in（工作流）
4. Item status notification（工作流）
5. Welcome message（工作流）

模板页：https://slack.com/templates/project-management-starter-kit

## slack · Feedback Intake & Triage

1. Feedback instructions（模块）
2. Feedback tracker（列表/List）
3. Feedback form（表单）
4. Item status notification（工作流）

模板页：https://slack.com/templates/feedback-intake-triage

## slack · New Hire Onboarding

1. Onboarding guide（文档/Canvas）
2. First week to-dos（模块）
3. Join team channels（模块）

模板页：https://slack.com/templates/new-hire-onboarding

## slack · Marketing Campaign Starter Kit

1. Campaign overview（文档/Canvas）
2. Campaign tracker（列表/List）
3. Welcome message（工作流）

模板页：https://slack.com/templates/marketing-campaign-starter-kit

## slack · External Partner Starter Kit

1. Key documents（文档/Canvas）
2. Project tracker（列表/List）
3. Item in-progress notification（工作流）
4. Completed item notification（工作流）

模板页：https://slack.com/templates/external-partner-starter-kit

## slack · Sales Deal Tracking

1. Deal tracker（列表/List）
2. Deal won notification（列表/List）

模板页：https://slack.com/templates/sales-deal-tracking

## taskade · web-app-bug-tracker

**一句话**：Bug tracker for SaaS and web product teams with AI severity scoring, GitHub PR sync, browser/OS field tracking, and regression search across past releases.

**组合**：4 projects / 1 agent / 3 automations

1. Bug Intake Form（表单）：Browser, OS, URL, repro steps, screenshot upload, and customer impact captured upfront
2. Triage Board（视图/看板）：Pipeline from New → Triaged → In Progress → In Review → Fixed → Verified on a [Board view](https://www.taskade.com/learn/projects/project-views)
3. Triage Agent（Agent）：[AI agent](https://www.taskade.com/learn/agents/custom-agents) reads bug reports, scores severity (P0-P3), deduplicates against past bugs, and suggests owners based on git blame
4. GitHub Sync（集成/同步）：Commits referencing the bug ID update status automatically; PR merge moves the bug to "In Review"
5. Release Notes Generator（生成/报告）：Each release auto-generates customer-facing release notes from the verified bugs

模板页：https://www.taskade.com/templates/bug-tracker/web-app-bug-tracker

## taskade · agency-client-onboarding

**一句话**：Branded onboarding workspace for marketing, creative, and consulting agencies. Walk every new account from signed SOW to first deliverable with intake forms and AI-drafted welcome plans.

**组合**：4 projects / 2 agent / 3 automations

1. Client Intake Form（表单）：Goals, brand assets, key stakeholders, and access credentials captured in one form
2. Kickoff Checklist（模块）：Discovery call agenda, contract acknowledgment, and asset handoff tasks
3. Milestone Tracker（模块）：Stages from Contract Signed → Kickoff → First Deliverable → 30-Day Review on a [Board view](https://www.taskade.com/learn/projects/project-views)
4. Welcome Plan Agent（Agent）：[AI agent](https://www.taskade.com/learn/agents/custom-agents) reads the intake form and drafts a personalized 30-day onboarding plan in seconds
5. Status Automation（自动化）：When a milestone moves to "At Risk," an [automation](https://www.taskade.com/learn/automation/triggers) DMs the account lead in Slack with context

模板页：https://www.taskade.com/templates/client-onboarding/agency-client-onboarding

## taskade · saas-marketing-plan

**一句话**：B2B SaaS marketing plan with demand-gen funnel, content + paid + email mix, AI agent that allocates budget across channels based on past CAC, and pipeline-attribution dashboard.

**组合**：4 projects / 1 agent / 3 automations

1. Funnel Plan（模块）：Awareness → Interest → Consideration → Decision → Customer with content and tactics per stage
2. Channel Mix（模块）：Content, paid (Google/Meta/LinkedIn), email, events, partnerships — with budget per channel
3. Budget Allocation Agent（Agent）：[AI agent](https://www.taskade.com/learn/agents/custom-agents) reads past CAC and conversion data, recommends budget shifts toward channels driving lowest CAC
4. Campaign Calendar（视图/看板）：[Calendar view](https://www.taskade.com/learn/projects/project-views) of upcoming campaigns by channel
5. Pipeline Attribution（视图/看板）：GA4 + CRM sync ties marketing-sourced pipeline back to specific campaigns

模板页：https://www.taskade.com/templates/marketing-plan/saas-marketing-plan

## taskade · saas-product-roadmap

**一句话**：B2B SaaS roadmap with theme-based prioritization, AI agent that clusters user feedback, Linear/Jira sync, customer-facing changelog, and quarterly OKR alignment.

**组合**：5 projects / 1 agent / 4 automations

1. Theme-Based Roadmap（模块）：[Board view](https://www.taskade.com/learn/projects/project-views) with Now / Next / Later columns, themes mapped to OKRs
2. User Feedback Database（模块）：Support tickets, sales asks, NPS comments, and user interview themes consolidated in one [Table view](https://www.taskade.com/learn/projects/project-views)
3. Theme Clustering Agent（Agent）：[AI agent](https://www.taskade.com/learn/agents/custom-agents) reads incoming user feedback weekly and clusters into emerging themes — 5-8 patterns surfacing across the cohort
4. Linear/Jira Sync（集成/同步）：Roadmap themes auto-create epics in Linear or Jira; engineering progress flows back to the roadmap
5. Customer-Facing Changelog（模块）：Themes shipped publish to a public changelog with a [public Genesis app](https://www.taskade.com/learn/genesis/faq)

模板页：https://www.taskade.com/templates/product-roadmap/saas-product-roadmap

## taskade · ai-crm-dashboard-template

**一句话**：Run every lead, deal, and follow-up from one live dashboard that tells you where the quarter actually stands before anyone has to ask for a pipeline update.

**组合**：4 projects / 2 agent / 2 automations

1. Lead capture（模块）：Name, company, source, owner, and first-touch date on one row — add leads by form, import, or paste
2. Stage pipeline（视图/看板）：Lead → Qualified → Proposal → Negotiation → Closed on a [Board view](https://www.taskade.com/learn/projects/board-view) you drag
3. Deal-value rollups（模块）：Weighted pipeline value by stage and by owner, recalculated as cards move
4. Follow-up automation（自动化）：[Triggers](https://www.taskade.com/learn/automation/triggers) fire a reminder when a deal sits past its stage limit
5. AI deal agent（Agent）：A [custom agent](https://www.taskade.com/learn/agents/custom-agents) scores new leads, drafts the follow-up, and flags deals going quiet
6. Multiple project views（视图/看板）：List, Board, Calendar, Table, Mind Map, Gantt, and Org Chart over the same records

模板页：https://www.taskade.com/templates/sales/ai-crm-dashboard-template

## taskade · app-data-model

**一句话**：Clone a structured app data model template with connected records, decision views, an AI review agent, and practical automation hooks.

1. Structured memory（模块）：Track entities, fields, relationships, required values, owners, and validation notes.
2. Decision views（视图/看板）：Use a table for fields, a relationship map, and a review queue for unresolved decisions.
3. AI assistance（模块）：An agent reviews the model for missing entities, duplicate fields, and unclear ownership.
4. Execution（模块）：Automation flags incomplete records and routes model changes to the right reviewer.

模板页：https://www.taskade.com/templates/operations-intelligence/app-data-model

## framer · Brevio

**一句话**：设计师/开发者/创意自由职业者的一页作品集，用来展示作品并接单

**组合**：6 个模块

1. Home 页面（界面）：hero + work + services + process + toolkit + testimonials + pricing + FAQ 八个区块
2. CMS 作品区（工具）：CMS 驱动的作品区，每个案例有独立详情页
3. 作品归档页（界面）：Dedicated work archive page
4. 联系表单（工具）：含 location 字段的 contact form
5. 响应式适配（界面）：desktop / tablet / mobile 三端
6. 动效（界面）：Smooth scroll 与入场动画

模板页：https://www.framer.com/marketplace/templates/brevio/

## framer · Tearsheet

**一句话**：独立设计师与小工作室的单页作品集，项目在页内展开

**组合**：8 个模块

1. Remix 项目（分发）：一个 remix 链接；demo 站就是同一个项目
2. 页面结构（界面）：Home + 7 个 CMS 案例页 + 404
3. 项目行（页内展开）（界面）：点击一行就地展开案例；首条默认展开；每条有 /#work-<slug> 深链
4. 复制链接（工具）：复制项目深链并提示 "Link copied"，剪贴板被拦时给出可选文本
5. 自适应 Hero 字号（界面）：名字按宽度自动缩放，长名字也不溢出
6. About / Services / Experience / 两条证言（界面）：个人介绍与信任块
7. 联系（复制邮箱 + 表单）（工具）：邮箱点击即复制；表单字段 name/email/project type/timeline/message，走 Framer 内置提交
8. CMS 字段（19 个）（工具）：Title/Folio/Client/Discipline/Year/Role/Timeline/Cover/Image 2/Image 3/Share Image/Brief/What I Did/Result/Metric Value/Metric Label/Live Link/Open First/Order/Body

模板页：https://www.framer.com/marketplace/templates/tearsheet/

## framer · Asher Vale

**一句话**：面向设计师与创意人的作品集模板，强调「几小时上线」

**组合**：5 个模块

1. 作品集页面（界面）：引导访客走完「你是谁—做过什么—为什么选你」的叙事
2. 项目展示（界面）：项目以干净布局呈现，突出作品本身
3. CMS 项目（工具）：用 Framer CMS 管理项目，便于持续更新
4. 排版与交互（界面）：克制的排版与细致的交互，注意力留在作品上
5. 转化路径（界面）：每页都为「潜在客户/雇主走下一步」设计

模板页：https://www.framer.com/marketplace/templates/asher-vale/

## figma · Free Figma UI kit and design system

**一句话**：一套可直接用的 UI kit + 设计系统底子

**组合**：3 个模块

1. Design tokens（工具）：颜色/字体/间距/阴影四类 token
2. 可访问组件（工具）：带 default/hover/focus/error/disabled 状态的组件
3. 布局模式（界面）：支撑迭代与扩展的 layout patterns

模板页：https://www.figma.com/community/file/1512527544070386427/free-figma-ui-kit-and-design-system

## figma · Media Dashboard

**一句话**：内容/社媒团队的可编辑数据看板

**组合**：4 个模块

1. 可编辑 Figma 文件（工具）：整套文件可改，非只读稿
2. 响应式布局（界面）：Clean, responsive layout
3. 核心指标与图表（界面）：Key media metrics, charts
4. 内容表格（界面）：Content tables

模板页：https://www.figma.com/community/file/1537877734913818740/media-dashboard

## figma · Ventixe 活动管理后台

**一句话**：活动组织者/票务平台/场馆的活动管理后台

**组合**：7 个模块

1. Dashboard（界面）：总览页
2. Bookings（界面）：预订
3. E-Voucher（界面）：电子凭证
4. Invoices（界面）：发票
5. Inbox（界面）：消息
6. Calendar（界面）：日历
7. Events（Grid）（界面）：活动网格

模板页：https://www.figma.com/community/file/1482921791678828657/ventixe-event-management-admin-dashboard-ui-design

## figma · Match – 约会 App UI Kit

**一句话**：约会/社交产品的完整 UI kit 与设计系统

**组合**：55+ 屏 / 6 组模块

1. 55+ 屏（亮/暗）（界面）：light + dark 两套，40+/55+ 屏
2. 模块化设计系统（工具）：variables / components / tokens / auto-layout
3. 匹配与聊天（界面）：smart match cards、chat UI、profile insights
4. Onboarding（界面）：目标与兴趣选择流程
5. 安全与信任（界面）：verified badge、safe chat、block/report
6. 个人资料构建（界面）：editable prompts、lifestyle tags、photos

模板页：https://www.figma.com/community/file/1523609597252271295

## figma · Material 3 Expressive（设计系统）

**一句话**：把 Google M3 Expressive 指南做成可交互 Figma 系统

**组合**：463 tokens / 75 组件集

1. 463 variable tokens（工具）：6 种颜色模式（亮/暗/中/高对比）+ Web/Android/iOS 代码语法
2. 75 组件集（工具）：3,200+ variants、9,600+ spring-based interactions
3. 35 个 Expressive 形状（界面）：几何参数从 Android 移植
4. 151 图标 + 30 文字样式（界面）：Material Symbols 图标与 text styles
5. 文档 + 可玩原型（知识）：每个组件有文档，整套可交互原型

模板页：https://www.figma.com/community/file/1695747533279107617
