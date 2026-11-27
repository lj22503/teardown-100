# -*- coding: utf-8 -*-
"""一键重建知识库：模板适配/模块 → 选型索引 → SQLite → xlsx。
不跑 fill_slack_taskade（避免覆盖已回填的产品表）。
用法：python _tools/rebuild_all.py
"""
import subprocess, sys, os

TOOLS = os.path.dirname(os.path.abspath(__file__))
steps = [
    "collect_template_fit.py",
    "collect_template_modules.py",
    "merge_templates.py",
    "build_catalog.py",
    "build_taxonomy.py",
    "build_anatomy_md.py",
    "build_fit_md.py",
    "build_picker.py",
    "merge_atoms.py",
    "build_db.py",
    "build_xlsx.py",
]
for s in steps:
    p = os.path.join(TOOLS, s)
    print("\n>>>", s)
    r = subprocess.run([sys.executable, p], cwd=os.path.dirname(TOOLS))
    if r.returncode != 0:
        print("FAILED:", s, "exit", r.returncode)
        sys.exit(r.returncode)
print("\nall done")
