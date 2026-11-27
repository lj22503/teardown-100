# -*- coding: utf-8 -*-
"""调试：用脚本内 UTF-8 关键词跑 ask.run，绕开 Windows 控制台参数编码问题。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ask

for kw in ["客户交接", "缺陷", "MCP"]:
    ask.run(kw)
