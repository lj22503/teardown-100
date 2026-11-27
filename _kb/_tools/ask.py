# -*- coding: utf-8 -*-
"""最小检索入口：给一个关键词，跨表返回最相关的结果（带出处）。
用法：python _tools/ask.py "客户交接"
"""
import sqlite3, os, sys, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(BASE, "db", "kb.sqlite")

def terms(kw):
    out = [kw]
    # 只有中文才做 2 字切片；英文切片会把 onboarding 拆成 on/bo/ar… 命中一切
    if len(kw) >= 4 and " " not in kw and re.search(r"[\u4e00-\u9fff]", kw):
        out += [kw[i:i+2] for i in range(0, len(kw)-1, 2)]
    return list(dict.fromkeys(out))

def fetch(con, table, match_cols, out_cols, ts, limit=5):
    where, args = [], []
    for t in ts:
        for c in match_cols:
            where.append(f"{c} like ?")
            args.append(f"%{t}%")
    sql = f"select {', '.join(out_cols)} from {table} where ({' or '.join(where)}) limit {limit}"
    return list(con.execute(sql, args))

def run(kw):
    ts = terms(kw)
    con = sqlite3.connect(DB)
    print(f"\n=== 查询：{kw} ===")

    print("\n[1] 模板：适合谁 / 场景 / 怎么用")
    rows = fetch(con, "template_fit",
                 ["template_name", "for_whom", "scenario", "how_to_use", "value"],
                 ["template_name", "product", "for_whom", "scenario", "how_to_use", "evidence_url"], ts)
    for r in rows:
        print(f"  - {r[0]}（{r[1]}）｜适合：{r[2]}｜场景：{r[3]}")
        print(f"    怎么用：{(r[4] or '')[:110]}...")
        print(f"    出处：{r[5]}")
    if not rows: print("  （无）")

    print("\n[2] 模板模块")
    rows = fetch(con, "template_modules", ["module_name", "detail", "module_type"],
                 ["template_name", "product", "module_name", "module_type", "detail", "evidence_url"], ts, 6)
    for r in rows:
        print(f"  - {r[1]} · {r[2]}（{r[3]}）：{(r[4] or '')[:100]}")
        print(f"    出处：{r[5]}")
    if not rows: print("  （无）")

    print("\n[3] 工作流")
    rows = fetch(con, "workflows", ["workflow_name", "steps", "atoms_used", "output"],
                 ["workflow_name", "product", "atoms_used", "steps", "evidence_url"], ts)
    for r in rows:
        print(f"  - {r[0]}（{r[1]}）｜原子：{r[2]}")
        print(f"    步骤：{(r[3] or '')[:110]}...")
        print(f"    出处：{r[4]}")
    if not rows: print("  （无）")

    print("\n[4] 原子能力")
    rows = fetch(con, "atoms", ["atom_name", "what_it_does", "composable_with"],
                 ["product", "atom_name", "atom_type", "what_it_does", "evidence_url"], ts, 6)
    for r in rows:
        print(f"  - {r[0]} · {r[1]}（{r[2]}）：{(r[3] or '')[:100]}")
        print(f"    出处：{r[4]}")
    if not rows: print("  （无）")

    print("\n[5] 资源")
    rows = fetch(con, "resources", ["resource_name", "problem_solved", "reuse_form"],
                 ["product", "resource_name", "resource_type", "problem_solved", "evidence_url"], ts)
    for r in rows:
        print(f"  - {r[0]} · {r[1]}（{r[2]}）：{(r[3] or '')[:80]} → {r[4]}")
    if not rows: print("  （无）")

    con.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python ask.py <关键词>")
    else:
        run(sys.argv[1].strip())

