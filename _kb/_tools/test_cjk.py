# -*- coding: utf-8 -*-
import sqlite3, os
DB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "db", "kb.sqlite")
con = sqlite3.connect(DB); cur = con.cursor()
for q in ["工作流", "MCP", "模板"]:
    try:
        n = list(cur.execute("select count(*) from search_fts where search_fts match ?", (q,)))[0][0]
    except Exception as e:
        n = "ERR:" + str(e)
    m = list(cur.execute("select count(*) from workflows where steps like ?", (f"%{q}%",)))[0][0]
    print("FTS", q, n, "| LIKE(workflows)", m)
con.close()
