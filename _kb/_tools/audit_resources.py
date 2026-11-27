# -*- coding: utf-8 -*-
"""资源层审计：每个产品的 resources / 原子 / 工作流 / 模板模块 / 适配 / 目录。"""
import sqlite3, os, csv

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(BASE, "db", "kb.sqlite")
con = sqlite3.connect(DB)

products = list(con.execute("select no, slug, name from products order by no"))
def cnt(sql, arg):
    return list(con.execute(sql, (arg,)))[0][0]

rows = []
for no, slug, name in products:
    rows.append({
        "no": no, "slug": slug, "name": name,
        "resources": cnt("select count(*) from resources where product=?", slug),
        "res_types": cnt("select count(distinct resource_type) from resources where product=?", slug),
        "atoms": cnt("select count(*) from atoms where product=?", slug),
        "workflows": cnt("select count(*) from workflows where product=?", slug),
        "modules": cnt("select count(*) from template_modules where product=?", slug),
        "fits": cnt("select count(*) from template_fit where product=?", slug),
        "catalog": cnt("select count(*) from template_catalog where no=?", no),
    })

with open(os.path.join(BASE, "17-resource-audit.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["no","slug","name","resources","res_types","atoms","workflows","modules","fits","catalog"])
    w.writeheader(); w.writerows(rows)

print(f"{'no':4} {'name':13} {'res':>4} {'typ':>4} {'atom':>5} {'flow':>5} {'mod':>4} {'fit':>4}")
for r in rows:
    print(f"{r['no']:4} {r['name'][:13]:13} {r['resources']:4} {r['res_types']:4} {r['atoms']:5} {r['workflows']:5} {r['modules']:4} {r['fits']:4}")
con.close()
