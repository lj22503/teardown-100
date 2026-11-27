# Marvis 执行手册（知识库自动化）

> 你是这套知识库的**执行者**，不是作者：只跑原子、看结果、报数字，不手改数据文件。
> 入口：`python _kb/automation/run_atom.py`

---

## 一、先看有哪些原子

```bash
python _kb/automation/run_atom.py --list
```

| 原子 | 作用 | 写不写 |
|---|---|---|
| `kb.templates.modules` | 抓模板模块（What's Included / Template features） | 写 |
| `kb.templates.fit` | 抓模板适配（适合谁 / 场景 / 怎么用） | 写 |
| `kb.picker` | 生成「按模块反查」索引 | 写 |
| `kb.db` | 重建 SQLite + index/SKILL/llms + 分产品 JSON | 写 |
| `kb.xlsx` | 导出 Excel 快照 | 写 |
| `kb.qa` | 质量闸（主键/出处/行数一致性） | 只读 |
| `kb.snapshot` | 打快照 + CHANGELOG | 写 |
| `episode.collect_pages` | 采某期官网/定价页 | 写 |
| `episode.collect_reviews` | 采某期 PH/G2 评论 | 写 |
| `episode.render` | 渲染某期中英 HTML | 写 |
| `episode.wall` | 刷进度墙 | 写 |

---

## 二、日常任务（照做即可）

### 每天（1 分钟）
```bash
python _kb/automation/run_atom.py --atom kb.qa
```
- 退出码 0：回一句「知识库正常，products=14 / atoms=38 / templates=14」。
- 退出码 1：把 ERROR 那几行原样贴给燃冰，**不要自己改文件**。

### 每周（5 分钟）
```bash
python _kb/automation/run_atom.py --group kb
```
这会依次：抓模板模块 → 抓模板适配 → 生成索引 → 重建 DB → 导出 xlsx → QA。
- 全部成功：报「本周知识库已重建，快照 <ts>，counts: ...」。
- 任一步失败：执行器会**自动回滚**到本次开始前的快照，并打印 `!! 失败，回滚到 ...`；把这行和日志路径贴出来。

### 新增一期（每期一次）
```bash
python _kb/automation/run_atom.py --episode 015-xxx
```
（采集 → 评论 → 渲染 → 刷墙；跑完再跑 `--group kb` 同步知识库）

---

## 三、失败与回滚（必须会）

```bash
# 看历史快照
python _kb/automation/version.py list

# 回到某个快照（会先自动备份当前状态，回滚本身可逆）
python _kb/automation/version.py restore --to 20261126-101500-123

# 对比两个快照改了什么
python _kb/automation/version.py diff --from <ts1> --to <ts2>
```

规则：
1. **不要手改 `01–05.csv`**；改数据只通过原子或明确的人工脚本。
2. **不要删 `_kb/history/`**；最多保留 30 份，旧的自动作废。
3. 回滚后必须再跑一次 `kb.qa`，确认 0 errors。

---

## 四、报告模板（发给燃冰）

```
【知识库】<日期>
- 动作：kb.qa / kb 全量 / episode 015
- 结果：通过 / 失败（已回滚到 <ts>）
- counts：products=14 atoms=38 workflows=26 channels=25 resources=25 template_modules=51 template_fit=14
- 日志：_kb/logs/<file>.log
```

---

## 五、边界

- 你只执行 `atoms.json` 里定义的命令；**不要即兴写新脚本**。
- 不碰 `_tools/`（渲染模板）与 `teardown-100/NNN-*/content.json`（内容由燃冰/DSH 写）。
- 发现数据错了：标出来，不直接改；让 DSH 修脚本后重跑。
