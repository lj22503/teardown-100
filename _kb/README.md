# _kb · 产品拆解知识库

> 目的：把每期拆解从「一次性 HTML 作品」变成**可检索、可拼接、可复用的判断集**。
> 一句话：**HTML 是给别人看的作品；_kb 是给下一个产品用的零件库。**

---

## 一、三层结构

| 层 | 文件 | 回答什么问题 | 谁来写 |
|---|---|---|---|
| **事实层** | `raw/<产品>-raw.md` | 官方原文说了什么，出处在哪 | 研究员（机器+人） |
| **结构层** | `01-products.csv` `02-atoms.csv` `03-workflows.csv` `04-channels.csv` `05-resources.csv` | 它是谁、由哪些原子组成、组成了什么工作流、靠什么被看见、内置了哪些资源 | 拆解人 |
| **判断层** | `06-problem-to-component.md` `07-patterns.md` | 我遇到这个问题时该拿哪个零件；哪些结构可以搬到我的场景 | 我（燃冰） |

**判断层的三个字段定义**（贯穿结构层）：

| 字段 | 取值 | 含义 |
|---|---|---|
| `reuse_score` 复用价值 | 1–5 | 这个零件搬到别的产品/我自己的场景里，能直接用吗 |
| `migration_cost` 迁移成本 | 1–5（1=很贵） | 换成我的场景要改多少：0 改=5，重写=1 |
| `evidence_strength` 证据强度 | A/B/C | A=官方原文/文档；B=可核实二手；C=推断（必须写依据） |

---

## 二、三种用法（这是建库的理由）

### 1. 做新产品前：先查「别人已经拆过的零件」
- 查 `02-atoms.csv`：这个能力有没有现成原子（别再自己造）
- 查 `03-workflows.csv`：这个场景有没有现成成品组合
- 查 `05-resources.csv`：有没有现成模板/Agent/数据可以直接拿来改

### 2. 做产品设计时：从问题反查零件
- 先查 `06-problem-to-component.md`：我这个问题，别人用什么组件解决的
- 再回 `02/03/05` 看那个组件的实现细节与出处

### 3. 做增长时：抄渠道结构，不抄文案
- 查 `04-channels.csv`：对手用哪种渠道、URL 模式是什么、覆盖多少页
- 查 `07-patterns.md`：这个渠道结构的适用条件与反例

### 4. 要参考某个模板时：先看模块，再点链接
- **不要直接翻 URL**。顺序是：`12-template-fit.md`（适合谁/场景/怎么用）→ `10-template-picker.md`（我要什么模块 → 哪些模板有）→ `09-template-anatomy.md`（完整结构）→ `08-template-modules.csv`（逐模块表格）→ 最后才点 `evidence_url`。
- 这就是「资源三层」：**目录层（05）→ 解剖层（08/09）→ 适配层（11/12）**。目录层回答"有什么"，解剖层回答"里面是什么"，适配层回答"适合谁、什么时候用、怎么用"。

### 5. 给 Agent 用：一句话查库
```bash
python _kb/_tools/ask.py "客户交接"     # 跨表返回：模板/模块/工作流/原子/资源（带出处）
```
或直接 SQL：`sqlite3 _kb/db/kb.sqlite`（表结构见 `_kb/SKILL.md`）。

---

## 三、每次拆完一个产品，最小更新量

1. `raw/<产品>-raw.md`：一份事实底稿（带 URL）
2. `01-products.csv`：+1 行
3. `02-atoms.csv`：+8～15 行（原子能力）
4. `03-workflows.csv`：+5～15 行（官方成品组合）
5. `04-channels.csv`：+3～8 行（渠道）
6. `05-resources.csv`：+5～20 行（资源目录）
7. `08-template-modules.csv`：抓 5–10 个代表模板的模块解剖（跑 `_tools/collect_template_modules.py`）
8. `06-problem-to-component.md`：把新发现的「问题→组件」补进去
9. `07-patterns.md`：只有出现**新结构**时才加，不重复
10. 跑 `_tools/build_picker.py` + `_tools/build_xlsx.py` 重刷索引与 Excel

> 判断：**没有出处的条目一律不进结构层**（宁可空着）；推断条目进结构层必须 `evidence_strength=C` 并写依据。

---

## 四、AI 检索约定（给以后接 Agent 用）

查询顺序固定为：

```
问题 → 06-problem-to-component（找方向）
     → 02-atoms（找零件）
     → 03-workflows（找成品组合）
     → 05-resources（找可直接改的素材）
     → raw（找原文出处）
```

约定：
- 每个返回结果必须带 `evidence_url`；没有 URL 的不返回
- 冲突时以 `evidence_strength=A` 为准
- 「我的判断」永远单独标，不混进事实

---

## 四.5 打开方式（编码，2026-11-26 修）

**症状**：Excel 双击 CSV，中文变成乱码。
**原因**：CSV 写成 UTF-8 **无 BOM**，Excel 在中文 Windows 上按 GBK 解码。

**三种解法（任选）**：
1. **直接开 `知识库.xlsx`**（推荐）：五个 sheet（产品主档 / 原子能力 / 工作流成品 / 流量渠道 / 资源清单），已冻结表头、加筛选、调好列宽。
2. 用 `_csv_bom/` 里的同版本 CSV（带 UTF-8 BOM，Excel 双击正常）。
3. Excel →「数据」→「从文本/CSV」→ 文件原始格式选 **65001: Unicode (UTF-8)**。

**已改**：生成脚本后续统一写 `utf-8-sig`（BOM），新产出的 CSV 不会再乱码。

---

## 四.6 存储：主库是 SQLite，xlsx 只是导出（2026-11-26 改）

**为什么改**：内容会持续变多，单个 Excel 会变成瓶颈（行数、手改冲突、无法查询）。所以：

| 角色 | 文件 | 说明 |
|---|---|---|
| **主库（机器查）** | `db/kb.sqlite` | 7 张表 + FTS5 全文检索；Agent 直接 SQL 查 |
| **索引** | `index.json` | 表结构、行数、产品清单、检索顺序（给程序读） |
| **Agent 说明书** | `SKILL.md` / `llms.txt` | 告诉 Agent 库在哪、怎么查、哪些字段是推断 |
| **人读** | 06 / 09 / 10 三份 md | 问题索引 / 模板解剖 / 按模块反查 |
| **导出快照** | `知识库.xlsx` | 7 个 sheet，给人看/发给别人；**不再作为主库** |

**后续加产品**：更新 CSV → 跑 `_tools/build_db.py` → 主库/index/SKILL 自动刷新；需要 Excel 时再跑 `build_xlsx.py`。

---

## 四.7 自动化与版本管理（2026-11-26 加）

**目标**：改不坏；改坏了能回到上一版；知道每次改了什么。

### 四层防护

| 层 | 做什么 | 文件 |
|---|---|---|
| 1. 写入前快照 | 每个写操作前，整库复制一份 + 每个文件 sha256 | `history/<ts>/manifest.json` |
| 2. 写入后 QA | 主键/出处/行数一致性/ sqlite 完整性，不过就失败 | `automation/qa_gate.py` |
| 3. 失败自动回滚 | 任一步失败 → 自动 restore 到本次开始前 | `automation/run_atom.py` |
| 4. 变更账本 | 每次快照一行；git 负责文本 diff | `CHANGELOG.md` + git |

> 说明：这是「快照 + 校验 + 回滚」，不是数据库事务级；足够防止一次改坏，且每一步可追溯。

### 原子清单（Marvis 只跑这些）

```bash
python _kb/automation/run_atom.py --list        # 看全部原子
python _kb/automation/run_atom.py --group kb    # 每周：全量重建 + 自动 QA
python _kb/automation/run_atom.py --atom kb.qa  # 每天：只体检
python _kb/automation/run_atom.py --episode 015-xxx   # 新增一期
```

| 原子 | 作用 | 写 |
|---|---|---|
| `kb.templates.modules` | 抓模板模块 | 是 |
| `kb.templates.fit` | 抓适合谁/场景/怎么用 | 是 |
| `kb.picker` | 生成按模块反查索引 | 是 |
| `kb.db` | 重建 SQLite/index/SKILL/分产品 JSON | 是 |
| `kb.xlsx` | 导出 Excel 快照 | 是 |
| `kb.qa` | 质量闸 | 否 |
| `kb.snapshot` | 手动打快照 | 是 |
| `episode.*` | 采集/评论/渲染/刷墙 | 是 |

### 回滚与对比

```bash
python _kb/automation/version.py list
python _kb/automation/version.py restore --to <ts>   # 会先备份当前，回滚可逆
python _kb/automation/version.py diff --from <ts1> --to <ts2>
```

**规则**：不手改 01–05.csv；不删 `history/`（保留最近 30 份）；回滚后必须再跑 `kb.qa`。
**Marvis 执行手册**：`automation/MARVIS.md`（每天/每周/每期三套命令 + 报告模板 + 边界）。

---

## 五、和 teardown-100 的关系

```
teardown-100/NNN-slug/     ← 对外作品（HTML、拆解卡）
        ↓ 拆完顺手沉淀
teardown-100/_kb/          ← 对内资产（可检索的判断集）
```

**顺序**：先拆（raw → 结构层），再写报告（HTML）。报告可以只写 3 段，但结构层必须填 —— 否则这一期对下一期没有增量。

---

## 六、当前进度（2026-11-26）

| 期号 | 产品 | raw 底稿 | 深度调研 | 结构层 | HTML |
|---|---|---|---|---|---|
| 013 | Slack | ✅ `raw/slack-raw.md`（305 行） | ✅ `dossiers/slack.md` | ✅ 15 atoms / 10 workflows / 8 channels / 8 resources / **4 个模板已解剖** | ✅ zh 102.7KB / en 106.5KB |
| 014 | Taskade | ✅ `raw/taskade-raw.md`（504 行） | ✅ `dossiers/taskade.md` | ✅ 23 atoms / 16 workflows / 17 channels / 17 resources / **10 个模板已解剖** | ✅ zh 103.5KB / en 107.3KB |

**历史 001–012 回填（2026-11-26）**：12 行已并入 `01-products.csv`（共 14 个产品），每行带定位/ICP/JTBD/定价/AI 类型/渠道/护城河假设。
- 缺口：`008-cursor` 原本就没有 README（只有 _raw 与评论），6 格「未采集」、定价「未公开」——建议重跑 008 期，不要靠回填补。
- `001-notion`、`002-obsidian` 是老格式（无 8 维表/9 字段卡），字段取自同目录 content.json，可追溯。
- `002-obsidian` 的 ai_mode 是「非 AI（官方零 AI）」，`004-reflect` 是「可选层（自带 key）」——没有硬套三值，保留原意。
- 明细：`raw/history-backfill-notes.md`（203 行，逐产品字段来源 + 缺口）。

> **模板层（2026-11-26 扩展）**：从只做 013/014 扩到**全 14 个产品**。
> - `13-template-catalog.csv`（14 行）：每个产品「有没有公开模板库、在哪、多大、能不能拆模块」。
> - `08-template-modules.csv` **95 条模块 / 20 个模板**：Slack 6 + Taskade 6 + **Framer 3** + **Figma 5**（3 个社区文件 + Match UI kit + Material 3 Expressive）。
> - `11-template-fit.csv` **30 条**：外加 Framer 3、Notion 2、Figma 8（含 3 个 Weave workflow）、Gamma 3。
> - 明确没有公开模板库的：Obsidian、Capacities、Reflect、Fathom、HyNote；Gamma 有库但**详情页没有模块清单**（只做适配）；Figma 是 SPA，模块来自页面描述/搜索摘要（B 级）；Notion 登录后 `About this template` 仍为空（只做适配）。
> - 未解剖 4 个（页面无结构区）：Slack Bug Tracker、Slack Incident Summary、Taskade AI Project Dashboard、Taskade Expense Tracker。
>
> **标签结构（Taxonomy，2026-11-26 加）**：`15-template-taxonomy.csv` / `16-template-taxonomy.md`，117 行，回答「这个平台有哪些板块/类别/主题/风格，agent 去哪找」。
> - **Gamma**：格式 4（演示文稿/文档/社交轮播卡片/网页）、类别 19（课程 223 / 提案 183 / 营销材料 173 / 报告 166 / 融资演讲稿 154 …）、主题 18（商业 361 / 教育 293 / 艺术 216 …）、风格 16（视觉 454 / 醒目 363 / 插画风格 315 …）。
> - **Notion**：市集 6 入口（探索/模板/代理/顾问/技能/连接）、模板范围 3（工作/生活/学校）、Use Case 25（市场营销/金融/咨询/设计/销售/工程…）、技能分类与示例。
> - **Figma**：资源板块 12（AI workflows / Website templates / UI kits / Skills / Presentations / Assets …）、AI workflows 子类 4（Product & brand / Marketing / Character & narrative / Ideation）。

> 本期重点：**两份 dossier 是按「定位 / AI 构建 / 流量渠道 / 资源清单」四段写的**，可以直接当 013、014 两期报告的素材源；HTML 只是排版，不再是唯一的产出。

**本期修正记录（写进来，避免下次再错）**：
1. Taskade sitemap 总量：我初算 ≈32,600 → **实测 28,602**（研究员逐个拉 17 个子 sitemap 相加）；结构占比 程序化 64.2% / UGC 21.4% / 手写 14.3%。
2. `Note/Doc`、`Mind Map` 不是独立对象，是 **project 的两种视图**（02-atoms 已从"容器"改为"界面（视图）"）。
3. 集成数：官方口径 100+，**实测 173 个 / 6 类**（以实测为准，注明两个口径）。
4. `/compare` 197 页的真实结构：**155 页 `free-<竞品>-alternative` + 33 页纯模型对比 + 6 页 `taskade-vs-*`**——是吃搜索量，不是品牌对比。
5. 定价补全：Business $25 / Max $100 / Enterprise $250（年付折算月价），年付省 50%。
6. 模板层从"只有 URL"改为**三层**：目录（05）→ 解剖（08/09）→ 适配（11/12）；适配表补了「适合谁 / 场景 / 怎么用」。
7. 主库从 Excel 改为 **SQLite（db/kb.sqlite）+ 分产品 JSON**；xlsx 降级为导出快照。

---

## 七、文件清单

```
_kb/
├── README.md                     ← 本文件
├── SKILL.md / llms.txt           ★ 给 Agent 的说明书（查什么、怎么查）
├── index.json                    ★ 机器索引（表结构/行数/产品清单）
├── CHANGELOG.md                  ★ 变更账本（每次快照一行）
├── db/kb.sqlite                  ★ 主库（9 表 + FTS5 全文检索）
├── history/                      ★ 快照（每个文件 sha256 + manifest，保留 30）
├── automation/                   ★ 原子执行器 + QA + 版本 + Marvis 手册
│   ├── atoms.json                原子清单（kb / episode 两组）
│   ├── run_atom.py               执行器（自动快照/失败回滚）
│   ├── qa_gate.py                质量闸
│   ├── version.py                快照/回滚/对比
│   └── MARVIS.md                 Marvis 执行手册
├── 知识库.xlsx                   ← 导出快照（9 sheet，给人看，不是主库）
├── 01-products.csv               产品主档
├── 02-atoms.csv                  原子能力库（143 条）
├── 03-workflows.csv              工作流成品组合（81 条）
├── 04-channels.csv               流量渠道（25 条）
├── 05-resources.csv              资源目录（81 条）
├── 08-template-modules.csv       模板解剖（95 条模块 / 20 个模板）
├── 09-template-anatomy.md        逐模板结构（含 Framer / Figma）
├── 10-template-picker.md         按模块反查模板
├── 11-template-fit.csv           ★ 模板适配（30 条：适合谁/场景/怎么用/价值）
├── 12-template-fit.md            ★ 上表的人读版
├── 13-template-catalog.csv       ★ 模板目录（14 个产品：有没有/在哪/多大/能否拆）
├── 14-template-catalog.md        ★ 目录人读版
├── 15-template-taxonomy.csv      ★ 标签结构（Gamma/Notion/Figma 的板块/类别/主题/风格，117 行）
├── 16-template-taxonomy.md       ★ 标签结构人读版 + agent 导航`n├── 17-resource-audit.md          ★ 资源层深度审计（001–014）
├── data/                         ★ 历史模板源数据（merge 用，勿手改 08/11）
│   ├── history-template-modules.csv
│   └── history-template-fit.csv
├── _csv_bom/                     带 UTF-8 BOM 的 CSV 备份（Excel 双击正常）
├── 06-problem-to-component.md    问题 → 组件索引
├── 07-patterns.md                可复用模式（7 个）
├── dossiers/
│   ├── slack.md                  013 深度调研
│   └── taskade.md                014 深度调研
├── raw/
│   ├── slack-raw.md              013 事实底稿（305 行）
│   ├── taskade-raw.md            014 事实底稿（504 行）
│   └── history-products-rows.csv 历史 001–012 回填（已并入 products）
└── _tools/
    ├── fill_slack_taskade.py     结构层生成
    ├── collect_template_modules.py 模板模块抓取
    ├── collect_template_fit.py   模板适配抓取（适合谁/场景/怎么用）
    ├── build_picker.py           按模块反查索引
    ├── build_db.py               CSV → SQLite + index/SKILL/llms
    ├── build_catalog.py          模板目录生成
    ├── build_taxonomy.py         标签结构生成
    ├── build_anatomy_md.py       模板解剖 md
    ├── build_fit_md.py           模板适配 md
    ├── merge_templates.py        历史模板并入 08/11
    ├── build_xlsx.py             CSV → xlsx 导出 + BOM 备份
    ├── ask.py                    ★ 一句话跨表检索（Agent 入口）
    ├── ask_demo.py               检索演示（UTF-8 关键词）
    └── test_query.py             主库检索自测
```




