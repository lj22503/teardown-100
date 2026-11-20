# 010 篇 Fathom

> 三方材料：**① 我的真实体验**（2026-11-19，20 分钟实测表 `实测.md`，署名实测（燃冰））｜**② 用户评论**（Product Hunt 产品页元数据抓到 316 条评论总数、8 条最新原话；G2 抓到 4.6 分 / 177 条，但**该页主体是另一个同名财务分析产品**，只有 1 条与会议记录相关，见第五节）｜**③ 公开材料**（fathom.ai 官网原文、fathom.ai/pricing 个人 2 档 + 团队 3 档、Superhuman 官方收购公告、Fireflies 定价页）
> 规则：事实都有来源；推断标 `[推断]` 或（我的判断）；体验结论只写我实测过的，没测的写没测。

## 〇、AI 类型判定（先判，再写别的）

**结论：原生（AI-native），但不是"整机原生"，是"记录壳 + AI 脑"两段式。**

- **拔电测试**：拿走 ASR 与摘要，剩下的是一段录音和一堆会议日历条目——**能录不能读**，转写与摘要一空，产品就退化成录音笔。所以判为原生，不是嵌入型。
- 我实测时的原话是：它有两部分，一部分是会议记录，一部分是 AI 识别和上下文决策判断——**判断权在 AI 那半边**。这也是它和 009 Figma 的区别：Figma 拔电照常干活，Fathom 拔电只剩音频文件。
- **类型决定死法**：原生型的风险不在"被套件集成"，而在"**上游模型与平台把这件事做成免费默认**"。Google Meet 的 Gemini、Zoom 的 AI Companion、Teams 的 Copilot 都是平台自己长出来的同一件事；Fathom 的反手是 bot-free + 免费档 + 跨会议检索（Ask Fathom / MCP），也就是把"平台内一条会议"变成"跨平台全部会议的记忆"。这是它唯一不被平台吞掉的位置。

## 一、8 维度速览

| # | 维度 | 一句话结论 | 依据 |
|---|---|---|---|
| D1 | 目标用户 | 三层人同时收：**个人重度开会者**（销售、教练、顾问、招聘）、**销售与客服团队**（要 CRM 与 Coaching）、**企业**（要 HIPAA / SSO / 自定义留存）；官网 Solutions 按岗位切了六个 | 官网 Solutions：Sales / Customer Success / Marketing / Operations / HR & Talent / Product & Engineering；实测（燃冰）是个人层 |
| D2 | 核心问题 | 卖的不是"转写"，是**"会开完，纪要、行动项、跟进邮件已经在那儿了"**：省掉的是会后那半小时，以及会中不敢分神的那部分注意力 | 官方一句：Fathom summarizes your meetings so you can focus on the conversation；实测：以前至少半小时，现在会议中就能记录反馈 |
| D3 | AI 是否不可替代 | **不可替代**，但不可替代的是"识别 + 提炼"这一层，不是"记录"这一层 | 拔电测试（见 〇）；实测三问原话：它的门槛在语言识别准确度 |
| D4 | 工作流整合 | 一条链：**会前授权（日历/邮箱/会议工具）→ 会中采集（bot 或 bot-free）→ 会后摘要 + 行动项 → 推进 CRM / Slack / Notion / Asana → 进 ChatGPT 与 Claude 查历史** | 官网：Works where you meet（Meet / Zoom / Teams / Gmail / Slack / Asana）+ Integrations（Salesforce、HubSpot、Asana、Zapier、Public API & MCP、ChatGPT、Claude） |
| D5 | 商业模式 | **个人订阅 + 团队按席位订阅 + 合规档加价**，三层叠，免费档极厚（无限录制与转写） | 定价页：Free $0 / Premium 16；Team 15 / Business 25 / Enterprise 35（每人每月，2 人起，Enterprise 仅年付，年付省 25%+） |
| D6 | 竞争差异化 | 差异化不在模型，在**"免费档厚到不像免费" + bot-free 采集 + 跨会议检索与 MCP** 三件；但同质化程度高 | 评论原话：free plan is genuinely generous；bot-free option removes the awkward "is someone else joining?" moment；MCP 与 Claude 集成 |
| D7 | 成本结构 | 结构性张力：**卖订阅、按分钟付 ASR 与推理**，所以免费档必须靠"无限录制"换增长，靠团队席位与企业合规赚钱 | 定价页免费档写 unlimited recordings + transcriptions；官网自述 500K+ companies——用户基数大、单用户毛利靠档位抬 |
| D8 | 技术边界 | 边界在**采集入口与语言识别**，不在摘要：bot 能不能进会、系统音频能不能抓、中文多人抢话准不准 | 实测：门槛在语言识别准确度；评论 Cons 里 bot joining meetings 是唯一被点名的采集反感项 |

## 二、9 字段卡片

| 字段 | 值 |
|---|---|
| 产品 | Fathom（官网自述 Fathom AI Notetaker - Never Take Notes Again） |
| 队列号 / slug | 010 / fathom（进度一律以 `daily.py next` 为准，本篇 RESULT 为 no=10 name=Fathom state=need_report） |
| 分类 | AI 会议记录 / 会议智能（ai-meeting-notetakers） |
| 官网 / 一手页 | https://www.fathom.ai ｜ 定价 https://www.fathom.ai/pricing ｜ 收购公告 https://blog.superhuman.com/superhuman-acquires-fathom/ ｜ PH 产品页 https://www.producthunt.com/products/fathom |
| 定价 | **本次直接抓的是官方定价页原文（每人每月，年付省 25%+）**：个人 Free $0（无限录制、无限转写、即时摘要、clips / playlists / 跨通话搜索；bot 或 bot-free 可选）、Premium $16（加高级摘要、AI 行动项、对话式会议助手、自定义 bot）。团队 2 人起：Team $15（含 Premium + 共享工作区、Trackers、团队级 Ask Fathom、团队安全控制、标准 BAA 的 HIPAA）、Business $25（加 CRM 字段同步、Deal View、Coaching 指标与 AI Scorecards、自定义摘要）、Enterprise $35（仅年付；加 Launch Assist 实施、SSO 与 SCIM、自定义数据留存、可申请自定义 BAA、优先 SLA 与专属成功经理）。全部档位写 90 day guarantee。 |
| 规模（自述 + 平台） | 官网自述 **Used at 500K+ companies**（公司数，不是用户数，口径按官网原文）；官网三个自述数字：95% 用户称能全程在场、每人每周省 6+ 小时跟进工作、从会议洞察到行动 3X 更快——**均为厂商口径，无第三方核实**。Product Hunt 产品页 316 条评论（本次只抓到汇总计数与 8 条最新原话，1–2 星 0 条）；G2 4.6 / 177（5 星 79%、4 星 19%、3 星 1%，但见第五节的数据污染说明）。官方未披露 ARR、付费席位与留存，本卡不编。 |
| AI 能力 | 转写（ASR）+ 即时摘要 + AI 行动项 + AI 跟进邮件 + Trackers（自动盯关键话题）+ Ask Fathom（跨会议问答）+ AI Scorecards（销售教练）+ CRM 字段同步 + 自定义摘要模板 + Public API 与 MCP（接 ChatGPT、Claude） |
| 官方「不做」清单 | 不做会后人工代写（就是替代它）；不做通用知识库/文档协作（只做会议这一层，往外靠集成）；不做硬件与会议室设备；不做开源与私有化部署；不做销售 CRM 本体（同步进别人的 CRM） |
| 实测状态 | **已实测（20 分钟，2026-11-19）**。走完 `注册授权 → 接会议工具 → 一场会 → 看能不能用 → 判错得起吗` 一圈，六维有记录。**未测**：真实秒表计时、中英混说多人抢话的准确率量化、团队协作与 CRM 同步、企业合规配置、MCP 实调——全部未测，本卡不写结论、不编评分。 |

## 三、校正后的四栏

- **一句话定位**：**它不是"会议记录工具"，是"会议的下游工厂"**——把一段对话压成三样能直接用的东西：纪要、行动项、跟进邮件。
- **核心优势（3 条）**：
  1. **免费档厚到不像免费**。无限录制、无限转写、即时摘要都在 $0 档；评论里至少两条独立原话在说这件事（原话：I was actually confused with the features that they offered me for free；另一条说我几乎担心他们给太多了）。这是它最锋利的获客武器，也是它最脆的变现梁。
  2. **bot-free 采集把社交摩擦删掉了**。会里没有第三方机器人，就没有"还有别人加入吗"那 30 秒尴尬（原话：removes the awkward "is someone else joining?" moment that always derailed the first 30 seconds）；实测的安装方式也是浏览器打开、支持插件，不逼你装重客户端。
  3. **把"一场会"变成"可查询的全部会议"**。Ask Fathom + Trackers + MCP 让 Claude / ChatGPT 能直接读会议数据（原话：query insights across all my sales conversations, without copy-pasting transcripts）。这一步把它从"记录工具"推到"记忆层"。
- **最大短板（2 条）**：
  1. **同质化极重，且敌人是平台本身**。官网自己列了七个对手（Fireflies、Granola、Gong、Otter、Read AI、ZoomMate、Google Meet 的 Gemini），其中 Gemini 与 Teams Copilot 是"开会时本来就在那儿"的免费默认。会议记录这件事正在变成平台功能，不是独立品类。
  2. **免费太强导致"升级理由"要另找**。评论里那条给出"Pro 试用两周后降回免费，价值大幅下降"的反馈（原文：the value diminishes greatly）就是反面：当免费档已经够用，付费只能卖团队协作、CRM 同步与合规——这三样恰好是个人用不到的。
- **失效场景（实测 + 评论证据，4 条）**：
  1. **中文为主、多人抢话的会**：实测的门槛结论就落在语言识别准确度上，识别不稳，后面全歪。
  2. **销售决策会**：实测结论是错不起——纪要写错一个承诺，下游跟着返工，且这类错不可逆。
  3. **不许第三方进会的客户**：bot 入会是唯一被点名的采集反感项（评论 Cons：bot joining meetings）。
  4. **手机与线下场景**：官方有 iOS App，但评论里仍有明确诉求（希望接原生 iPhone 通话、方便上传电话录音），说明这一段还没闭环。

## 四、我的实测（2026-11-19，20 分钟）

> 署名：实测（燃冰）。原始记录：`实测.md`（来源：`D:\ObsidianVault\03-Resources\product sense\01-拆解\010-fathom.md`）。**本卡所有体验结论只来自这一份记录；没测的一律写未测。**

| 观察项 | 实测结论 |
|---|---|
| 上手用时（TTV） | **未计时**。记录只写"landing page 上就展示了它能干什么"，没做秒表，本卡不换算成分钟。 |
| 哪一步停下来想「下一步该干嘛」 | **不是界面，是授权**：它在下下载之前就让你注册，一步步授权会议相关的邮箱与会议软件，最后一步才下载 app。流程顺，但这一步是"先交权限、后见产品"。 |
| 结果改了几次才敢用 | **能直接用**；如果要改，改的是「会议共识和行动清单」这一类内容，不是格式。 |
| 最像智能的一刻 | **它把下一步行动提炼出来、再让人确认**（原话：会议的下一步行动她也会提炼然后让人确认）。这是"AI 干活、人签字"的正确姿势。 |
| 它不管的部分 | **前提错了它不纠**：它只如实记录会议、按会议给结果；给错前提它顺着走，兜底靠人工确认。 |
| 出错怎么退 | 有历史记录、能回听；但结论是**错不起**——"这种一边谈话一边形成销售决策的，错不起"。退得回文件，退不回已经说出口的决策。 |
| 免费与付费的墙 | 付费墙在**团队协作、CRM 字段同步、Coaching 与合规**上；个人层免费档已经够用（实测原话：免费就很强大了，而且提供了丰富的 API 和 AI 接入支持）。 |
| AI 类型备注 | **原生**（我填的判定，不是官方说法）：一半是记录，一半是 AI 识别与上下文判断 |

**三个必答结论**：值不值这个价——**值**，因为省的是记录时间，而记录在免费档就已经免费；门槛在模型还是在别处——**在模型这一侧**，具体是语言识别准确度（实测原话），不是界面也不是分发；会不会留下——**会**，而且我的下一步想法是看能不能迁到中文场景、有没有同类竞品。

## 五、评论证据

**Product Hunt（直接抓取元数据 + 8 条最新原话）**：总评论 316 条。AI 汇总的抱怨计数就是痛点分布，**总共只有 10 条抱怨**：bot joining meetings（1）、connectivity issues（1）、ease of use（3）、no mobile app（3）、limited free plan features（2）。夸的计数是另一种量级：AI summaries（102）、meeting recording（85）、automatic transcription（73）、ease of use（58）、action items（56）。

**G2（必须如实说）**：4.6 分 / 177 条，分布 5 星 79%、4 星 19%、3 星 1%。但**这一页的主体是另一个同名产品**——做 Xero / QuickBooks 财务报告与预算的 Fathom，差评原话全是多币种合并、预算、报表定制。会议记录版的 Fathom 在抓到的最差评里只出现 1 条（原话：This tool takes notes from the meetings in a very useful way so you can concentrate on the meeting fully）。**所以本卡不拿 G2 的财务版差评充当会议记录版的痛点证据**，只记录这个数据污染本身。

**归纳四类真实抱怨（全部来自 PH 原话，不做外推）**：

1. **免费档太强的反作用**：Pro 两周试用到期后降回免费，"价值大幅下降"，后来换去别家 note taker；同时也抱怨"它想加入我所有的通话，而我从里面拿不到价值"。
2. **会中体验的笨重**：界面 clunky，希望音视频能弹出到单独屏幕、转写能单独放到另一块显示器——重度用户（两小时会）会撞到这条。
3. **采集方式的社交成本**：bot 入会是 cons 里唯一被点名的反感项（1 条），也正是 bot-free 存在的理由。
4. **移动与电话场景缺口**：no mobile app（3 条），原话希望"接原生 iPhone 通话或至少方便上传电话录音"。

**读法**：316 条评论里抱怨只有 10 条，这在一个同质化严重的品类里属于异常干净的口碑——说明**产品层已经过关**，剩下的分歧全在"免费给太多，为什么还要付钱"。

## 六、应用层六维（必答）

| # | 维度 | 结论与证据 |
|---|---|---|
| 1 | 替掉哪一步 | 替掉的是"会后写纪要 + 发邮件备案"这一段：原来人做，至少半小时，会议内容还没法直接转成行动；现在会中就记录，会后摘要与行动项已经在（实测原话）。钱从人工时间变成 $0 起（免费档）= 值。 |
| 2 | 脏活谁干 | 它啃掉转写、摘要、行动项、跟进邮件、CRM 回写；**甩回一次**——让你把常用会议工具授权接进来（实测原话：她需要我补充接入我常用的会议工具），以及行动项要人确认。这道授权不是它的偷懒，是这个品类的准入门槛：不接会议，就没有音频。 |
| 3 | 出来能不能用 | **能直接用**。要改就改"会议共识和行动清单"这一类事实与判断，不改格式；团队场景里确实有人拿它直接对外发（实测原话：有，她本身主推团队使用）。 |
| 4 | 错了怎么兜 | 兜底薄：它只如实记录会议、按会议给结果，没有来源标注、没有置信度；给错前提它顺着走；真正兜底的是**人工复核**（实测原话：人工确认）。 |
| 5 | 错一次多贵 | **错不起**。有历史记录、能回听（可撤回），但对"一边谈一边形成销售决策"的会，错误的行动项会把下游带歪，且话已经说出口——不可逆（实测原话）。 |
| 6 | 不用它的替代 | 别的免费会议记录工具顶上，差在识别稳定性（实测原话）；但对时效与成交要求高的团队**换不掉**，因为免费档已经足够好、越用功能越多。 |

## 七、附录四段

1. **对标竞品地图**：Fathom 官网自己列了七个对手（Fireflies、Granola、Gong、Otter、Read AI、ZoomMate、Google Meet 的 Gemini）+ "内置方案"一类。真正的三层夹击：**同类独立工具**（Fireflies 价格更低、100+ 语言；Otter 自研 ASR；Granola 主打无 bot 本地采集）、**平台原生**（Meet 的 Gemini、Teams 的 Copilot、Zoom 的 AI Companion——开会时本来就在那儿，边际成本为零）、**收入智能层**（Gong 往销售管理走，Fathom 用 Business 档的 Scorecard 与 Deal View 正面对上）。用户实际跑去哪：评论里那条离开的人说是" bounced around to other note takers"，没点名——**PH 与 G2 都未给出可核实的迁移去向，此处不编**。
2. **竞品技术底座**：Fathom 是 ASR + LLM 摘要 + 会议平台接入（日历、会议 SDK、bot 入会、Mac 端 bot-free 系统音频）+ 检索层（Ask Fathom）+ MCP/API 出口；接缝在"会议平台让不让进"。Fireflies 是 bot 入会 + 100+ 语言 + AskFred + 私有存储与 ISO 42001（官方定价页原文）；Otter 自研 ASR 起家；Granola 走本地系统音频、无 bot（本次定价页为 JS 渲染，**未读到可引用的价格原文**）；平台原生方案直接长在会议软件里，不需要采集权限——**这是结构性优势**。`[推断]` 真护城河不在 ASR 模型，在"跨平台采集权限 + 历史会议数据留存 + 团队工作流嵌入"三件；ASR 本身会被追平。
3. **可迁移的机会（我的判断）**：①**会前授权引导**——实测最值得抄的一点：先注册、逐步授权邮箱与会议工具、最后才下载 app，把"权限"变成上手流程的一部分（最轻，纯流程设计）；②**中文多人抢话的识别稳定性**——实测认定的门槛就在这儿，这恰好是国产会议软件生态的缺口；③**bot-free 采集**在中国会议软件（腾讯会议、飞书、钉钉）里基本空白，本地音频 + 桌面端是更现实的路；④**会议 → 行动 → CRM** 的闭环，对销售团队是刚需，对一人公司是过度设计。哪个最轻？第 1 个，一次改 onboarding。哪个最值？第 2 个，因为它是这个品类的地基。
4. **流量与变现拆解**：钱从三层人兜里出——个人（$16）、团队席位（$15 / $25）、企业合规（$35，仅年付）。套利三问：**钱从谁的兜里出**——会议密度高的人与团队，本质是替掉"专职写纪要的人"那份工时；**还能拿多久**——窗口在收窄，平台原生（Gemini / Copilot / AI Companion）正在把这件事变成免费默认；**凭什么你拿到**——靠免费档先占住个人、bot-free 解掉社交摩擦、再用 MCP 与集成把会议数据变成可查询资产。流量吃两段：长尾靠 **七张竞品对比页 + 集成目录 + Solutions 岗位页**的 SEO 矩阵（官网 Competitors 导航就是证据），爆款靠 Product Hunt（316 条评论）与 Superhuman 收购的媒体曝光。变现三层：**个人订阅（广度）→ 团队席位（厚度）→ 企业合规与实施（深度，Launch Assist、SSO/SCIM、自定义 BAA）**。最脆的梁：**免费档太强**——评论里已经有人说"几乎担心他们给太多"，而付费理由集中在个人用不到的团队与合规功能上；再叠一层风险：2026-04-15 起它已归属 Superhuman（官方公告原文：FATHOM IS NOW PART OF SUPERHUMAN），独立定价权不再完全在自己手里。

## 来源

1. 官网首页（一句话、bot-free、500K+ companies、合规标识、Works where you meet、Solutions、Competitors 导航）https://www.fathom.ai/
2. 定价页（个人 Free / Premium 16，团队 Team 15 / Business 25 / Enterprise 35，年付省 25%+，90 天保证，功能对照表）https://www.fathom.ai/pricing
3. 产品概览页（转写、摘要、音视频三种视图截图）https://www.fathom.ai/product
4. Superhuman 官方收购公告（2026-04-15 宣布收购 Fathom）https://blog.superhuman.com/superhuman-acquires-fathom/
5. Product Hunt 产品页（316 条评论汇总计数 + 8 条最新原话；产品页本身被 Cloudflare 拦截，采集见 `_raw.md`）https://www.producthunt.com/products/fathom
6. Product Hunt 评论区 https://www.producthunt.com/products/fathom/reviews
7. G2 评论页（4.6 / 177；**页面主体为同名财务分析产品，仅 1 条与会议记录相关**）https://www.g2.com/products/fathom/reviews
8. Fireflies 定价页（Free / Pro 18 月付·10 年付 / Business 29·19 / Enterprise 39 仅年付；1,000,000+ companies 自述）https://fireflies.ai/pricing
9. Otter 定价页（本次仅读到学生折扣 FAQ 段，正价未完整读取）https://otter.ai/pricing
10. Granola 定价页（JS 渲染，本次未读到可引用正文）https://www.granola.ai/pricing
11. 实测表（2026-11-19，20 分钟，实测（燃冰））`实测.md`
12. 官网 OG 主图与产品截图（可热链原图，见 content.json 的 SHOT_1–6）https://cdn.prod.website-files.com/6899da9beccbdbe92be49b5d/68f20f5cd1c6d0de365b8849_Fathom-Visual_Identity_Concepts-Stage_07-Website_Thumbnail-01.jpg
*（内容由AI生成，仅供参考）*
*（内容由AI生成，仅供参考）*
