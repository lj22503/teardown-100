# -*- coding: utf-8 -*-
"""生成 teardown-100 的 README 进度墙 + 同步已完成的拆解资产。
用法：python _tools/build_wall.py
数据源：_data/queue.csv（100 条队列）+ 各产品目录是否存在
"""
import os, csv, shutil, sys, json, io
sys.stdout.reconfigure(encoding="utf-8")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE = os.path.join(REPO, "_data", "queue.csv")

def load_queue():
    rows = []
    with open(QUEUE, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r.get("no", "").strip():
                rows.append(r)
    return rows

def folder_of(r):
    n = int(r["no"])
    slug = r["slug"]
    return "%03d-%s" % (n, slug)

def done_set():
    out = {}
    for d in os.listdir(REPO):
        p = os.path.join(REPO, d)
        if os.path.isdir(p) and len(d) > 3 and d[:3].isdigit() and "-" in d:
            out[int(d[:3])] = d
    return out

def main():
    rows = load_queue()
    done = done_set()
    total = len(rows)
    completed = sum(1 for r in rows if int(r["no"]) in done)
    pct = (completed / total * 100) if total else 0

    lines = []
    lines.append("# 拆解 100 个 AI+产品")
    lines.append("")
    lines.append("> 每天拆一个 AI 产品：**可核实的事实 + 一手实测 + 明确标注的判断**。")
    lines.append("> 不给假精度，不把推断说成事实。")
    lines.append("")
    lines.append("**进度：%d / %d（%.0f%%）**" % (completed, total, pct))
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 进度墙")
    lines.append("")
    lines.append("✅ = 已拆（点进目录看报告）· ⬜ = 在队列里")
    lines.append("")
    lines.append("|  |  |  |  |  |  |  |  |  |  |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    cell_by_no = {}
    for r in rows:
        n = int(r["no"])
        name = r["name"].replace("|", "/")
        if n in done:
            cell_by_no[n] = "✅ [%s](%s/)" % (name, done[n])
        else:
            cell_by_no[n] = "⬜ %s" % name
    for start in range(1, total + 1, 10):
        cells = [cell_by_no.get(i, "") for i in range(start, min(start + 10, total + 1))]
        cells += [""] * (10 - len(cells))
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 每篇怎么看")
    lines.append("")
    lines.append("| 文件 | 内容 |")
    lines.append("|---|---|")
    lines.append("| `teardown-zh.html` | 中英双语产品拆解报告（15 段：快照 / JTBD / 核心循环 / 架构 / 手艺 / 体验 / 商业模式 / 竞品 / 增长 / AI 就绪度 / 指标 / 摩擦 / 风险 / 机会 / 终局） |")
    lines.append("| `teardown-en.html` | 英文版 |")
    lines.append("| `README.md` | 拆解卡：8 维度 + 9 字段 + 用户评论证据 |")
    lines.append("| `实测.md` | 体验者的一手记录 |")
    lines.append("")
    lines.append("## 三条规矩")
    lines.append("")
    lines.append("1. **事实只写可核实的**（官网 / 定价页 / 帮助中心 / 用户评论），并在报告末尾附来源链接。")
    lines.append("2. **未公开的写推断，但必须标 `[推断]` 并写依据**；不写假精度数字。")
    lines.append("3. **一手体验署名**（体验者：燃冰），不冒充他人实测。")
    lines.append("")
    lines.append("## 目录说明")
    lines.append("")
    lines.append("```")
    lines.append("_data/queue.csv      100 个产品的队列（含分类、PH 链接）")
    lines.append("_tools/build_wall.py 重新生成本 README 的进度墙")
    lines.append("NNN-slug/            每个产品的报告目录")
    lines.append("```")
    lines.append("")
    lines.append("## 联系")
    lines.append("")
    lines.append("- 公众号 / 小红书：拆解100个AI+产品")
    lines.append("- 有想看的 AI 产品，开 issue 点单。")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*内容许可：CC BY-NC-SA 4.0（署名 · 非商业 · 相同方式共享）。引用请注明来源。*")
    out = "\n".join(lines) + "\n"
    with open(os.path.join(REPO, "README.md"), "w", encoding="utf-8") as f:
        f.write(out)
    print("README written: %d/%d done" % (completed, total))
    for r in rows:
        if int(r["no"]) in done:
            print("  done:", done[int(r["no"])])

if __name__ == "__main__":
    main()
