# -*- coding: utf-8 -*-
import sqlite3, os
DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "db", "kb.sqlite")
con = sqlite3.connect(DB)
cur = con.cursor()
print("tables:", [r[0] for r in cur.execute("select name from sqlite_master where type='table' order by name")])
print("\n[模板：适合谁 / 场景 / 怎么用]")
for r in cur.execute("select template_name, for_whom, scenario, substr(how_to_use,1,60) from template_fit limit 5"):
    print(" -", r)
print("\n[FTS: MCP]")
for r in cur.execute("select tbl, title from search_fts where search_fts match 'MCP' limit 5"):
    print(" -", r)
print("\n[按模块类型查 Agent]")
for r in cur.execute("select template_name, module_name from template_modules where module_type='Agent' limit 6"):
    print(" -", r)
print("\n[问题→工作流：审批]")
for r in cur.execute("select workflow_name, steps from workflows where steps like '%审批%' limit 3"):
    print(" -", r)
con.close()
