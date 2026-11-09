# content.json 字段规范

> 一份 content.json 驱动一中一英两页报告。
> 键名必须和 `_tools/template-zh.html` / `template-en.html` 里的 `{{占位符}}` 完全一致（大小写敏感）。
> 缺 key 不会报错，但页面上会留空 —— 所以**先跑 `build_teardown.py` 看残留占位符数**。

## 顶层字段（脚本用）

| 字段 | 说明 | 例 |
|---|---|---|
| `product` | 产品名 | `"Notion"` |
| `product_label` | 报告里显示的完整名（可含 AI 后缀） | `"Notion AI"` |
| `date` | 生成日期 | `"2026-11-09"` |
| `zh` | 中文文案字典 | `{ "PRODUCT": "...", ... }` |
| `en` | 英文文案字典 | 键与 zh 相同 |
| `sources_zh` / `sources_en` | 来源列表 `[[标签, 链接], ...]` | 见下 |
| `metrics_zh` / `metrics_en` | 「关键信号」三卡的 HTML 片段（可选） | 见下 |

## 文案字段的 16 组（对应报告 15 段 + 头部）

| 组 | 主要键（节选） | 注意 |
|---|---|---|
| 头部 | `PRODUCT` `ONE_LINER_2_LINE_SUBTITLE` `CATEGORY` `USER_SCALE` `STAGE_MATURITY` `BUSINESS_MODEL_SHORT` `DATE_YYYY_MM_DD` | 一句话定位必须是判断，不是描述 |
| 判断区 | `VERDICT_ONE_LINER` `VERDICT_BODY_2_3_LINES` `TLDR_1..3_HEADLINE/BODY` | 只写三件事，多写没人看 |
| §1 快照 | `SNAPSHOT_ONE_TO_TWO_SENTENCE_DEFINITION` `USER_PROMISE` `SEGMENT_1..3_NAME/DETAIL` | 优先引官方原话 |
| §2 JTBD | `JTBD_FUNCTIONAL/EMOTIONAL/SOCIAL` `TRIGGER_MOMENT` `FREQUENCY` `USAGE_CONTEXT` | 情绪 JTBD 要写人话 |
| §3 循环 | `LOOP_TRIGGER/ACTION/REWARD/RETURN_TITLE/DETAIL` `ACQUISITION_LOOP_DETAIL` `AHA_MOMENT_DETAIL` `VIRALITY_DETAIL_OR_NONE` `RETENTION_1..3` `GROWTH_LOOP_1..2_NAME/DETAIL` | 循环要能一句话讲完 |
| §4 架构 | `SURFACE_1..6_NAME/ROLE` `ENTITY_1..5` `IA_LOGIC_PARAGRAPH` `NAV_INTERACTION_PARAGRAPH` | 只写真的点得到的东西 |
| §5 手艺 | `CRAFT_1..5_NAME/DETAIL` `CRAFT_PRINCIPLE` | 要具体到能抄的做法，不写形容词 |
| §6 体验 | `TTV_*` `COG_*` `DELIGHT_*` `TRUST_*` `STRUGGLE_*` `STRUGGLE_1..3` | **默认隐藏条形分**，只留文字 |
| §7 商业 | `REVENUE_MODEL_NAME/DETAIL` `MON_ENTRY_*` `FREE_PAID_*` `UX_MON_*` | 数字必须能在定价页找到 |
| §8 竞品 | `COMP_DIM_1..4` `COMP_1..4_NAME/D1..D4` `COMP_OWN_D1..D4` `COMP_INTRO` `COMP_WHERE_OWN_WINS` `COMP_WHERE_RIVALS_CATCH` | 标注「主观判断，不是评分」 |
| §9 增长 | `CHANNEL_1..3` `HORIZONTAL/VERTICAL/PLATFORM_1..2` | 官网没写的标「未披露」 |
| §10 AI | `ACTIVE_IF_ASSISTIVE/EMBEDDED/AUTONOMOUS` `CURRENT_AI_USAGE_PARAGRAPH` `AGENTIC_CANDIDATE_1..3` `AI_OPPORTUNITY_1..2` `AI_DISRUPTION_RISK` | 三选一填 `active`，另外两个留空 |
| §11 指标 | `METRICS_INTRO` `NORTH_STAR_METRIC/WHY` `INPUT_METRIC_1..3_NAME/WHY` `GUARDRAIL_*` `METRIC_BLINDSPOT*` | 未公开→标 `[推断]` + 依据 |
| §12 摩擦 | `FRICTION_1..4_TITLE/BODY` | 每条对应一条评论证据 |
| §13 风险 | `RISK_1..4_NAME/CAT/SEV/SEV_CLASS/LIK/MIT` | `SEV_CLASS` 只能是 `high`/`med`/`low` |
| §14 机会 | `OPP_1..3_HEADLINE/DETAIL` `STRATEGIC_*` `MOONSHOT_*` | 每条前缀「（我的判断）」 |
| §15 终局 | `FINAL_WINS` `FINAL_BREAKS` `FINAL_MOAT_OR_LACK_THEREOF` `MOAT_SCORE` `MOAT_REASONING_ONE_LINE` | 护城河要敢说"没有" |
| 截图 | `SHOT_1..6_URL/CAPTION` | 只用可热链原图 |
| 语言切换 | `LANG_ZH_HREF` `LANG_EN_HREF` `ACTIVE_IF_ZH` `ACTIVE_IF_EN` | 固定写法，别改 |

## 来源怎么写

```json
"sources_zh": [
  ["产品功能页", "https://example.com/features"],
  ["定价", "https://example.com/pricing"],
  ["用户评论 · G2", "https://www.g2.com/products/xxx/reviews"]
]
```

## 关键信号三卡怎么写

```json
"metrics_zh": "  <div class=\"num-card\">\n    <div class=\"label\">价值到达时间</div>\n    <div class=\"big\">未测</div>\n    <div class=\"desc\">为什么未测</div>\n  </div>"
```

三张卡固定是：价值到达时间 / 核心循环频次 / 护城河评分。
**未公开的一律写「未公开」或「未测」，不要编数字。**

## 硬性约定

- 中文文件统一 UTF-8（无 BOM）
- 键名大小写必须与模板一致（含 `STAR_ROW_e_g_★★★★☆` 这种小写键）
- `[推断]`、`（我的判断）`、`我的评分，不是测量` 三种标注不能省
