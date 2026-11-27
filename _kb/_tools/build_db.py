# -*- coding: utf-8 -*-
"""把 _kb 的 CSV 汇入 SQLite（主库），并生成 index.json / SKILL.md / llms.txt。
Xlsx 降级为导出快照，不再是主库。
"""
import csv, os, json, sqlite3, datetime

BASE = r"D:\claudework\teardown-100\_kb"
DB_DIR = os.path.join(BASE, "db")
os.makedirs(DB_DIR, exist_ok=True)
DB = os.path.join(DB_DIR, "kb.sqlite")

TABLES = [
    ("products",         "01-products.csv"),
    ("atoms",            "02-atoms.csv"),
    ("workflows",        "03-workflows.csv"),
    ("channels",         "04-channels.csv"),
    ("resources",        "05-resources.csv"),
    ("template_modules", "08-template-modules.csv"),
    ("template_fit",     "11-template-fit.csv"),
    ("template_catalog", "13-template-catalog.csv"),
    ("template_taxonomy", "15-template-taxonomy.csv"),
]

def read_csv(name):
    path = os.path.join(BASE, name)
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        return [], []
    header = rows[0]
    body = [r for r in rows[1:] if r and len(r) == len(header)]
    return header, body

if os.path.exists(DB):
    os.remove(DB)
con = sqlite3.connect(DB)
cur = con.cursor()
counts = {}
columns = {}

for table, fname in TABLES:
    if not os.path.exists(os.path.join(BASE, fname)):
        continue
    header, rows = read_csv(fname)
    cols = ", ".join('"%s" TEXT' % h.replace('"', '""') for h in header)
    cur.execute('CREATE TABLE "%s" (%s)' % (table, cols))
    ph = ", ".join(["?"] * len(header))
    cur.executemany('INSERT INTO "%s" VALUES (%s)' % (table, ph), rows)
    cur.execute('CREATE INDEX "idx_%s_1" ON "%s" ("%s")' % (table, table, header[0]))
    counts[table] = len(rows)
    columns[table] = header
    print(table, len(rows), "rows")

# 全文检索表（跨表）
cur.execute("CREATE VIRTUAL TABLE search_fts USING fts5(tbl, rid, title, body, url)")
fts_rows = []
for r in read_csv("01-products.csv")[1]:
    fts_rows.append(("products", r[0], r[2], " ".join(r[1:]), r[17] if len(r) > 17 else ""))
for r in read_csv("02-atoms.csv")[1]:
    fts_rows.append(("atoms", r[0], r[2], " ".join(r[1:]), r[6] if len(r) > 6 else ""))
for r in read_csv("03-workflows.csv")[1]:
    fts_rows.append(("workflows", r[0], r[2], " ".join(r[1:]), r[8] if len(r) > 8 else ""))
for r in read_csv("05-resources.csv")[1]:
    fts_rows.append(("resources", r[0], r[2], " ".join(r[1:]), r[10] if len(r) > 10 else ""))
for r in read_csv("11-template-fit.csv")[1]:
    fts_rows.append(("template_fit", r[0], r[2], " ".join(r[3:9]), r[9] if len(r) > 9 else ""))
cur.executemany("INSERT INTO search_fts (tbl, rid, title, body, url) VALUES (?,?,?,?,?)", fts_rows)
con.commit()
print("fts rows:", len(fts_rows))

# index.json
index = {
    "name": "teardown-100-kb",
    "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    "db": "db/kb.sqlite",
    "counts": counts,
    "tables": {t: {"columns": columns[t], "rows": counts[t]} for t in counts},
    "products": [{"no": r[0], "slug": r[1], "name": r[2], "category": r[3], "one_liner": r[4]}
                 for r in read_csv("01-products.csv")[1]],
    "query_order": ["problem-to-component (md)", "template_fit", "template_modules", "atoms", "workflows", "resources", "raw"],
    "notes": "所有条目均带 evidence_url；无出处条目不入库。判断类字段标 fit_basis / evidence_strength。",
}
with open(os.path.join(BASE, "index.json"), "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)
print("index.json written")

# SKILL.md
skill = f"""---
name: teardown-100-kb
description: 100 个 AI 产品拆解的知识库（Slack / Taskade 已入库）。当需要查「某个产品怎么定位、由哪些原子能力组成、工作流怎么拼、靠什么渠道获客、有哪些模板可参考（适合谁/什么场景/怎么用）」时使用。数据在 db/kb.sqlite 与同名 CSV/MD。
---

# Teardown-100 知识库

## 数据在哪
- **主库（推荐查询）**：`db/kb.sqlite`（SQLite，含 7 张表 + 全文检索表 search_fts）
- 分表 CSV：`01-products` / `02-atoms` / `03-workflows` / `04-channels` / `05-resources` / `08-template-modules` / `11-template-fit`
- 可读索引：`06-problem-to-component.md`（问题→组件）、`10-template-picker.md`（按模块反查模板）、`09-template-anatomy.md`（逐模板结构）
- 原始底稿：`raw/*.md`（每条带 URL）

## 表结构（列名即字段）
- `products`：no, slug, name, category, one_liner, icp_primary, icp_secondary, jtbd, core_scenarios, ai_mode, pricing_model, free_tier, paid_tiers, atoms_count, workflows_count, primary_channels, moat_hypothesis, evidence_urls, updated_at
- `atoms`：atom_id, product, atom_name, atom_type, what_it_does, composable_with, evidence_url
- `workflows`：workflow_id, product, workflow_name, input, atoms_used, steps, output, who_uses, evidence_url
- `channels`：channel_id, product, channel_type, mechanics, url_pattern, scale_note, replicable_score, evidence_url
- `resources`：resource_id, product, resource_name, resource_type, problem_solved, how_to_access, reuse_form, reuse_score, migration_cost, evidence_strength, evidence_url
- `template_modules`：template_id, product, template_name, template_one_liner, module_no, module_name, module_type, detail, composition, evidence_url
- `template_fit`：template_id, product, template_name, for_whom, scenario, how_to_use, value, what_it_is, composition, evidence_url, fit_basis
- `search_fts`：tbl, rid, title, body, url（FTS5）

## 查询套路
```sql
-- 1) 我要做 X 功能，别人怎么拼的
SELECT workflow_name, input, atoms_used, steps, output FROM workflows WHERE steps LIKE '%关键词%';
-- 2) 我要参考一个模板（先看适合谁/场景/怎么用）
SELECT template_name, for_whom, scenario, how_to_use FROM template_fit WHERE scenario LIKE '%关键词%';
-- 3) 这个模板由哪些模块组成
SELECT module_name, module_type, detail FROM template_modules WHERE template_id = ?;
-- 4) 某种原子能力谁有
SELECT product, atom_name, what_it_does, composable_with FROM atoms WHERE atom_type = '工具';
-- 5) 全文检索
SELECT tbl, title, url FROM search_fts WHERE search_fts MATCH 'MCP OR 工作流' LIMIT 20;
```

## 规则
1. 回答必须带 `evidence_url`；查不到出处就说「库里没有」。
2. `fit_basis` / `evidence_strength` 标了「推断」的，不能当事实陈述。
3. 先查 `template_fit`（人/场景/怎么用）→ 再查 `template_modules`（模块）→ 再查 `atoms/workflows`（实现）。
4. 需要原文时去 `raw/` 找对应产品的底稿。
"""
with open(os.path.join(BASE, "SKILL.md"), "w", encoding="utf-8") as f:
    f.write(skill)

llms = """# Teardown-100 KB（AI 产品拆解知识库）

> 100 个 AI 产品的结构化拆解库。当前已入库：013 Slack、014 Taskade。
> 主库：db/kb.sqlite（7 表 + FTS5）。索引：index.json。人读：06/09/10 md。
> 每条记录带 evidence_url；判断类字段带 fit_basis / evidence_strength。

## 结构
- products：定位（为谁/解决什么/场景/定价/AI 模式/渠道/护城河）
- atoms：原子能力（类型/做什么/能和什么组合）
- workflows：官方成品组合（输入→原子→步骤→输出）
- channels：流量渠道（机制/URL 模式/规模/可复制性）
- resources：资源目录（解决什么问题/怎么拿/复用价值）
- template_fit：模板适配（适合谁/场景/怎么用/价值）
- template_modules：模板模块（模块名/类型/说明/组合计数）

## 如何使用
- 机器：读 SKILL.md 的查询套路，用 SQL 查 db/kb.sqlite。
- 人：06-problem-to-component.md → 10-template-picker.md → 09-template-anatomy.md。
- 原文：raw/slack-raw.md、raw/taskade-raw.md。

## 引用
Teardown-100 KB, generated 2026-11-26. Facts from official pages; URLs kept in evidence_url.
"""
with open(os.path.join(BASE, "llms.txt"), "w", encoding="utf-8") as f:
    f.write(llms)

con.close()

# ---------- 分产品 JSON（便于迁移/单独喂给 Agent）----------
by_dir = os.path.join(BASE, "by-product")
os.makedirs(by_dir, exist_ok=True)
import csv as _csv

def rows_of(fname):
    p = os.path.join(BASE, fname)
    if not os.path.exists(p):
        return []
    with open(p, "r", encoding="utf-8-sig", newline="") as f:
        return list(_csv.DictReader(f))

products = rows_of("01-products.csv")
atoms = rows_of("02-atoms.csv")
workflows = rows_of("03-workflows.csv")
channels = rows_of("04-channels.csv")
resources = rows_of("05-resources.csv")
tmods = rows_of("08-template-modules.csv")
tfit = rows_of("11-template-fit.csv")
tcat = rows_of("13-template-catalog.csv")

written = 0
for p in products:
    slug = p.get("slug", "").strip()
    if not slug:
        continue
    payload = {
        "product": p,
        "atoms": [r for r in atoms if r.get("product") == slug],
        "workflows": [r for r in workflows if r.get("product") == slug],
        "channels": [r for r in channels if r.get("product") == slug],
        "resources": [r for r in resources if r.get("product") == slug],
        "template_modules": [r for r in tmods if r.get("product") == slug],
        "template_fit": [r for r in tfit if r.get("product") == slug],
        "template_catalog": [r for r in tcat if r.get("no") == p.get("no")],
    }
    fn = os.path.join(by_dir, f"{p.get('no','')}-{slug}.json")
    with open(fn, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    written += 1
print("by-product json:", written, "files")
print("SKILL.md / llms.txt written")
