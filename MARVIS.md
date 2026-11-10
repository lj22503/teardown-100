# Marvis 执行手册（每日拆解）

> 这份文件是给 Marvis 的。人不用照着做，人只做一件事：按任务单实测 20 分钟。
> 所有"判断"都在脚本里，你只需要按顺序跑命令、照抄输出。

## 一条铁律

**任何命令输出 `ERROR=` 或以非零退出码结束，立刻停止，只回复那一行错误，不许继续下一步，不许换方案，不许跳到下一篇。**

## 每日五步

### 第 1 步 · 问今天做哪篇

```
cd D:\claudework\teardown-100
python _tools\daily.py next
```

读最后一行 `RESULT={...}`：
- `state=need_start` → 这篇还没采集，走第 2 步
- `state=need_report` → 素材齐了，跳到第 4 步
- `state=all_done` → 全部完成，今天就结束

**不要自己看目录猜进度，一切以这条命令为准。**

### 第 2 步 · 采集

```
python _tools\daily.py collect <no> --site <官网> --pricing <定价页>
```

`--site` 和 `--pricing` 自己找，通常挂在 Product Hunt 产品页的 Visit website 上。找不到就只传 `--site`，不许瞎填。

成功会输出 `RESULT={"ok": true, "step": "collect", ...}`，目录里会出现 `_raw.md`、`<slug>-评论.md`、`<slug>-G2评论.md`。

### 第 3 步 · 停下来，等人工实测

采集完先别往下走，回复一句：

> 第 N 篇 <产品> 素材齐了，请在 Obsidian 的 03-Resources\product sense\01-拆解\ 写 20 分钟实测，写完回我一句。

**没有实测就不许写体验结论，不许编用时、不许编评分。**

### 第 4 步 · 写卡与文案（这是唯一需要你动脑的部分）

按 `PIPELINE.md` 第 5 步和第 6 步：
- 写 `<dir>\README.md`：8 维度 + 9 字段 + 评论证据
- 写 `<dir>\content.json`：中英两套 + 来源 ≥10 条 + metrics 三卡 + 附录四段（16 竞品地图 / 17 竞品技术底座 / 18 可迁移机会 / 19 流量与变现）

字段规范看 `_tools\CONTENT-SCHEMA.md`，可以直接抄上一篇的 `content.json` 改。

三条不能破：
1. 事实只写可核实的，末尾必须有来源链接
2. 未公开的写 `[推断]` 并给依据，不写假精度
3. 实测署名「实测（燃冰）」，没有实测就写「未实测」，不许编

### 第 5 步 · 渲染、刷墙、提交

```
python _tools\daily.py build <no>
python _tools\daily.py commit <no>
```

`build` 必须看到 `残留占位符=0`。有残留就是 content.json 缺字段，回去补，不许硬提交。

### 第 6 步 · 发 IMA（你的活）

把这两个文件发到 IMA 知识库「拆解100个AI＋产品」：
- `<dir>\README.md`
- `<dir>\teardown-zh.html`

正文按原文，不许改文案。

## 输出格式

每次执行完，固定三行，不多写：

```
今天：第 N 篇 <产品>（<state>）
结果：<完成到哪一步>
下一步：<等实测 / 已发 IMA / 报错原因>
```

## 常见失败与处理

| 报错 | 原因 | 怎么办 |
|---|---|---|
| `选题器跑不通` | 队列文件被改坏 | 停下，报给老板，不要自己补队列 |
| `采集失败` | ego-browser 不可用 / 页面打不开 | 停下，把错误原文贴出来 |
| `缺 content.json` | 第 4 步没做 | 回去写 content.json |
| `残留占位符=x` | content.json 缺 key | 按提示的 key 名补 |
| `git push 失败` | 网络或凭证 | 停下，报给老板，不要 force push |

## 一句话总结

**判断交给脚本（next / build / commit），动脑只做一件事（写卡和文案），体验交给老板。**
