# 历史期回填说明（001–012）

> 配套文件：`history-products-rows.csv`（12 行 × 19 列，UTF-8 BOM，`csv` 模块写出）
> 生成日期：2026-11-26 ｜ 回填人：DSH 子 agent `history-backfill`
> 纪律：只新增本文件与上面那张 CSV，未改动任何已有文件；每个字段都能指回具体一节，没依据的写「未采集」/「未公开」。

---

## 0. 一句话结论

12 行齐全，表头逐字一致，无空单元格。**11 个产品的字段基本都能落到具体章节；1 个产品（008-cursor）没有 README，只能从官网抓取原文补一半，另有 6 个字段写「未采集」。**

---

## 1. 来源优先级（先读这段，核对时按这个顺序找原文）

| 优先级 | 来源 | 覆盖范围 | 为什么用它 |
|---|---|---|---|
| ① | `<dir>/README.md` | 全部 12 个目录中 **11 个**（008 缺） | 任务指定的主源；8 维表、9 字段卡、〇 节都在这里 |
| ② | `<dir>/content.json` | 001–007、009–012（008 缺） | 同一张卡的**渲染源**，是 8 维/9 字段的结构化版本（`CATEGORY`/`SEGMENT_*`/`JTBD_*`/`CHANNEL_1-3`/`FINAL_MOAT_OR_LACK_THEREOF`/`REVENUE_MODEL_DETAIL`），每条都有原文可核对。仅在 README 缺该节或该节没写数字时用它兜底 |
| ③ | `<dir>/_raw.md`、`<dir>/*评论.md` | 008 只有这一层 | 官网自动抓取原文，只用来补 008 的官网自述与产品能力 |

**凡用 ② 兜底的格子，下表都单独标了「来自 content.json」，没有混在 README 里冒充。**

---

## 2. 三个必须先说清的格式坑

1. **8 维的编号在 12 期里不统一，不能按位置对齐。**
   - 002 用 `①②③…`：① 目标用户 ② 核心问题 ③ AI 是否不可替代 ④ 工作流整合 ⑤ 商业模式 ⑥ 竞争差异化 ⑦ 成本结构 ⑧ 技术边界。
   - 003–005 用 `D1–D8` 但含义另一套：D1 定位与承诺 / D2 JTBD / D3 核心循环 / D4 信息架构 / D5 体验 / D6 商业模型 / D7 竞争与迁移 / D8 AI 位置。
   - 006–012 又回到 `D1–D8`：D1 目标用户 / D2 核心问题 / D3 AI / D4 工作流 / D5 商业模式 / D6 差异化 / D7 成本 / D8 边界。
   - 所以本次是**按语义取字段**（如 `jtbd` 在 002 取「② 核心问题」、003 取「D2 JTBD」、006 取「D2 核心问题」），不是按列号。核对时请按语义找。
2. **〇 节（AI 类型判定）只有 6 期有**：006、007、009、010、011、012。003/004/005 没有〇 节（`ai_mode` 分别取自 D8 / D3 / 交叉推断，下表逐条注明）；001/002 是老格式，也没有。
3. **README 里没有「段 9 增长」和「段 15 终局/护城河」这两个编号**。实际对应内容是：`primary_channels` ← 附录 **19「流量与变现拆解」**（003–012 都有），`moat_hypothesis` ← 附录 **17「竞品技术底座」里的 `[推断]` 护城河结论**（003–012 都有）+ content.json 的 `FINAL_MOAT_OR_LACK_THEREOF`。001/002 只有 content.json 这一处有。

---

## 3. 逐产品字段来源

图例：**R** = README；**J** = 同目录 content.json；**X** = `_raw.md` 抓取原文；`未` = 未采集 / 未公开。

### 001 · Notion —— 老格式，没有 8 维表 / 9 字段卡 / 〇 节

| 字段 | 取自 | 说明 |
|---|---|---|
| name / slug / no | R 标题 + 目录名 | — |
| category | **J** `CATEGORY` | README 无「分类」。原值「AI 工作空间 / 知识管理」；**不是**我按 D6 推断的（001 无 D6） |
| one_liner | **J** `ONE_LINER_2_LINE_SUBTITLE` | README 三节「一句话定位」原话是「把工作现场搬进一个可结构化的空间…卖的是『你的工作已经在它里面』，不是 AI」——压缩后与 J 的版本一致，取 25 字版 |
| icp_primary / secondary | **J** `SEGMENT_1/2/3_NAME` | R 一节第 2 条只说「已从个人笔记转向企业/团队/初创/开发者四类」，没分层 |
| jtbd | **J** `JTBD_FUNCTIONAL` | R 二节的 ⑧ 只谈边界，无 D2 原文 |
| core_scenarios | R 二节 + **J** `JTBD`/帮助页清单 | R 里出现的是：会议纪要、决策链、结构化、企业搜索、MCP/API 接入、日历与打卡打不通 |
| ai_mode | **R 四节 + J**，标 `[推断]` | README 原话「在自己的竞争优势上叠加 AI，让 AI 实现价值变现」→ 判定为嵌入，但**001 无〇 节，属我的推断**，已打标 |
| pricing_model | R 二节 ⑤ | 原话「存信息不要钱，调用查找时收费」，又「月租 + 额度双轨」 |
| free_tier / paid_tiers | R 二节 + **J** `REVENUE_MODEL_DETAIL` | R 只写「Free/Plus 只有 Trial of Notion AI；正式额度从 Business $20 起（1,500 credits/席位/月）」；$10 Plus 与 500 Select credits 来自 J |
| primary_channels | **J** `CHANNEL_1-3` + 流量节 | R 无流量章节。J 的「流量与变现拆解」一节写明：爆款弱、**长尾强**、无补贴 |
| moat_hypothesis | **J** `FINAL_MOAT_OR_LACK_THEREOF` | R 只有「优势=个人上下文密度」，没有终局结论 |
| evidence_urls | **J** `sources_zh` 前 3 条官网页 | R 附节只给了 1 个定价页 URL |

**缺**：〇 节、9 字段卡、D6/D7 原文、流量节、护城河节——全靠 content.json 兜底，属「软缺」。

### 002 · Obsidian —— 有「八维 + 单卡 9 字段」，无 〇 节

| 字段 | 取自 | 说明 |
|---|---|---|
| category | **R** frontmatter「分类」 | 原值 `notes-documents · 本地知识管理` |
| one_liner | **R** 一句话定位 | 原文两句，取第一句 |
| icp_primary | **R** 八维 ① | 「个人，愿意为自己搭系统的人」 |
| icp_secondary | **J** `SEGMENT_2/3` | R 的 ① 只有一层；J 补「把 vault 当 AI 上下文的工程师」「受合规/保密约束的个人」 |
| jtbd | **R** 八维 ② | 原话「解决知识的**关联**，不是知识的存放」 |
| core_scenarios | **R** 八维 ④ | 建库→写→双链→本地库→外部 AI 读库 |
| ai_mode | **R** 八维 ③ | **官方零 AI 功能**，AI 在用户手里 → 记作「非 AI」，没有硬套原生/嵌入/辅助三值（套任何一个都会失真），核对时请留意这个取值 |
| pricing_model | **R** 八维 ⑤ | — |
| free_tier | **R** 一句话定位节 | 定价页原话 `Free without limits, no sign-up required` |
| paid_tiers | **R** 八维 ⑤ | Sync $4、Publish $8、商业授权 $50/人/年；**Catalyst 金额 README 没写**（J 写 $25），本格按规定只放 README 原文数字 |
| primary_channels / moat | **J** `CHANNEL_1-3` / `FINAL_MOAT` | R 无流量节；护城河只有「三条洞察」里的第 3 条（AI 让给了外部），J 的表述更完整 |
| evidence_urls | R 附节 + **J** `sources_zh` | 官网、定价页、社区插件目录 |

**缺**：〇 节、流量节、护城河节；另 `icp_secondary`、`primary_channels`、`moat` 三格靠 content.json。

### 003 · Capacities —— 8 维 + 9 字段齐全，无 〇 节

- `category` ← R 9 字段卡「分类」（`notes-documents · 个人知识管理`）。
- `one_liner` ← R 三节「一句话定位」（不是 AI，是「你不用再花三个月把笔记系统搭出来」）。
- `icp_primary` ← **J** `SEGMENT_1`：R 的 D1 是「定位与承诺」，**没有目标用户**，只能用 J 的迁移链表述（Evernote→Notion→Roam→Obsidian→Capacities）。
- `icp_secondary` ← **J** `SEGMENT_2/3`。
- `jtbd` ← R D2「JTBD（功能/情绪/社会）」的功能层。
- `core_scenarios` ← R D3 核心循环 + 9 字段卡「AI 能力」。
- `ai_mode` ← **R D8**「官方明写 AI should stay assistive」→ 辅助。无〇 节。
- `pricing_model` ← R D6 商业模型。
- `free_tier` / `paid_tiers` ← R 9 字段卡「定价」原文（**港币区域价**，同一格里带上官方对比页的美元口径 $9.99）。
- `primary_channels` / `moat` ← R 附录 19 / 附录 17 + **J** `CHANNEL_*`/`FINAL_MOAT`。
- `evidence_urls` ← R 9 字段卡「官网/一手页」，取 why / pricing / whats-not-next 三页。
- **缺**：〇 节（ai_mode 从 D8 转写）。

### 004 · Reflect —— 8 维 + 9 字段齐全，无 〇 节

- 全部字段有 README 原文（D1/D2/D4/D5/D6、9 字段卡定价、附录 19、附录 17）。
- `ai_mode` ← **R D3**「AI 是可选层，用自己的 key」→ 记作「可选层」，不硬塞三值；无〇 节。
- `jtbd` 用 **J** `JTBD_FUNCTIONAL` 的完整句（R 的 D2 讲的是「起步卖云端 E2EE、2026 转开源本地版」，那是定位变迁，不是 JTBD）。
- `icp_secondary` 用 **J** `SEGMENT_1/2/3` 合成（R D1 只给「个人 + 苹果生态 + 不想先做架构决策」）。
- 定价两格照抄 R 9 字段卡：Classic $10/月、14 天试用、**无免费档**；Open 版 Mac 免费、iPhone/iPad 价格「官网未披露」。
- **缺**：〇 节；另有 1 处 README 自己声明没测（T2 脏材料边界），但不影响本表字段。

### 005 · HyNote AI —— 8 维 + 9 字段齐全，无 〇 节

- `ai_mode` 是**本表唯一一处跨期推断**：R D3 说「不可替代，嵌在主干里不可替代」，但 005 没有〇 节；采用 **006 第〇节对 005 的判定口径**（「HyNote 是 AI 嵌在笔记主干里，拿走 AI 还能当录音笔」）→ 嵌入，并打 `[推断]`。
  - ⚠️ 已知冲突：005 自己的 9 字段卡写「官网说它是现在唯一一个 AI 原生驱动的产品」，那是**官网口径**不是判定口径。两处都保留，本表取判定。
- 其余：`icp_primary` ← R D1（专业人士与学生）；`icp_secondary` ← **J** `SEGMENT_2/3`；定价两格 ← R 9 字段卡「定价」五档原文；channels ← 附录 19 + **J**（Free Tools 长尾那条 R 与 J 都标了 `[推断]`，本格保留标记）。
- **缺**：〇 节。

### 006 · Claude —— 6 期起的新格式，〇 节齐全

- `ai_mode` ← **R 〇 节**照抄：「AI 原生（AI Native）」。
- `one_liner` ← R 三节（「不是助手，是插座」）。
- `icp_primary` ← R D1（写代码的人）；`icp_secondary` ← R D1 + **J** `SEGMENT_2/3`（内容与知识工作者；官网 16 类）。
- `jtbd` ← R D2（判断力外包）。
- `core_scenarios` ← R D4 三层 + 9 字段卡「AI 能力」。
- `pricing_model` ← R D5（订阅 + 平台按量 + 企业合同）。
- `free_tier` / `paid_tiers` ← **R 9 字段卡明确写「本次未取到官方金额」，只给结构与脚注** → 两格都写「未公开」并保留可核实的规则（这是任务允许的「没有就写未公开」，**没有猜档位价**）。
- `primary_channels` ← 附录 19 + **J** `CHANNEL_*`；`moat` ← 附录 17 的 `[推断]` 结论 + **J** `FINAL_MOAT`。
- **缺**：仅 `free_tier` / `paid_tiers` 两格（抓取失败，原文如此）。

### 007 · Framer — 〇 节齐全

- `ai_mode` ← R 〇 节：「嵌入（Embedded）」。
- 其余全部有 R 原文：D1（目标用户）、D2、D4、D5 + 9 字段卡「定价」（**港币区域价**，本格保留 HK$ 并注明美元价为第三方转述、不作官方口径）、附录 19 / 17。
- `free_tier` / `paid_tiers` 取 9 字段卡原文（Free 500 credits；Basic/Pro/Enterprise 三档 + 四个附加包）。
- **缺**：无。

### 008 · Cursor —— ⚠️ 目录里**没有 README.md**

| 实际情况 | `008-cursor` 只有 `_raw.md`、`cursor-评论.md/json`、`cursor-G2评论.md/json`。没有 README、没有 content.json、没有 teardown-zh.html，**这一期没写完**。`_raw.md` 里定价页那一段是 `FAILED https://cursor.com/pricing`（PageNavigationTimeoutError）。 |
|---|---|---|

| 字段 | 取自 | 说明 |
|---|---|---|
| name / slug / no | 目录名 + `_raw.md` | — |
| category | **X** 官网自述 + 我的归纳，标 `[推断]` | 官网一句「AI Coding Agent for Building Ambitious Software」→「AI 编程工具 / 代码编辑器（AI coding agent）」 |
| one_liner | **X** 官网首屏原文 | 「Cursor 是您的编程智能体，助您构建雄心勃勃的软件」——是官网 tagline，不是我写的定位 |
| icp_primary | **X** 官网原文 | 「构建世界级软件的团队」「超半数财富 500 强」 |
| icp_secondary / jtbd / ai_mode / primary_channels / moat_hypothesis | — | **未采集**（无 README、无 8 维、无 9 字段、无流量节、无护城河节；不拿评论文件里的零散句子拼） |
| core_scenarios | **X** 官网功能原文 | Agent 规划与生成、云端智能体并行、CLI/Slack/GitHub PR 审查、代码库索引与语义搜索 |
| pricing_model | — | **未采集**（定价页 FAILED） |
| free_tier / paid_tiers | — | **未公开**（`_raw.md` 里定价页是抓取失败，只有导航项「定价」，无任何数字） |
| evidence_urls | **X** | 只有 `https://cursor.com/` 一个可用（`cursor.com/agent` 是站内路径，不算一手页，未收） |

> 这一行的正确做法是**重跑 008 期**，不是靠回填补齐。建议在 notes 里保留这个结论给 lead 决策。

### 009 · Figma — 〇 节齐全

- `ai_mode` ← R 〇 节：「嵌入型（Embedded）」。
- 全部字段有 R 原文：D1/D2/D4/D5、9 字段卡「定价」（四档 × 三类席位 + credits，**美元年付原价**）、附录 19 / 附录 2 护城河。
- `core_scenarios` 里 `Sites（发布，beta）` 保留 beta 标记——README 明写 Sites 页本次 404，beta 与计费取自定价页。
- **缺**：无。

### 010 · Fathom — 〇 节齐全

- `ai_mode` ← R 〇 节：「原生（AI-native），但不是整机原生，是记录壳 + AI 脑两段式」。
- `pricing_model` / `free_tier` / `paid_tiers` ← R 9 字段卡原文（Free 0 / Premium 16 / Team 15 / Business 25 / Enterprise 35，每人每月，年付省 25%+，90 day guarantee）。
- `primary_channels` ← 附录 19（七张对比页 + PH 316 条 + 收购媒体波峰 + 集成目录）+ **J** `CHANNEL_*`。
- `moat_hypothesis` ← 附录 2 的 `[推断]` 结论 + **J** `FINAL_MOAT`（「弱到中，三条都可被覆盖」）。
- **缺**：无。⚠️ 提醒：G2 那一页是**同名的财务分析产品**，本行所有事实都**没有**用 G2，避免污染。

### 011 · ElevenLabs — 〇 节齐全

- `ai_mode` ← R 〇 节：「原生（AI-native），整机原生」。
- 定价两格 ← R 9 字段卡原文（六档 + 首月 $1/$11 + 黑五最高省 55% + 额外一分钟 $0.36→$0.17）。
- `primary_channels` ← 附录 19 + **J**；`moat` ← 附录 2 `[推断]` + **J** `FINAL_MOAT`（中偏强、最薄一环是中文）。
- **缺**：无。

### 012 · Gamma — 〇 节齐全

- `ai_mode` ← R 〇 节：「嵌入式（embedded）——实测判定，不是官方说法」。
- 定价两格 ← R 9 字段卡 FAQ 原文（四档 + 400 积分 + 单次 10 页）；**`paid_tiers` 补了「均为年缴折月价」**，依据是同目录 content.json `REVENUE_MODEL_DETAIL`（「四项均为年缴折月价，年缴分别 US$108/216/1080」），避免把 $9 读成月缴价。币种与逐项年缴折扣 README 明写「本次未核实」，故未补。
- `icp_primary` ← R D1（咨询、教育、营销、产品设计四类）；`icp_secondary` ← **J** `SEGMENT_2/3`（产品与营销；教育与内部汇报），把 J 的 SEGMENT_1「咨询/顾问」去掉以免与 primary 重复。
- **缺**：无。⚠️ 本期的 PH 与 G2 **双源全部抓取失败**，README 自己写了「不引用任何评分与原话」；本表因此没有一条来自评论侧的证据，这是材料缺口不是回填缺口。

---

## 4. 缺口汇总（按格数排）

| 排名 | 产品 | 硬缺口 | 软缺口（有替代源兜底） |
|---|---|---|---|
| 1 | **008-cursor** | `未采集` 6 格：icp_secondary、jtbd、ai_mode、pricing_model、primary_channels、moat_hypothesis；`未公开` 2 格：free_tier、paid_tiers | — （空目录，连 content.json 都没有） |
| 2 | **006-claude** | `未公开` 2 格：free_tier、paid_tiers（定价页 JS 渲染，只抓到脚注） | 无 |
| 3 | **001-notion** | 无「未采集」字样，但**结构缺三块**：〇 节、9 字段卡、流量/护城河节——category / 5 个字段 / 渠道 / 护城河全靠 content.json | 5 格 |
| 4 | **002-obsidian** | 结构缺：〇 节、流量节、护城河节 | 4 格（icp_secondary、channels、moat + Catalyst 金额） |
| 5 | **003 / 005** | 结构缺：〇 节（ai_mode 分别取自 D8 / 跨期推断） | 2 格 / 1 格 |
| — | 004 / 007 / 009 / 010 / 011 / 012 | 无 | 0–2 格 |

**另外 3 个「不是缺、但要在合并时留个心」的点：**

1. `003` 与 `007` 的定价是**港币区域价**（访问地决定币种），003 已附官方美元口径，007 的美元价是第三方转述、不作官方口径。
2. `002` / `004` 的 `ai_mode` 写的是「非 AI（官方零 AI）」与「可选层（自带 key）」——不是三值里的任何一个，因为它们真的不属于原生/嵌入/辅助（Obsidian 官方不做 AI，Reflect 的 AI 是可选项而非产品层）。合并知识库时若必须三值，这两行需要人工映射。
3. `004` 的 `primary_channels` 里「GitHub/开源渠道」那条 README 标了 `[推断]`，本格保留了标记；`005` 的「Free Tools 长尾」同理。

---

## 5. 需要 lead 拍板的两件事

1. **008 是重跑还是就这样留在表里？** 现在这 6 个「未采集」会在合并时污染统计。建议重跑 008 期，或把它从历史表里剔出去单列。
2. **001 / 002 用 content.json 兜底，是否接受？** 如果你要求「只认 README」，那 001 的 category、icp 分层、free/paid 数字、channels、moat，以及 002 的 icp_secondary、channels、moat 都要改回「未采集」，表会有 8 格空。我的判断是 content.json 是同一张卡的渲染源、可逐条核对，比留空更有用——但这属于口径问题，你定。
