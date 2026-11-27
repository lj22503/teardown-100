# -*- coding: utf-8 -*-
"""补录登录墙后抓到的模板：Figma 3（有模块清单）+ Gamma 3（仅适配）。
写入 data/history-template-*.csv（幂等：先删同 id 再加）。
"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")

MOD_HEADER = ["template_id","product","template_name","template_one_liner","module_no","module_name","module_type","detail","composition","evidence_url"]
FIT_HEADER = ["template_id","product","template_name","for_whom","scenario","how_to_use","value","what_it_is","composition","evidence_url","fit_basis"]

FIGMA = "https://www.figma.com/community/file/"
mods = [
    # Free Figma UI kit and design system
    ["TP-figma-free-ui-kit","figma","Free Figma UI kit and design system","一套可直接用的 UI kit + 设计系统底子",1,"Design tokens","工具","颜色/字体/间距/阴影四类 token","3 个模块",FIGMA+"1512527544070386427/free-figma-ui-kit-and-design-system"],
    ["TP-figma-free-ui-kit","figma","Free Figma UI kit and design system","一套可直接用的 UI kit + 设计系统底子",2,"可访问组件","工具","带 default/hover/focus/error/disabled 状态的组件","3 个模块",FIGMA+"1512527544070386427/free-figma-ui-kit-and-design-system"],
    ["TP-figma-free-ui-kit","figma","Free Figma UI kit and design system","一套可直接用的 UI kit + 设计系统底子",3,"布局模式","界面","支撑迭代与扩展的 layout patterns","3 个模块",FIGMA+"1512527544070386427/free-figma-ui-kit-and-design-system"],
    # Media Dashboard
    ["TP-figma-media-dashboard","figma","Media Dashboard","内容/社媒团队的可编辑数据看板",1,"可编辑 Figma 文件","工具","整套文件可改，非只读稿","4 个模块",FIGMA+"1537877734913818740/media-dashboard"],
    ["TP-figma-media-dashboard","figma","Media Dashboard","内容/社媒团队的可编辑数据看板",2,"响应式布局","界面","Clean, responsive layout","4 个模块",FIGMA+"1537877734913818740/media-dashboard"],
    ["TP-figma-media-dashboard","figma","Media Dashboard","内容/社媒团队的可编辑数据看板",3,"核心指标与图表","界面","Key media metrics, charts","4 个模块",FIGMA+"1537877734913818740/media-dashboard"],
    ["TP-figma-media-dashboard","figma","Media Dashboard","内容/社媒团队的可编辑数据看板",4,"内容表格","界面","Content tables","4 个模块",FIGMA+"1537877734913818740/media-dashboard"],
    # Ventixe
    ["TP-figma-ventixe","figma","Ventixe 活动管理后台","活动组织者/票务平台/场馆的活动管理后台",1,"Dashboard","界面","总览页","7 个模块",FIGMA+"1482921791678828657/ventixe-event-management-admin-dashboard-ui-design"],
    ["TP-figma-ventixe","figma","Ventixe 活动管理后台","活动组织者/票务平台/场馆的活动管理后台",2,"Bookings","界面","预订","7 个模块",FIGMA+"1482921791678828657/ventixe-event-management-admin-dashboard-ui-design"],
    ["TP-figma-ventixe","figma","Ventixe 活动管理后台","活动组织者/票务平台/场馆的活动管理后台",3,"E-Voucher","界面","电子凭证","7 个模块",FIGMA+"1482921791678828657/ventixe-event-management-admin-dashboard-ui-design"],
    ["TP-figma-ventixe","figma","Ventixe 活动管理后台","活动组织者/票务平台/场馆的活动管理后台",4,"Invoices","界面","发票","7 个模块",FIGMA+"1482921791678828657/ventixe-event-management-admin-dashboard-ui-design"],
    ["TP-figma-ventixe","figma","Ventixe 活动管理后台","活动组织者/票务平台/场馆的活动管理后台",5,"Inbox","界面","消息","7 个模块",FIGMA+"1482921791678828657/ventixe-event-management-admin-dashboard-ui-design"],
    ["TP-figma-ventixe","figma","Ventixe 活动管理后台","活动组织者/票务平台/场馆的活动管理后台",6,"Calendar","界面","日历","7 个模块",FIGMA+"1482921791678828657/ventixe-event-management-admin-dashboard-ui-design"],
    ["TP-figma-ventixe","figma","Ventixe 活动管理后台","活动组织者/票务平台/场馆的活动管理后台",7,"Events（Grid）","界面","活动网格","7 个模块",FIGMA+"1482921791678828657/ventixe-event-management-admin-dashboard-ui-design"],
]

fits = [
    ["TP-figma-free-ui-kit","figma","Free Figma UI kit and design system","产品设计师、设计团队","从 0 搭 UI 或补一套设计系统底子","复制文件 → 用 tokens/组件 → 按 states 扩展 → 接进自己的设计系统","省掉搭基础层；token + 可访问组件 + 布局模式","一套可直接用的 UI kit + 设计系统底子","3 个模块",FIGMA+"1512527544070386427/free-figma-ui-kit-and-design-system","适合谁/场景=推断；模块=页面描述与搜索摘要（B）；怎么用=推断"],
    ["TP-figma-media-dashboard","figma","Media Dashboard","内容创作者、社媒经理、媒体团队","可视化内容/投放表现并管理 campaign","Duplicate → 接自己的数据 → 改图表与表格","可编辑、响应式、含核心指标与内容表格","内容/社媒团队的数据看板","4 个模块",FIGMA+"1537877734913818740/media-dashboard","适合谁=页面描述原文；模块=页面描述（B）；怎么用=推断"],
    ["TP-figma-ventixe","figma","Ventixe 活动管理后台","活动组织者、票务平台、场馆管理者","活动运营后台（预订/凭证/发票/消息/日历/活动）","Duplicate → 换品牌色 → 接业务数据","7 个页面覆盖活动运营主流程","活动管理后台 UI 模板","7 个模块",FIGMA+"1482921791678828657/ventixe-event-management-admin-dashboard-ui-design","适合谁=页面描述原文；模块=搜索摘要列出的页面（B）；怎么用=推断"],
    ["TP-gamma-sorbet-sprint-finish","gamma","Sorbet（营销材料）","市场与活动团队","营销活动启动 deck","选模板 → 使用此模板生成 → 输入内容/大纲 → Gamma 生成可编辑幻灯片","风格统一（奶油+亮橙）、自动排版、可重组","营销材料示例 deck","",  "https://gamma.app/zh-cn/templates/sorbet-sprint-finish","适合谁/场景=推断；怎么用=页面原文（使用此模板生成）；价值=页面描述"],
    ["TP-gamma-deep-cut-sprint-finish","gamma","Deep Cut（商业规划）","创始人/战略与商业规划团队","商业规划/路演 deck","选模板 → 使用此模板生成 → 输入内容 → 生成","深洋红+深绿的强对比风格，海报级几何版式","商业规划示例 deck","",  "https://gamma.app/zh-cn/templates/deep-cut-sprint-finish","适合谁/场景=推断；怎么用=页面原文；价值=页面描述"],
    ["TP-gamma-daktilo-dispatch-sprint-finish","gamma","Daktilo Dispatch（报告）","分析师、咨询顾问、研究团队","调查报告/研究汇报 deck","选模板 → 使用此模板生成 → 输入报告内容 → 生成","案件档案式视觉（马尼拉文件夹/打字机字体/证据照片）","报告示例 deck","",  "https://gamma.app/zh-cn/templates/daktilo-dispatch-sprint-finish","适合谁/场景=推断；怎么用=页面原文；价值=页面描述"],
]

def append(path, header, rows, ids):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        old = list(csv.reader(f))
    kept = [r for r in old if r and r[0] not in ids]
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(kept[1:] if kept and kept[0] == header else kept)
        w.writerows(rows)
    print(path, "->", len(kept) - 1 + len(rows), "rows")

append(os.path.join(DATA, "history-template-modules.csv"), MOD_HEADER, mods, {r[0] for r in mods})
append(os.path.join(DATA, "history-template-fit.csv"), FIT_HEADER, fits, {r[0] for r in fits})
