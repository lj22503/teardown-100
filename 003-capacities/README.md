---
type: 产品拆解
产品: Capacities
slug: capacities
队列号: 003
分类: notes-documents · 个人知识管理（PKM）
系列: AI产品Sense · 第 3 篇
拆解日期: 2026-11-11
材料版本: 官网/why 页/定价页/六张对比页/whats-next/whats-not-next 2026-11 版 · PH 66 条 · G2 1 条 · App Store 40 条
实测状态: 已实测（2026-11-11，20 分钟，署名「实测（燃冰）」）
状态: 已完成
tags:
  - product-sense
  - capacities
  - pkm
  - object-based
---

# 003 · Capacities（对照版）

> 三方材料：**① 我的真实体验**（2026-11-11 完成 20 分钟实测，见 `实测任务单.md` 与《2026-11-11 Capacities 真实体验》）｜**② 用户评论**（PH 66 条、G2 1 条、App Store 40 条）｜**③ 公开材料**（官网、why 页、定价页、六张官方对比页、whats-next、whats-not-next）
> 规则：事实都有来源；推断标 `[推断]` 或（我的判断）；体验结论只写我实测过的，没测的写没测。

## 一、8 维度速览

| # | 维度 | 一句话结论 | 依据 |
|---|---|---|---|
| D1 | 定位与承诺 | 官方 slogan 是 "Stop building your system. Start using it."，卖的是「结构天生就在，你不用搭」——首页、定价页、whats-next 都没把它归到 AI 工具里 | why 页（/why-capacities）首句、whats-next（2026-09-08）原文 |
| D2 | JTBD | 功能：让散落的材料自己长成关系网；情绪：别再为一个笔记系统当项目经理；社会：看上去是个有体系的人 | why 页话术 ＋ PH 评论（"Obsidian 像在城市工作，Capacities 像在乡下"） |
| D3 | 核心循环 | 每日笔记当收件箱 → 碎片升级成 object → object 自动双向链接 → 第二天回来看时间线 | 官网每日笔记与 object 页说明；实测（燃冰）：五类对象一眼看懂 |
| D4 | 信息架构 | 对象模型是它的护城河候选：`Person / Book / Meeting / Project` 等 typed object + 属性 + 反向链接，**一个东西只存一次** | 对比页表格 "Typed objects with properties & links"；实测（燃冰）：书、项目、人、每日笔记、灵感五类 |
| D5 | 体验 | **实测：注册流程里就有引导，打开到写出第一篇 1 分钟，全程没卡。** 但评论侧一致指向移动端是另一个人做的产品 | 实测（燃冰）；App Store 3★「Desktop is Lifechanging, iOS is Barely Functional」 |
| D6 | 商业模型 | 免费给「结构 + 存储」（无限 object、全平台同步、导入导出、只读分享），钱收在「调用 + 回顾」（AI、查询、任务、日历、语义检索） | 定价页三档对比表 |
| D7 | 竞争与迁移 | 官方同时打 6 家（Obsidian/Evernote/Notion/Tana/Heptabase/Anytype），六张 `/compare/*` 全 200；`/vs`、`/alternatives`、`/switch` 全 404——打法不是功能对比，是「你是谁」的自我识别 | 2026-11-11 逐页探测结果 |
| D8 | AI 位置 | 官方明写 AI should "stay assistive"，不进主循环；AI 全在 Pro 之后，免费版零 AI | whats-next 原文 ＋ 定价页（Basic 行 AI 为 Not included）＋ 实测（燃冰）：墙在 AI 与任务/探索触发 |

## 二、9 字段卡片

| 字段 | 值 |
|---|---|
| 产品 | Capacities（官方自述完全独立自营、团队 7 人；whats-next 原文） |
| 队列号 / slug | 003 / capacities |
| 分类 | notes-documents · 个人知识管理 |
| 官网 / 一手页 | https://capacities.io ｜ PH：producthunt.com/products/capacities |
| 定价 | Basic 免费永久；Pro HK$77.99/月、Believer HK$98.99/月（月付，港区页面，年付 -16%）；Plus 加购 HK$66.67/月（年付）。官方对比页统一美元口径：Pro $9.99/月（按年付） |
| 规模（自述+平台） | 官网 why 页出示 50,000+ 活跃知识工作者、10,000+ Discord 社区成员；PH 4.8（官网 badge 写 198 条评价，产品页实采 66 条，两个口径不一致）；App Store 4.28 / 116 个评分；G2 仅 1 条评论（样本不足） |
| AI 能力 | Pro 含 AI 助手（Explore AI Chat）、属性自动填充、图片分析/OCR、自动打标签与归集、`/Ask AI`、AI 生成查询；AI Chat Connectors（ChatGPT/Claude/Cursor 可直接建改 object）；REST API 2.0 + TypeScript SDK |
| 官方「不做」清单 | 平板手写、公式/高级自动化、闪卡与间隔重复、RTL、**协作与团队版（on hold）**、对象继承、**端到端加密**、终身订阅、**插件** |
| 实测状态 | **已实测**（2026-11-11，20 分钟，实测（燃冰））。唯一没做的一项：喂 8000 字脏材料验证它会不会「通顺地错」，本卡不给结论 |

## 三、校正后的四栏

- **一句话定位**：它卖的不是 AI，是「你不用再花三个月把笔记系统搭出来」——把 PKM 圈最贵的隐性成本（配置与维护）直接抹掉。
- **核心优势（1 条）**：**放弃自由度换来的开箱结构**。不给插件、不给文件夹、不给你自定义脚本，只给你对象类型；代价是你的系统长什么样它说了算，收益是你第一天就能用。实测（燃冰）：注册环节本身带引导，1 分钟出第一篇笔记，比 Obsidian 更容易启用，也比 Notion 更便于结构化。
- **最大短板（1 条）**：**存量迁移时的类型不匹配**（实测（燃冰）判断），叠加**移动端不是同一个产品**。桌面端被评 "lifechanging"，iOS 端被评 "barely functional"：不能建 object 类型、分享面板坏数月、同步要重启、iPad 分屏布局错乱。
- **失效场景（有实测也有评论证据，不用推测）**：
  1. **想定制的人**：实测（燃冰）原话判断——想自己定制一些东西，它不合适。没有插件、没有公式与高级自动化（官方明列）。
  2. **存量迁移者**：实测（燃冰）最大感受就是「搬进来类型对不上」；PH 3★ 原话「唯一阻止我每天用并付费的就是批量导入」——迁移成本直接卡住付费转化。
  3. **靠手机 capture 的人**：Apple Notes 3 秒记完，Capacities 要等它不卡；3★ 原话「我仍然用 Apple Notes 做随手记录」。
  4. **团队 / 需要合规的人**：官方自己写进「不做」（团队版、E2EE），是路线外不是暂缺。

## 四、我的实测（20 分钟，2026-11-11）

> 署名：实测（燃冰）。原始记录：Obsidian Vault《2026-11-11 Capacities 真实体验》。

| 观察项 | 实测结论 |
|---|---|
| 上手用时（TTV） | **1 分钟**从打开到能写出第一篇。原因很具体：使用说明直接嵌在注册流程里，不是让你先去看文档 |
| 有没有卡点 | **没有卡**。第一次用没出现「下一步该点哪」的时刻 |
| 最像智能的一刻 | 输入书名《深度工作》，它自动把结构化信息填好了，不用手打。这个动作发生在免费流程里 |
| 对象模型是否清晰 | 清晰：书、项目、人、每日笔记、灵感五类，看名字就知道干什么；每个内容里还植入默认案例 |
| 免费与付费的墙 | 墙只在「AI」与「任务 / 探索」模块触发。免费版给无限 object，收钱收在「调用 / 回顾」上，不按容量收 |
| 隐私提示 | 有强提示：不用 AI 时数据不会共享给模型供应商 |
| 会不会当主力 | **不会**。但它这套结构值得学——我会把它的字段设计拿去喂给自己的 AI |
| 没测的部分 | 脏材料边界（喂长文看它会不会通顺地错）没做，只看了文档与演示，不下结论 |

**实测之外的一条判断**：它已经把「人、书、会议、项目」清洗成带字段的对象，这正好是个人 agent 最缺的输入层。它围着个人最关注的几块内容去 link，把「被用起来」的成本压到很低——这是比 AI 功能更值钱的地方。

## 五、用户评论证据（全部原文，未改写）

**Product Hunt（4.8 / 66 条，1★ 0 条、2★ 1 条）**

| 星级 | 原话 | 它证明了什么 |
|---|---|---|
| 4★ | "It broke my brain at first… Took me 3 days to stop fighting it. But when it clicked? Magic." | 学习曲线真实存在，「结构天生」≠「零学习」 |
| 3★ | "the only thing retaining me from using it daily and paying premium is bulk import" | 导入 = 付费转化的实体卡点（与我的实测判断一致） |
| 2★（唯一差评） | "the object-oriented notetaking method is not for me — it takes too much thought and effort to set up and organize. Second, I need an app that is available offline." | 对象化对一部分人是负担 |
| 14 赞老用户 | "Obsidian feels like working in a city and Capacities is like working in the Countryside" | 差异是美感与心流，不是功能表 |
| 1 赞迁移者 | "I first lived in Evernote for many years, then went to Notion, then Roam… now Capacities (a pretty common pattern)" | 迁移链：Evernote → Notion → Roam → Capacities |
| 4★ | "designed for individual use… not designed for team work" | 用户自己复述了官方的「不做团队」立场 |

**App Store（4.28 / 116 评分，采到 40 条，1–3★ 占多数）**

| 星级 | 原话 | 它证明了什么 |
|---|---|---|
| 3★ | "Desktop is Lifechanging, iOS is Barely Functional"（标题） | 端间断裂是最大口碑裂缝 |
| 3★ | "the most basic function (share from an app via sharesheet) has been broken for many months… no fix in sight" | 移动端主链路（capture）断裂 |
| 3★ | "I can group multiple lines on iPhone but not on iPad… I have to get on my iPad or computer in order to create or edit an object" | 能力矩阵不一致，edges 都在移动端 |
| 3★ | "it consistently has trouble with syncing… I end up having to reboot the app" | 同步可靠性（与官方「sync 免费且无痛」卖点冲突） |
| 1★ | "Dishonest Pricing… $199/year? No way… It doesn't even have an import or export tool." | 渠道价差 + 导入缺失被读成「不诚实」 |
| 1★ | "iPad handwriting support please!! It just does not recognize 90% of what I write with my pencil" | 官方明确不做手写，用户仍在要求——需求与路线正面撞车 |
| 1★ | "The app does not load. It is stuck at the splash screen.（iOS 15）" | 低版本 iOS 直接不可用 |
| 1★ | "No color, no instructions, like an ADD-er's worst nightmare…" | 与「开箱即用」对撞：没有引导时，空状态是负资产（和我实测「引导在注册流程里」正好互补） |
| 3★ | "I'm in love with the concept… works really well with my ADHD"（同一条里） | 同一人群里既是最好也是最难，产品感两极化 |

**G2（仅 1 条 4★，样本不足，只能当线索）**：dislike 字段写「标签一多就丢项」「缺乏刚性约束」。**不作为结论使用。**

## 六、附录四段摘要

- **16 对标竞品地图**：2026-11-11 逐页探测——`/compare`、`/compare/{obsidian,evernote,notion,tana,heptabase,anytype}` 全部 200；`/vs`、`/alternatives`、`/switch` 全部 404。**它把「打谁」写进了 URL 结构**：只做「存量迁移者的比较」，不做泛替代品。PH 的 Similar Products 是另一套名单（Obsidian、Craft.do、Bear、Reflect、Tana）——用户视角的相似 ≠ 官方视角的对手。
- **17 竞品技术底座**：Obsidian＝本地 Markdown + 插件（锁住可迁移/可 agent 化，锁死开箱即用）；Notion＝云端块 + 数据库（锁住团队，锁死个人配置成本）；Tana＝supertag 大纲 + 查询（锁住重流程，学习曲线最陡）；Anytype＝本地优先 + P2P + E2E + 开源（锁住隐私，锁死生态速度）。Capacities＝云端对象 + 全内建 + 无插件，**用「不做」换一致性与速度**，代价是隐私叙事与可扩展性永久缺位。
- **18 可迁移的机会（我的判断）**：① 官方对比页 + 官方「不做什么」页是零成本的信任与 GEO 资产；② 它公开的短板就是生意：迁移时的类型映射；③ 它的字段设计本身就是可复用资产（我把这套结构拿去喂自己的 AI 就是这个动机）。
- **19 流量与变现拆解**：钱从「买了三四个笔记软件还没找到系统」的知识工作者兜里出；凭什么拿到——对比页吃离付费最近的长尾搜索 ＋ Reddit/Discord 口碑 ＋ PH 三次发布长期挂 4.8 分；三层变现 Basic → Pro/Believer → Plus(AI 额度加购)。**最脆的一根梁是「AI 在付费墙后」**，因为那正是转化率最高、也最容易流失的一刻。
- **20 官方「不做」清单与替代路径（补充第五段）**：不做 E2EE 与不做插件是同一个取舍的两面——都会拖慢一致性与速度。导出侧三档都含 Markdown/CSV，搬走不靠它批准；但把隐私当第一需求的用户注定流向 Anytype 或 Obsidian。

## 附：证据索引

- 采集原文：`_raw.md`（首页/定价/PH）、`_raw-round2.md`（六张对比页 + whats-next + whats-not-next）
- 评论：`capacities-评论.md`（PH 66）、`capacities-G2评论.md`（G2 1）、App Store id 1670188548（40 条，本卡摘要）
- 官方页：https://capacities.io/why-capacities（承诺）｜https://capacities.io/pricing（三档）｜https://capacities.io/compare（竞品目录）｜https://capacities.io/whats-next（路线与 AI 立场）｜https://capacities.io/whats-not-next（不做清单）｜https://docs.capacities.io/（AI 与导入）
- 实测：`实测任务单.md`（20 分钟流程）｜Obsidian Vault《2026-11-11 Capacities 真实体验》（原始记录，署名 实测（燃冰））
- 渲染产物：`teardown-zh.html` / `teardown-en.html`（content.json 生成）

---
> 本卡所有事实均可在上述来源中逐条核对；凡推断已标 `[推断]` 或（我的判断）；实测结论均标注「实测（燃冰）」，未测的项目明确写「未测」。
