# 006 · Claude by Anthropic

> 三方材料：**① 我的真实体验**（2026-11-15 整理，实测原始表 `实测.md`；实用于 2026 年 4 月，网页版，几天后账号被封）｜**② 用户评论**（Product Hunt 1.1K 条，5.0 分；G2 1,907 条，4.7 分）｜**③ 公开材料**（PH 产品页与 48 次发布记录、官网产品矩阵与行业清单、claude.com/pricing 与帮助中心限额说明）
> 规则：事实都有来源；推断标 `[推断]` 或（我的判断）；体验结论只写我实测过的，没测的写没测。

## 〇、AI 类型判定（先判，再写别的）

**结论：AI 原生（AI Native）。**

- **拔电测试**：拿掉 AI，剩下的是一个登录页和一个空输入框——没有模型，这个产品不存在。不是"能看不能用"，也不是"照常卖"，是**根本没有东西可卖**。
- 与 005 HyNote 的差别在这里很关键：HyNote 是"AI 嵌在笔记主干里"（拿走 AI 还能当录音笔），Claude 是**模型本身即产品**。所有功能（聊天、Code、Cowork、Duet、Personal Finance）都是同一个模型能力换壳。
- **类型决定死法**：原生怕上游吞——它自己就是上游，所以它怕的不是被吞，是被**同层追平**（同代模型差距缩到用户感知不到）和**被下游当零件**（Cursor、Lovable 把它的 API 做成别人的产品壳，见 PH 评论原话）。类型与死法对得上：它的护城河只能建在"模型领先 + 协议（MCP）+ 分发渠道"，不能建在交互。

## 一、8 维度速览

| # | 维度 | 一句话结论 | 依据 |
|---|---|---|---|
| D1 | 目标用户 | 官网把用户切成 16 类（金融顾问、政府、医疗、高教、K-12 教师、生命科学、非营利、小企业、科学家、初创、开发者……），真实的第一批付费者却是**写代码的人**——PH 评论里几乎每一条好评都在讲 Claude Code | PH 产品页"可用部门/行业"清单原话；PH 好评 Pros 计数 code generation 78 次，仅次于 AI assistant 111 次 |
| D2 | 核心问题 | 它卖的不是"聊天"，是**判断力外包**：用户要的是"帮我把这件事想清楚并直接做成"，不是"给我一段答案" | PH 评论原话 It pushed back when I was wrong… Claude consistently asked the right question before building the wrong thing；实测（燃冰）T5 原话「省的是能力，它比我强」 |
| D3 | AI 是否不可替代 | 不可替代到残酷：**拿走 AI 产品为零**。因此它没有"AI 赋能"这条路，只有"模型是否领先"这一条命 | 拔电测试（见第〇节）；官网产品矩阵全部围绕同一模型家族（Mythos/Fable、Opus、Sonnet、Haiku） |
| D4 | 工作流整合 | 三层：聊天面（Claude / Cowork / Personal Finance）→ 代码面（Claude Code，CLI + IDE + 桌面）→ 平台面（AWS、Google Cloud、Microsoft Foundry、Managed Agents）。整合点不是界面，是 **MCP 协议** | PH 产品页"可用平台/资源"原话；PH 评论 And because it speaks MCP, my users' agents call my tools through Claude directly — no glue code |
| D5 | 商业模式 | 个人订阅（Free / Pro / Max，本次未取到官方金额）+ 平台按量（云厂商转售）+ 企业合同（按部门/行业销售）。**没有一次买断，也没有永久版** | claude.com/pricing 页面脚注（"Usage limits apply"、"Prices shown don't include applicable tax"）；PH 产品页行业与"Service partners / Claude partner network"入口 |
| D6 | 竞争差异化 | 它自己不说差异化，用户替它说：**"推理在多步难题上不糊弄"+"写得像人"+"MCP 让 agent 直连"**。我的判断：真正的差异化是**协议位**——MCP 让 Claude 从"一个 App"变成"agent 的插座" | PH 评论原话 the reasoning holds up on hard, multi-step problems where other models hand-wave；For writing, … a combination of solid context awareness and just better, more natural writing skills |
| D7 | 成本结构 | 结构性矛盾：**卖定额订阅、付按量推理**。5 小时窗口与技术性限额就是这个矛盾的产物（官方脚注承认 usage limits 生效，并注明 verified 账号不受 5 小时限制） | claude.com/pricing 脚注原话；support.claude.com 帮助文章目录（How does the five-hour limit work? / How do weekly limits work? / How can I get unlimited usage?） |
| D8 | 技术边界 | 边界不在"会不会做"，在**"敢不敢让它自己动手"**：Claude Code 自动编辑能删掉整个数据库，出事后它还会否认（PH 1★ 原话）。能力已到"能执行"，信任还停在"要人盯" | PH 1★ 原话 Opus 4.8 xHigh just deleted my entire database without any logic or prompt to do so… And worse thing is, it denies that it did that；G2 5★ 用户的 dislike 字段同样指向"改一个坏一个" |

## 二、9 字段卡片

| 字段 | 值 |
|---|---|
| 产品 | Claude by Anthropic（Anthropic PBC 出品；PH 评分 5.0 / 1.1K 评论 / 101K 关注） |
| 队列号 / slug | 006 / claude |
| 分类 | AI 对话 / 基础模型（LLM · AI Chatbots） |
| 官网 / 一手页 | https://claude.com ｜ 定价 https://claude.com/pricing ｜ 帮助中心 https://support.claude.com ｜ PH：producthunt.com/products/claude |
| 定价 | **本次未取到官方金额**（定价页为 JS 渲染，抓取只拿到脚注，见 `_raw.md`）。可核实的是结构与规则：页面按档位售卖、脚注写明 Usage limits 生效、"how fast you reach a limit depends on the model you use, how long your chats are, and how large your files are"、5 小时限额存在且 verified 账号不受此限、价格不含税、可随时调整。**不写金额，不猜档位价。** |
| 规模（自述 + 平台） | 可核实：PH 5.0 分 / 1.1K 评论 / 101K 关注 / 48 次发布（最近一次 2026-11-10，Claude Fable 5.2）；G2 4.7 分 / 1,907 条（5 星 85%、4 星 13%）。**官方未在采集页披露 ARR、用户数或付费数**，本卡不编。 |
| AI 能力 | 对话与长文推理、代码生成与重构（Claude Code）、桌面代理（Cowork）、主动代理（Duet）、个人财务问答（Personal Finance，2026-11-07 发布）、MCP 协议直连外部工具、多模态文档产出（docx/pptx/xlsx）、企业侧Security / Science / Tag 等专项产品 |
| 官方「不做」清单 | 不做图像生成（PH 汇总 Cons：limited image output 3；多条评论因此转去 ChatGPT / Banana）；不做企业级人工客服（G2 差评两次点名"非企业客户基本没有支持"）；不承诺单次执行可回滚（1★ 删库案例后官方未见机制披露）；**部分地区不可用**（PH 产品页原话：支持国家部分区域不可用，需联系支持） |
| 实测状态 | **已实测（受限）**。2026 年 4 月用网页版，Gmail 注册后对话可用，几天后账号被封（提示"账号有问题"），T1 改稿次数、T2 误答形态、T3 限额文案均**没测到**。本卡所有体验结论只覆盖实测到的部分，其余标「未测」。 |

## 三、校正后的四栏

- **一句话定位**：**它不是助手，是插座**——模型能力做成订阅卖给你，再用 MCP 把别人的 agent 插上来。
- **核心优势（1 条）**：**多步推理不糊弄**。用户自己给出的证据最硬：solo founder 说"months of daily use… the reasoning holds up on hard, multi-step problems where other models hand-wave"；另一位开发者说"85+ 开发会话，Claude Code 写了 90% 的 Next.js 应用"。实测（燃冰）T5 的说法更短：**省的不是时间，是能力，它比我强**。
- **最大短板（1 条）**：**账号与可用性是第一道墙，而且这道墙比模型能力更早挡住人**。实测（燃冰）4 月网页版用了几天就被封，提示"账号有问题"，全程没有可用的申诉路径；PH 产品页自己写着"部分区域不可用，需联系支持"。**一个 AI 原生产品的最大短板是"你进不去"，这在报告里必须写在最前面。**
- **失效场景**（实测 + 评论证据，四条）：
  1. **账号不在服务区的人**：实测（燃冰）——封号后所有能力归零，"我卡在账号上"。这不是体验问题，是可达性问题。
  2. **要图像的人**：PH 汇总 Cons limited image output 3；评论原话 I still use ChatGPT or Banana for many visual tasks because the image tooling around Claude is not yet strong enough。
  3. **要它扛重活的人**：G2 一位付费超 $600 的用户原话 the project approaches completion, Claude Code attempts to fix one problem, and suddenly something that was already working stops functioning；PH 1★ 更狠——自动编辑删掉整个数据库，且"it denies that it did that"。
  4. **要被当客户对待的人**：G2 差评原话 If you aren't an enterprise customer, good luck getting any support（5 天无回应）；另一条写 billing function does not work… all they can do is allow their chatbot, Fin, to answer you with the same stiff nonsense answer 100 times in a row。

## 四、我的实测（2026-11-15 整理；实际使用发生在 2026 年 4 月，20 分钟实测表）

> 署名：实测（燃冰）。原始记录：`实测.md`。**注意：这份实测是"受限实测"——账号在第 3 天被封，四段里有三段没测完，本卡不替它补结论。**

| 观察项 | 实测结论 |
|---|---|
| 上手用时（TTV） | **5 分钟**（T4 原话：5min，不用先读教程）。路径是 Gmail 注册 → 直接进对话可用，没有引导流程、没有配置项 |
| 哪一步停下来想「下一步该干嘛」 | **没卡在界面上，卡在账号上**（T1 与最后四问第 3 题原话：我卡在账号上） |
| 结果改了几次才敢用 | **没测到**（T1 原话：没测到）。它确实能给出可用结果，但样本不足以说"几次" |
| 最像智能的一刻 | **它主动指出我的问题**：T2 原话——让它把我 GitHub 的项目统统看了一遍，它能很好地指出我的问题。这是"判断力外包"成立的最小证据 |
| T2 边界（矛盾指令 / 黑话） | **部分成立**：主动指出矛盾——有；错的时候是"明显错"还是"通顺地错"——**没测到**；是否提醒核对来源——**空白，未测** |
| 免费与付费的墙 | 墙不是额度提示，是**封号**：T3 原话"直接被封号了，说账号有问题"。免费版够不够日常：不够用，用得很少；它主卖的是**能力**，不是额度、不是席位 |
| 它主卖什么 | **能力**（T3 + T5 一致）：省的是能力不是时间，依据一句话——"它比我强" |
| 会不会留下 | **会，但换形态**：现在用 Claude Code CLI + 其他大模型（T4 后第 4 问原话）。留下的是命令行里的那个它，不是网页里的那个它 |
| 没测的部分 | T1 改稿次数、T2 误答形态与来源提醒、T3 正常限额文案（被封号后无从观察）、图像能力、团队协作、企业支持响应速度——**全部未测，本卡不写结论** |

**实测之外的一条判断**（我的判断）：我原以为它是给"普通人用的聊天工具"（实测第 1 问原话），用完发现真正被它服务的是**已经在写代码、且愿意把判断权交出去的人**。这个偏差不是我用错，而是它的产品叙事（对公众讲"AI 助手"）和它的付费现实（评论里全是 Claude Code）之间本来就有一道缝。**这道缝是它最大的机会，也是它最大的风险：对公众讲得太好，公众进来被限额和封号劝退，口碑由"没付费的人"决定。**

## 五、用户评论证据（原话，未改写）

**Product Hunt（5.0 / 1.1K；采集到 8 条最新 + 2 条 1★ + 1 条 2★）**

| 原话 | 它证明了什么 |
|---|---|
| "the reasoning holds up on hard, multi-step problems where other models hand-wave. Opus for the deep work, Haiku for the fast paths." | D6 的核心优势与模型分层策略，是用户自己讲出来的 |
| "On running my Instagram page alone, I believe it saves me 10+ hours per week" | 价值量化来自用户自述（不是官方数据），可用于说明"省时间"这条叙事对内容工作者成立 |
| "And because it speaks MCP, my users' agents call my tools through Claude directly — no glue code." | MCP 是真实的生态位：它不只是自家功能，是别人的基础设施 |
| "Only real friction is rate/message limits when I'm deep in a long Claude Code session — I'll be mid-flow on a hard refactor and have to pause." | 限额打在"最深的工作流"上，痛感最强（对应 PT 汇总 Cons message limits 28 次） |
| "Context window limits can be frustrating during very long sessions — the conversation gets compressed and some earlier decisions are lost." | 长会话压缩会丢决策，这是 agent 类产品的隐性成本 |
| "Opus 4.8 xHigh just deleted my entire database without any logic or prompt to do so… And worse thing is, it denies that it did that."（1★） | 执行力已到"能破坏"的程度，而可观测性与回滚没跟上——这是它最像"危险工具"的一刻 |
| "Anthropic Support refused to refund the new payment solely because a refund had previously been issued on my account."（1★，UAH 1,075.94 自动续费） | 计费与退款政策是它第二条硬伤级差评线 |
| "a brand new blog… listed 5 high level overused topics… Instead any other (Grok, Gemini, Perplexity) provided right off the bat interesting subtopics"（2★） | 弱场景：需要"给具体、反常识的小众答案"的运营类问题，它会滑向平庸答案 |

**PH 汇总页的 Pros / Cons 计数（抱怨计数就是痛点分布）**：Pros — AI assistant 111、code generation 78、contextual understanding 64、reasoning 57、data analysis 30、fast performance 28、creative writing 27、nuanced responses 23、ethical AI 20、UI 17。Cons — **message limits 28**、typography issues 11、limited image output 3、high cost 3、long context windows 3、agent observability 2、conversation search 2、cross-surface context sharing 1。**解读：它被爱的原因是"会想"，被恨的原因是"不让多用"和"帮不上图像"。**

**G2（4.7 / 1,907；5 星 85%、4 星 13%）**——关键在"连 5 星用户也在 dislike 字段里写的不满"：

| 原话 | 它证明了什么 |
|---|---|
| "If you aren't an enterprise customer, good luck getting any support."（Teams 计划数据是否用于训练的核实，5+ 天无回应） | 支持体系按合同规模分层，个人与小团队被系统性放弃 |
| "The billing function does not work. They give you subscriptions you did not ask for, they then upgrade you with no warning… all they can do is allow their chatbot, Fin" | 计费系统 + 客服外包给机器人，是信任崩塌的两级加速器 |
| "I have spent more than $600… I have not been able to complete a single project successfully."（5 星用户的 dislike） | "改一个坏一个"的循环是 agent 编码的真实失败模式 |
| "It's often quite inaccurate and doesn't follow directions… then Claude block me from using the account for hours"（5 星用户的 dislike） | 失败会**消耗额度**，这是"按次计费 + 需要多轮修错"的结构性摩擦，不是偶发 bug |
| "I dislike that AI is being used for unnecessary surveillance of ordinary people… I have replaced claude with a similar AI service"（1★） | 存在一类用户的迁移动机与产品体验无关，纯价值观——这是模型厂才有的风险 |
| "Sometimes I like a more direct answer and the empathetic responses don't hit the mark."（2★） | 它的人格设定（共情、铺垫）对一部分人是减分项，不是加分项 |

## 六、附录四段摘要

- **16 对标竞品地图**：PH 评论里用户实际点名过的替代品是 ChatGPT（OpenAI）、Gemini（Google）、Codex 3.0、Grok、Perplexity、DeepSeek、Cursor、GitHub Copilot——**它们抢的不是同一个需求**：ChatGPT / Gemini / Grok 抢"通用问答"，Codex / Cursor / Copilot 抢"写代码的那双手"，Perplexity 抢"查资料"，DeepSeek 抢"便宜"。真正抢走 Claude 付费用户的是 **ChatGPT（一位 G2 1★ 用户原话：I had already moved to ChatGPT）** 和 **Codex（PH 评论：I use Codex more for research, content images, and tasks that involve connected tools）**。`[推断]` 名单之外最大的威胁不在名单里：**系统级助手**（操作系统自带的对话入口）与**IDE 内置的 agent**——它们不争品牌，争默认位。
- **17 竞品技术底座**：Claude＝自研前沿模型家族（Mythos/Fable、Opus、Sonnet、Haiku）+ 多云分发（AWS、Google Cloud、Microsoft Foundry、Managed Agents）+ **MCP 协议**（开放给第三方 agent 调用）。ChatGPT＝自研模型 + 自有应用与插件生态；Gemini＝自研模型 + Google 账号与 Workspace 分发；Codex / Cursor / Copilot＝**别人模型的壳 + 极致的编辑器集成**。`[推断]` 护城河结论：真护城河有两层——**模型层（最难，也最容易被追平）** 与 **协议层（MCP，最容易被采纳，也最难被独占）**；壳层（界面、人格、模板）没有护城河，这正是它相对 Cursor 类产品的处境反过来的地方。
- **18 可迁移的机会（我的判断）**：① **把"能不能用"变成产品功能**——区域可用性与账号申诉做成透明通道（实测（燃冰）卡死在这里，而官网自己写着"部分区域不可用"）；② **把限额做成可见预算**——28 次抱怨指向同一件事：用户不知道还剩多少、什么时候撞墙；把"还能问几次"提前显示，是低成本、高感知的一改；③ **给自动执行加"预演 + 回滚"**——1★ 删库案例说明 agent 已能破坏，产品还没给出刹车；这一条最重，也最难被别人抄（需要模型层配合）。**哪个最轻？②，一周能上，直接吃掉最大一条抱怨。**
- **19 流量与变现拆解**：钱从三方兜里出——个人（订阅，按定额卖）／开发者与企业（平台按量，经云厂商转售）／大客户（合同 + 席位 + 专项产品）。凭什么它拿到：模型领先带来的**开发者口碑扩散**（PH 48 次发布、G2 1,907 条、评论里"我朋友都在用"式的自发推荐）+ **企业渠道**（Service partners、Claude partner network、Claude Academy）+ **协议位**（MCP 让别人的产品必须接它）。流量吃的是**爆款**（每次模型发布都是一次全球性上新，2026-11-10 Fable 5.2 就是最近一次），不是长尾。变现三层：**订阅（广度）→ 平台按量（深度）→ 企业合同（厚度）**。**最脆的一根梁是订阅层的毛利**：定额收费 + 按量成本，用户越重度、推理越贵，限额就必须越紧；限额一紧，抱怨就上来（message limits 28 次，占全部 Cons 的第一位）。

## 附：证据索引

- 采集原文：`_raw.md`（PH 产品页：5.0 / 1.1K / 101K 关注 / 48 次发布 / 四条最新发布记录 / 16 类行业与部门 / 平台与合作伙伴入口 / 官网语言仅 English / 部分区域不可用）
- 评论：`claude-评论.md`（PH 8 条最新 + 1★ 2 条 + 2★ 1 条 + Pros/Cons 计数）｜`claude-G2评论.md`（G2 4.7 / 1,907 条，Lowest Rated 排序 10 条差评，含 5 星用户的 dislike 字段）
- 官方页：https://claude.com/pricing（只取到脚注：Usage limits 生效、5 小时限额、verified 账号例外、价格不含税、可随时调整）｜https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work（限额机制文章目录，正文本次未取到金额与细节）
- 实测：`实测.md`（2026-11-15 归档；实际使用 2026 年 4 月，网页版，账号数日后被封；署名 实测（燃冰））
- 渲染产物：`teardown-zh.html` / `teardown-en.html`（由 `content.json` 生成）

---
> 本卡所有事实均可在上述来源中逐条核对；凡推断已标 `[推断]` 或（我的判断）；实测结论均标注「实测（燃冰）」，未测项目明确写「未测」；定价金额因抓取失败**不写数字**，不猜、不补。
