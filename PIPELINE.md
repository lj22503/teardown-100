# 拆解流水线（PIPELINE）

> 目标：**加一篇新产品 = 写一个目录 + 一份 content.json，跑两条命令。**
> 产品、文案、模板、脚本全部分离，谁都不改谁的。

## 目录约定

```
teardown-100/
├── README.md                进度墙（脚本生成，别手改）
├── _data/queue.csv           100 个产品队列（no, slug, name, tagline, category, url）
├── _tools/
│   ├── template-zh.html      报告模板（中文）
│   ├── template-en.html      报告模板（英文）
│   ├── build_teardown.py     渲染：content.json → teardown-{zh,en}.html
│   ├── build_wall.py         重刷 README 进度墙
│   ├── collect-product.mjs   采集官网/定价/演示页（ego-browser）
│   ├── collect-ph-reviews.mjs 采集 Product Hunt 评论（含 1-2 星）
│   ├── collect-g2-reviews.mjs 采集 G2 评论（Lowest Rated + dislike 字段）
│   └── EXPERIENCE.md         实测清单（人做，20 分钟）
└── NNN-slug/
    ├── README.md             拆解卡（8 维 + 9 字段 + 评论证据）
    ├── content.json          报告文案（中英两套 + 来源 + 关键信号卡）
    ├── teardown-zh.html      生成物
    └── teardown-en.html      生成物
```

## 一篇的 7 步

| # | 谁做 | 动作 | 产物 / 命令 |
|---|---|---|---|
| 1 | 机器 | 从队列取下一个未拆的产品 | `_data/queue.csv` |
| 2 | 机器 | 采产品页、定价、演示页原文 | `_tools/collect-product.mjs` → `<dir>/_raw.md` |
| 3 | 机器 | 采评论：PH + G2 | `collect-ph-reviews.mjs` / `collect-g2-reviews.mjs` → `<dir>/_reviews.md` |
| 4 | **人** | 照 `_tools/EXPERIENCE.md` 实测 20 分钟 | `<dir>/实测.md` |
| 5 | 机器+人 | 写拆解卡（8 维 + 9 字段 + 评论证据） | `<dir>/README.md` |
| 6 | 机器 | 写内容文件（中英两套文案 + 来源） | `<dir>/content.json` |
| 7 | 机器 | 渲染 + 刷墙 + 提交 | `python _tools/build_teardown.py NNN-slug` → `python _tools/build_wall.py` → `git commit` |

## 质量闸（发之前逐条过）

- [ ] 报告里 **0 个** `{{占位符}}`（脚本会打印残留数）
- [ ] 末尾引用来源 **≥10 条**，且每条能打开
- [ ] 事实层每句都能在来源里找到对应
- [ ] 推断处有 `[推断]` + 推断依据
- [ ] 主观评分标「我的评分，不是测量」
- [ ] 没有假精度数字（如"1,398 条"式的伪精确）
- [ ] 实测归属写明「实测（燃冰）」，不冒充他人
- [ ] 页脚只有署名，没有外部品牌/社交链接

## 三条硬规矩（写进内容层的）

1. **事实只写可核实的**：官网 / 定价页 / 帮助中心 / 用户评论，末尾附来源。
2. **未公开的写推断，但必须标 `[推断]` + 依据**；不写假精度。
3. **一手体验署名**，不冒充他人实测。

## 加一篇新产品的实际工作量

1. 建目录 `NNN-slug/`
2. 抄 `001-notion/content.json` 改文案（zh/en 两套，共约 250 个字段，但大部分可以沿用上一次的句式）
3. 跑 `build_teardown.py`，看残留占位符
4. 跑 `build_wall.py`，commit

> 文案字段太多时，**先只填事实相关的段落**，其余留空也能出页（空字符串不会报错），之后再补。

## 常见故障

| 症状 | 原因 / 处理 |
|---|---|
| 页面出现 `{{XXX}}` | content.json 缺该 key，按提示补 |
| 图挂掉 | `SHOT_n_URL` 必须是可热链的 `images.ctfassets.net` 原图 |
| 进度墙不更新 | 目录名必须是 `NNN-slug`，且 `_data/queue.csv` 里有对应 no |
| 中文乱码 | 所有文件统一 UTF-8（无 BOM），Python 写文件显式 `encoding="utf-8"` |

## 发布交接（谁接手做什么）

| 环节 | 谁做 | 交接物 |
|---|---|---|
| 每日提醒 | Marvis | 一句话提醒 + 本 PIPELINE 路径 |
| 采集 → 卡片 → content.json → 渲染 → 提交 | 我（DSH） | 仓库里的 `NNN-slug/` |
| IMA 知识库同步 | Marvis | `<dir>/README.md` + `<dir>/teardown-zh.html` |
| 公众号 / 小红书 / 知乎 改写 | 我（DSH） | `<dir>/` 作为唯一素材源 |

> 边界：我只写仓库，不碰 IMA；Marvis 只做提醒与 IMA 同步，不改文案。素材永远以仓库里的 `<dir>/` 为准。