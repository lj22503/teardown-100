# -*- coding: utf-8 -*-
"""知识库质量闸：任何一次改动后必须通过，否则回滚。
退出码：0 通过；1 有错误（阻止 promote）。
用法：python _kb/automation/qa_gate.py
"""
import csv, os, sqlite3, sys, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERRORS = []
WARNS = []

def read(name):
    p = os.path.join(BASE, name)
    if not os.path.exists(p):
        ERRORS.append(f"缺文件：{name}")
        return [], []
    with open(p, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        return [], []
    header = rows[0]
    body = [r for r in rows[1:] if r and len(r) == len(header)]
    return header, body

def check_unique(name, rows, col_idx):
    seen = {}
    for i, r in enumerate(rows, 2):
        if len(r) <= col_idx:
            ERRORS.append(f"{name} 第{i}行列数不足")
            continue
        v = r[col_idx].strip()
        if not v:
            ERRORS.append(f"{name} 第{i}行 {col_idx} 列为空")
        elif v in seen:
            ERRORS.append(f"{name} 主键重复：{v}（第{seen[v]}行与第{i}行）")
        else:
            seen[v] = i

def check_evidence(name, header, rows, must_cols):
    if "evidence_url" not in header:
        ERRORS.append(f"{name} 缺 evidence_url 列")
        return
    idx = {h: i for i, h in enumerate(header)}
    for i, r in enumerate(rows, 2):
        for c in must_cols:
            if c in idx and idx[c] < len(r) and not r[idx[c]].strip():
                ERRORS.append(f"{name} 第{i}行 {c} 为空")
        if "evidence_url" in idx and idx["evidence_url"] < len(r):
            u = r[idx["evidence_url"]].strip()
            if not (u.startswith("http://") or u.startswith("https://")):
                ERRORS.append(f"{name} 第{i}行 evidence_url 非法：{u[:50]}")

# 1) products
h, rows = read("01-products.csv")
if h:
    check_unique("01-products.csv", rows, 0)
    idx = {x: i for i, x in enumerate(h)}
    if len(rows) < 14:
        WARNS.append(f"products 只有 {len(rows)} 行（预期 ≥14）")
    for i, r in enumerate(rows, 2):
        for c in ["no", "slug", "name", "one_liner", "icp_primary", "jtbd", "ai_mode"]:
            if c in idx and idx[c] < len(r) and not r[idx[c]].strip():
                ERRORS.append(f"01-products.csv 第{i}行 {c} 为空")

# 2) atoms / workflows / channels / resources
h, rows = read("02-atoms.csv")
if h:
    check_unique("02-atoms.csv", rows, 0)
    check_evidence("02-atoms.csv", h, rows, ["atom_name", "what_it_does"])
h, rows = read("03-workflows.csv")
if h:
    check_unique("03-workflows.csv", rows, 0)
    check_evidence("03-workflows.csv", h, rows, ["workflow_name", "steps"])
h, rows = read("04-channels.csv")
if h:
    check_unique("04-channels.csv", rows, 0)
    check_evidence("04-channels.csv", h, rows, ["channel_type", "mechanics"])
    idx = {x: i for i, x in enumerate(h)}
    for i, r in enumerate(rows, 2):
        if "replicable_score" in idx and idx["replicable_score"] < len(r):
            if r[idx["replicable_score"]].strip() not in {"1", "2", "3", "4", "5"}:
                WARNS.append(f"04-channels.csv 第{i}行 replicable_score 非 1-5")
h, rows = read("05-resources.csv")
if h:
    check_unique("05-resources.csv", rows, 0)
    check_evidence("05-resources.csv", h, rows, ["resource_name", "problem_solved"])
    # 覆盖度：除 008（已放弃）外，每个产品至少 2 条资源
    ph, prows = read("01-products.csv")
    pidx = {x: i for i, x in enumerate(ph)}
    res_by = {}
    for r in rows:
        if len(r) > 1:
            res_by[r[1]] = res_by.get(r[1], 0) + 1
    for pr in prows:
        if "no" not in pidx or "slug" not in pidx:
            break
        no = pr[pidx["no"]].strip()
        slug = pr[pidx["slug"]].strip()
        if no == "008":
            continue
        n = res_by.get(slug, 0)
        if n == 0:
            ERRORS.append(f"产品 {no} {slug} 没有资源条目")
        elif n < 3:
            WARNS.append(f"产品 {no} {slug} 资源只有 {n} 条（建议 ≥3）")

# 2.5) 原子/工作流覆盖度（008 除外）
if 'prows' in dir() and prows:
    _, arows = read("02-atoms.csv")
    _, wrows = read("03-workflows.csv")
    ac, wc = {}, {}
    for r in arows:
        if len(r) > 1: ac[r[1]] = ac.get(r[1], 0) + 1
    for r in wrows:
        if len(r) > 1: wc[r[1]] = wc.get(r[1], 0) + 1
    for pr in prows:
        if "no" not in pidx or "slug" not in pidx:
            break
        no = pr[pidx["no"]].strip(); slug = pr[pidx["slug"]].strip()
        if no == "008":
            continue
        na, nw = ac.get(slug, 0), wc.get(slug, 0)
        if na == 0:
            ERRORS.append(f"产品 {no} {slug} 没有原子能力")
        elif na < 8:
            WARNS.append(f"产品 {no} {slug} 原子只有 {na} 条（建议 ≥8）")
        if nw == 0:
            ERRORS.append(f"产品 {no} {slug} 没有工作流")
        elif nw < 3:
            WARNS.append(f"产品 {no} {slug} 工作流只有 {nw} 条（建议 ≥3）")

# 3) template_modules / template_fit
h, rows = read("08-template-modules.csv")
if h:
    # 主键是 template_id + module_no 组合
    seen = {}
    for i, r in enumerate(rows, 2):
        if len(r) < 5:
            ERRORS.append(f"08-template-modules.csv 第{i}行列数不足")
            continue
        key = (r[0].strip(), r[4].strip())
        if not key[0] or not key[1]:
            ERRORS.append(f"08-template-modules.csv 第{i}行主键为空")
        elif key in seen:
            ERRORS.append(f"08-template-modules.csv 主键重复：{key}（第{seen[key]}行与第{i}行）")
        else:
            seen[key] = i
    check_evidence("08-template-modules.csv", h, rows, ["module_name"])
h2, rows2 = read("11-template-fit.csv")
if h2:
    check_unique("11-template-fit.csv", rows2, 0)
    check_evidence("11-template-fit.csv", h2, rows2, ["for_whom", "scenario", "how_to_use"])
    # 交叉引用：每个 template_fit 的 template_id 至少要出现在 08 里
    if h:
        ids08 = {r[0] for r in rows if r}
        missing = [r[0] for r in rows2 if r and r[0] not in ids08]
        if missing:
            WARNS.append("template_fit 有、template_modules 没有的模板：" + ", ".join(missing[:5]))

# 3.5) 模板目录
h, rows = read("13-template-catalog.csv")
if h:
    check_unique("13-template-catalog.csv", rows, 0)
    idx = {x: i for i, x in enumerate(h)}
    for i, r in enumerate(rows, 2):
        for c in ["no", "product", "has_gallery", "gallery_type"]:
            if c in idx and idx[c] < len(r) and not r[idx[c]].strip():
                ERRORS.append(f"13-template-catalog.csv 第{i}行 {c} 为空")
        if "has_gallery" in idx and idx["has_gallery"] < len(r):
            v = r[idx["has_gallery"]].strip()
            if v not in {"yes", "no", "partial", "放弃"}:
                ERRORS.append(f"13-template-catalog.csv 第{i}行 has_gallery 非法：{v}")
            if v in {"yes", "partial"} and "gallery_url" in idx and idx["gallery_url"] < len(r) and not r[idx["gallery_url"]].strip():
                ERRORS.append(f"13-template-catalog.csv 第{i}行 有模板库但 gallery_url 为空")
    if len(rows) < 12:
        WARNS.append(f"template_catalog 只有 {len(rows)} 行（预期 ≥12）")

# 3.6) 标签结构
h, rows = read("15-template-taxonomy.csv")
if h:
    idx = {x: i for i, x in enumerate(h)}
    seen = set()
    for i, r in enumerate(rows, 2):
        if len(r) < 4:
            ERRORS.append(f"15-template-taxonomy.csv 第{i}行列数不足")
            continue
        plat, facet, val = r[0].strip(), r[1].strip(), r[2].strip()
        if plat not in {"gamma", "notion", "figma"}:
            ERRORS.append(f"15-template-taxonomy.csv 第{i}行 platform 非法：{plat}")
        if not facet or not val:
            ERRORS.append(f"15-template-taxonomy.csv 第{i}行 facet/value 为空")
        key = (plat, facet, val)
        if key in seen:
            ERRORS.append(f"15-template-taxonomy.csv 重复：{key}")
        seen.add(key)
    if len(rows) < 80:
        WARNS.append(f"template_taxonomy 只有 {len(rows)} 行（预期 ≥80）")

# 4) sqlite 完整性 + 行数一致
db = os.path.join(BASE, "db", "kb.sqlite")
if not os.path.exists(db):
    ERRORS.append("缺 db/kb.sqlite")
else:
    con = sqlite3.connect(db)
    ok = list(con.execute("PRAGMA integrity_check"))[0][0]
    if ok != "ok":
        ERRORS.append("sqlite integrity_check: " + str(ok))
    pairs = [("products", "01-products.csv"), ("atoms", "02-atoms.csv"),
             ("workflows", "03-workflows.csv"), ("channels", "04-channels.csv"),
             ("resources", "05-resources.csv"), ("template_modules", "08-template-modules.csv"),
             ("template_fit", "11-template-fit.csv"), ("template_catalog", "13-template-catalog.csv"),
             ("template_taxonomy", "15-template-taxonomy.csv")]
    for table, f in pairs:
        try:
            n_db = list(con.execute(f'select count(*) from "{table}"'))[0][0]
        except Exception as e:
            ERRORS.append(f"表 {table} 查询失败: {e}")
            continue
        _, rws = read(f)
        if n_db != len(rws):
            ERRORS.append(f"行数不一致：{table}={n_db} vs {f}={len(rws)}")
    con.close()

# 5) index.json 可解析
try:
    with open(os.path.join(BASE, "index.json"), "r", encoding="utf-8") as f:
        json.load(f)
except Exception as e:
    ERRORS.append("index.json 解析失败: " + str(e))

print(f"QA: {len(ERRORS)} errors, {len(WARNS)} warnings")
for e in ERRORS[:30]:
    print("  ERROR:", e)
for w in WARNS[:10]:
    print("  WARN:", w)
sys.exit(1 if ERRORS else 0)
