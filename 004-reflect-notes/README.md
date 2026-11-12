---
type: 产品拆解
产品: Reflect
slug: reflect-notes
队列号: 004
分类: notes-documents · 个人知识管理（PKM）
系列: AI产品Sense · 第 4 篇
拆解日期: 2026-11-12
材料版本: 官网 reflect.app 2026-11 版（Reflect Open 形态）· PH 产品页与 45 条评论 · GitHub 仓库与 README/CLI 文档 2026-11 版 · 定价页 404，改用第三方 2026-10 核对 · G2 采集失败 0 条
实测状态: 已实测（2026-11-12，20 分钟，署名「实测（燃冰）」；T2 失效场景未做，本卡不给结论）
状态: 已完成
tags:
  - product-sense
  - reflect
  - pkm
  - local-markdown
---

# 004 · Reflect

> 三方材料：**① 我的真实体验**（2026-11-12 完成 20 分钟实测，原始表 `实测.md`）｜**② 用户评论**（PH 45 条，4.8 分；G2 本次 0 条）｜**③ 公开材料**（官网首页、GitHub 仓库 README/CLI/privacy 文档、PH 产品页四次发布记录）
> 规则：事实都有来源；推断标 `[推断]` 或（我的判断）；体验结论只写我实测过的，没测的写没测。

## 一、8 维度速览

| # | 维度 | 一句话结论 | 依据 |
|---|---|---|---|
| D1 | 目标用户 | 个人用户，尤其是苹果生态里的人；再精确一层是「不想为记笔记先做一次架构决策」的人 | 官网只提供 Mac 与 iPhone/iPad 两端；PH 评论「thought I required a very heavy feature set」；实测（燃冰）：它应该是给苹果用户用的 |
| D2 | 核心问题 | 起步卖的是云端 E2EE 双链笔记，2026 年转向开源本地版：笔记就是你选的文件夹里的 Markdown | 官网首屏（本地文件 / 自选 iCloud 或 Git 同步 / MIT 开源）；PH 评论反复点名端到端加密 |
| D3 | AI 是否不可替代 | 可替代但被产品化：AI 是可选层，用自己的 key，价值在「内置了一整套写好的提示词」而不是模型本身 | 官网原话 Optional AI、Connect your own API key、AI usage is billed separately；GitHub README（OpenAI / Anthropic / Google / OpenRouter 四家 key、答案 cite source notes）；实测（燃冰）：内置提示词帮用户推进下一步 |
| D4 | 工作流整合 | 收口在「今天」：会议笔记、日历与联系人、浏览器剪辑、Kindle 笔记、语音备忘都落进当天那篇 | GitHub README（Chrome 扩展、audio memos、iCloud/git 同步）；PH 评论（Google Calendar & Contacts、Kindle notes sync、web highlighter） |
| D5 | 商业模式 | 单档订阅：Classic 官方原话「One plan one price」$10/月、14 天试用、无免费档；Open 版 Mac 免费、iPhone/iPad 订阅；AI 不赚差价 | 官网定价区原话；第三方 2026-10 核对（$10/月、无免费档）；toolradar 2026-10 页面（14-day free trial） |
| D6 | 竞争差异化 | 它砍掉了 Obsidian 的 vault/插件与 Capacities 的对象模型，只留时间轴 + 双链；卖点是「你有想法，AI 帮你往下推」 | 实测（燃冰）原话判断；PH 汇总原话 opinionated setup；官网 IA（daily notes 为默认入口） |
| D7 | 成本结构 | 对用户是「14 天试用后一次性决定」，对厂商是「不承担模型成本」（自带 key） | 官网 AI usage is billed separately by your provider；实测（燃冰）：墙在试用到期，不在功能触发点 |
| D8 | 技术边界 | 没答出来——原因是我没测。T2（喂互相矛盾 / 8000 字术语密集长文看它会不会「通顺地错」）这次没做，本卡不写结论 | 实测（燃冰）：T2 一栏留「？」 |

## 二、9 字段卡片

| 字段 | 值 |
|---|---|
| 产品 | Reflect（Reflect App, LLC；官网 About 自述 indie team dotted across the globe） |
| 队列号 / slug | 004 / reflect-notes |
| 分类 | notes-documents · 个人知识管理（PKM） |
| 官网 / 一手页 | https://reflect.app ｜ PH：producthunt.com/products/reflect-notes ｜ 代码：github.com/team-reflect/reflect-open |
| 定价 | Classic：官方首页定价区「One plan one price」$10/月，14 天试用，第三方 2026-10 核对为 $10/月、按年计费、无免费档。Open：Mac 免费，iPhone/iPad 需订阅（本地价在 App Store，官网未披露）。AI 自带 key，模型费用由供应商另收 |
| 规模（自述+平台） | 官方未披露任何用户数；可核实的只有 PH 4.8 分 / 45 条评论 / 1.2K 关注、四次发布（2022-04 / 2022-07 / 2023-01 / 2023-11，含 #2 Bootstrapped & Crowdfunded Product of the Year） |
| AI 能力 | ⌘J 问笔记（答案回链源笔记）、语义搜索、语音转写、改写与摘要、保存自定义提示词；`private: true` 的笔记排除在 AI 与外部服务之外；四个供应商 key 任选 |
| 官方「不做」清单 | 不做插件市场、不做模板市场、不做团队/协作套餐、不做文件夹树（只有时间轴 + 双链）、不内置模型（自带 key）；签名分发包只给 Mac（Windows/Linux 在 Releases 里是 unsigned builds） |
| 实测状态 | **已实测**（2026-11-12，20 分钟，实测（燃冰））。唯一没做的一项：T2 脏材料/矛盾材料边界，本卡不给结论 |

## 三、校正后的四栏

- **一句话定位**：它卖的不是功能，是把「第一分钟」做到零决策——打开就是今天，没有新建、没有 vault、没有模板选择。
- **核心优势（1 条）**：**用「不要生态」换来的第一分钟**。代价是没有插件、没有结构化查询、没有 Windows 签名包；收益是实测（燃冰）从打开到能产出 10 分钟、前 5 分钟就出第一个可用结果，前置动作只有注册和设一个密码，不需要先读文档。
- **最大短板（1 条）**：**墙是时间墙，不是功能墙**。14 天试用一到期就得决定付不付，而此时它旁边站着免费的 Obsidian、有免费档的 Capacities；PH 的 Cons 里 price compared to competitors（2 次）与实测（燃冰）「不会留下，就是因为这条」指向同一处。
- **失效场景**（有实测也有评论证据）：
  1. **按文件夹思考的人**：PH 汇总原话 its backlink-first structure does not suit people who think in folders；实测（燃冰）：它没有文件夹概念，我找不到「按项目看全部」的入口。
  2. **要插件 / 要结构化的人**：官方明确没有插件与模板市场；对比 Obsidian 4,350+ 插件（第三方口径，见附录 17），这是路线差异不是暂缺。
  3. **主力机不是 Apple 的人**：官网下载区只给 Mac 与 iPhone/iPad，GitHub README 原话 Windows and Linux: each release includes unsigned builds——实测（燃冰）在 Windows 上没走通。
  4. **必须端到端加密的人**：Classic 有 E2EE，Open 改成「本地文件 + private 标记」，两种隐私叙事不是一回事，转型期用户要自己分清（官网原文两套并存）。

## 四、我的实测（20 分钟，2026-11-12）

> 署名：实测（燃冰）。原始记录：`实测.md`（20 分钟四段式）。

| 观察项 | 实测结论 |
|---|---|
| 上手用时（TTV） | **10 分钟**从打开到能产出；其中**约 5 分钟**出第一个可用结果。前置动作是注册 + 设一个密码，不是读文档 |
| 哪一步停下来想「下一步该干嘛」 | **不太需要**——这一层它做到了（打开即今天） |
| 结果改了几次才敢用 | 一次就够用；真正起作用的是日历把所有日期放在一个页面。但它没有文件夹概念，我找不到第二个入口 |
| 最像智能的一刻 | 不是 AI，是**日历摊平**：所有日期摆在一屏，替我省掉「找」这个动作 |
| T2 边界（矛盾材料 / 长文） | **未做**。实测表里这一栏没填，所以本卡不写「它会不会通顺地错」，也不给 ⑧ 的结论 |
| 免费与付费的墙 | 墙在 **14 天试用到期**那一刻，不在任何功能触发点；免费版是 Mac，我没有 Mac |
| 它主卖什么 | 实测（燃冰）判断：卖的是**系统提示词**——内置一批写好的提示词，帮你把「下一步该写什么、该干什么」推进下去，不是卖模型 |
| 会不会留下 | **不会**：14 天后要收费。但补一句——它现在提供了 Reflect Open，这条路也许会不一样 |
| 没测的部分 | T2 失效场景没做；AI 在真实长文上的表现没测。本卡只写「内置提示词存在且有价值」，不写效果评分 |

**实测之外的一条判断**：我原本没想明白它给谁用，用完的判断是给「不喜欢折腾的苹果用户」。从产品 sense 看，同一赛道、同一个底层假设（本地 Markdown + AI），Obsidian 赌「用户愿意为了强大而折腾」，Reflect 赌「用户宁愿放弃强大也要省事」——它竞争的不是功能，是第一分钟。

## 五、用户评论证据（原话，未改写）

**Product Hunt（4.8 / 45 条，本次采到 8 条正文；1★ 与 2★ 各 0 条，采集结果未返回单条星级，故不标星）**

| 原话 | 它证明了什么 |
|---|---|
| "it is the *only* tool (besides email) that I use every single day" | 日更习惯是它最强的留存证据（与「每日笔记当锚点」的设计对得上） |
| "it has you enter notes in chronological form and then uses backlinks to cross-reference everything" | 时间轴 + 双链这个组合，用户自己能讲清楚 |
| "The minimalist interface belies its powerful capabilities… The semantic search capability is particularly impressive" | AI 的价值被感知在「搜得到」，不在「生成得多」 |
| "It lacks some of the features of similar apps in the space… what Reflect does well, it does very well" | 功能缺位被主动原谅——这是 opinionated 产品才有的宽容度 |
| "After jumping from Evernote, to Roam, to Craft, to Obsidian, to Agenda, I now personally use Reflect every day" | 迁移链：Evernote → Roam → Craft → Obsidian → Agenda → Reflect；这群人已经换过四五个，忠诚度天生低 |
| "the built-in GPT-4 integration has many predefined prompts (which are great) but you can also create custom prompts" | 与我实测结论一致：它卖的是提示词，不是模型 |
| "use the Whisper integration to dictate the events of a meeting… Reflect will automatically insert a summary, action items, and next steps" | 转写 → 摘要 → 行动项这条链路是真实工作流，不是演示 |
| "it's end-to-end encrypted means which means I don't have to worry about what I put there" | 加密是它早期最硬的信任资产——而 Open 版把它换成了「本地文件」，这是转型期的裂缝 |

**PH 汇总页的 Cons（抱怨计数就是痛点分布）**：price compared to competitors（2 次）、syncing issues（2 次）；汇总原话同时点名「backlink-first 结构不适合按文件夹思考的人」「协作有限」。

**G2（本次 0 条，抓取失败）**：只作为入口保留，**不用于任何结论**。样本不足，我不编差评。

## 六、附录四段摘要

- **16 对标竞品地图**：PH 的 Similar Products 只点了五家（Craft.do 4.6/37、Capacities 4.8/66、Tana Outliner 4.8/55、HyNote AI 4.8/39、Bear 4.6/34），**Obsidian 不在名单里**——它自己没把本地文件派写进对手。我的判断：这五家没有一家是它的真对手，真正带走用户的是名单外那个免费的本地文件 App；G2 失败导致「迁出方向」这一栏没有证据，本报告不给结论。
- **17 竞品技术底座**：Reflect Open＝本地 Markdown 文件夹 + 可重建 SQLite 索引 + 自带 key 的 AI（锁住数据归属与零配置，锁死生态）；Classic＝云端 + 客户端 XChaCha20-Poly1305（第三方口径）；Obsidian＝本地 Markdown + 插件生态；Capacities＝云端 typed object 全内建；Tana＝supertag + 查询；Craft＝云端文档块 + 模板。`[推断]` 护城河结论：它用「不要生态」换第一分钟，代价是永远无法靠生态加深护城河——本地 Markdown 是公共地基。
- **18 可迁移的机会（我的判断）**：① 把 `reflect today / search / show` 的输出契约固定下来，让笔记变成 agent 的默认记忆层；② 给 Windows / 中文用户一条明确签名路径——实测（燃冰）卡在没 Mac，而底层只是文件夹 + Markdown；③ 把内置提示词做成「会议 / 面试 / 复盘」三套成套能力，让 AI 从可选变默认。三条里最轻的是②，最值钱的是①。
- **19 流量与变现拆解**：钱从「苹果生态里的个人用户」兜里出，不为功能付、为「不用想」和「加密/本地」付；凭什么拿到——PH 四次发布长期挂 4.8 分 + 推特口碑墙 + 2026 年新增 GitHub（MIT / Releases / CLI）这条开发者渠道 `[推断]`；三层结构其实是两层：试用 → 单档订阅，没有额度、没有席位、没有 AI 加购；**最脆的一根梁是「试用到期」**——同一时刻免费替代品就摆在右边。

## 附：证据索引

- 采集原文：`_raw.md`（PH 产品页 + reflect.app 首页；定价页 /not-found 404）
- 评论：`reflect-notes-评论.md`（PH 45 条汇总 + 8 条正文）｜`reflect-notes-G2评论.md`（本次 0 条，抓取失败）
- 官方页：https://reflect.app/（本地文件、Optional AI、Classic 仍在维护）｜https://github.com/team-reflect/reflect-open（MIT、Releases、unsigned Windows/Linux 构建）｜README 功能清单与 CLI｜docs/cli.md｜docs/privacy.md
- 定价：https://toolradar.com/tools/reflect/pricing（2026-10 核对，$10/月、14 天试用、无免费档）
- 实测：`实测.md`（20 分钟四段式，署名 实测（燃冰））
- 渲染产物：`teardown-zh.html` / `teardown-en.html`（content.json 生成）

---
> 本卡所有事实均可在上述来源中逐条核对；凡推断已标 `[推断]` 或（我的判断）；实测结论均标注「实测（燃冰）」，未测的项目明确写「未测」。
