# -*- coding: utf-8 -*-
"""模板标签结构（taxonomy）：平台 → 板块/分类/主题/风格/标签 + 数量 + 入口。
输出 15-template-taxonomy.csv 与 16-template-taxonomy.md。
"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GAMMA = "https://app.gamma.app/#gamma-templates"
NOTION = "https://app.notion.com/marketplace"
FIGMA = "https://www.figma.com/files/team/1666643033011782866/resources/community"

rows = []
def add(platform, facet, value, count="", parent="", note="", url="", ev=""):
    rows.append([platform, facet, value, str(count), parent, note, url, ev])

# ---- Gamma ----
for v in ["演示文稿", "文档", "社交轮播卡片", "网页"]:
    add("gamma", "format", v, "", "格式", "顶部格式筛选", GAMMA, GAMMA)
for v, c in [("课程",223),("提案",183),("营销材料",173),("报告",166),("融资演讲稿",154),("培训",127),
             ("商业规划",117),("活动",116),("研究",96),("社交媒体",85),("学校项目",60),("宣传册",57),
             ("作品集",53),("会议",49),("电子书",21),("项目管理",19),("信息图",15),("好玩有趣",13),("简历",5)]:
    add("gamma", "category", v, c, "类别", "左侧类别筛选（已展开全部）", GAMMA, GAMMA)
for v, c in [("商业",361),("教育",293),("艺术",216),("科学",149),("数据与分析",132),("自然",115),
             ("财务",97),("技术",93),("食物",86),("历史与社会研究",84),("工程",63),("法律与政府",60),
             ("健康",54),("房地产与建筑",50),("旅行",49),("心理学与自我提升",37),("体育运动",19),("宗教与信仰",13)]:
    add("gamma", "theme", v, c, "主题", "左侧主题筛选（已展开全部）", GAMMA, GAMMA)
for v, c in [("视觉",454),("醒目",363),("插画风格",315),("温馨友好",228),("现代",221),("活泼",205),
             ("专业",197),("优雅",195),("深色",177),("学术与技术",133),("复古",131),("简洁",101),
             ("文字型",84),("自然有机",58),("可爱",26),("未来感",13)]:
    add("gamma", "style", v, c, "风格", "左侧风格筛选（已展开全部）", GAMMA, GAMMA)
add("gamma", "color", "色块筛选", "", "颜色", "颜色为色块，文字值未取；示例：绿色 96", GAMMA, GAMMA)

# ---- Notion ----
for v in ["探索", "模板", "代理", "顾问", "技能", "连接"]:
    add("notion", "marketplace_tab", v, "", "市集", "应用内市集一级入口", NOTION, NOTION)
for v in ["工作", "生活", "学校"]:
    add("notion", "template_scope", v, "", "模板", "模板页顶部范围", NOTION, NOTION)
for v in ["市场营销","风险投资","金融","网站建设","产品","用户调研","企业版","教学","创始人","工程",
          "咨询","创意机构","非营利组织","房地产","数据科学","销售","启动","业务","招聘","公共关系与传播",
          "设计","自由职业者","IT","人力资源","经理"]:
    add("notion", "use_case", v, "", "Use Case", "业务场景筛选（25 个）", NOTION, NOTION)
for v in ["写作技能", "总结与整理技能", "分析技能"]:
    add("notion", "skill_category", v, "", "技能", "技能页分类", NOTION, NOTION)
for v in ["会议纪要","翻译成英文","校对","零基础解释","将笔记整理成文档","创建技能"]:
    add("notion", "skill_example", v, "", "技能/示例", "技能页示例（前 6 个）", NOTION, NOTION)

# ---- Figma ----
for v, c, note in [("AI workflows", "20+", "Figma Weave 工作流"),
                   ("Website templates", "5", "Figma Sites 网站模板"),
                   ("UI kits", "5", "iOS / Material 3 / Simple Design System 等"),
                   ("Skills", "6", "可复用指令"),
                   ("Presentations", "", "Figma Slides"),
                   ("Assets", "", "图标/插画/照片/图案"),
                   ("Riffs", "", "创作过程快照"),
                   ("Figma Make", "", "Prompt to Code"),
                   ("Extensions", "", "插件/组件"),
                   ("Whiteboarding", "", "白板"),
                   ("Websites", "", "网站"),
                   ("Design resources", "", "设计资源总入口")]:
    add("figma", "section", v, c, "资源板块", note, FIGMA, FIGMA)
for v in ["Product & brand", "Marketing", "Character & narrative", "Ideation"]:
    add("figma", "ai_workflow_subcategory", v, "", "AI workflows", "AI workflows 子类", FIGMA, FIGMA)

header = ["platform", "facet", "value", "count", "parent", "note", "url", "evidence_url"]
csv_path = os.path.join(BASE, "15-template-taxonomy.csv")
with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)
print("written:", csv_path, len(rows), "rows")

# 人读版
def block(platform, title, facets):
    lines = [f"## {title}", ""]
    for facet, label in facets:
        items = [r for r in rows if r[0] == platform and r[1] == facet]
        if not items:
            continue
        lines.append(f"### {label}")
        lines.append("")
        lines.append("| 值 | 数量 | 说明 |")
        lines.append("|---|---|---|")
        for r in items:
            lines.append(f"| {r[2]} | {r[3] or '—'} | {r[5]} |")
        lines.append("")
    return lines

md = ["# 模板标签结构（Taxonomy）", "",
      "> 目的：以后要知道「这个平台有什么可参考、agent 怎么去哪」，先查这张表，而不是凭记忆。",
      "> 数据来自 2026-11-26 登录后的实际筛选面板/导航；数量是平台显示的筛选计数。", "",
      "## 入口与筛选方式", "",
      "| 平台 | 入口 | 怎么筛 |", "|---|---|---|",
      f"| Gamma | {GAMMA} | 左侧筛选：格式 / 类别 / 主题 / 颜色 / 风格（无 URL 参数，靠 UI） |",
      f"| Notion | {NOTION} | 顶部：模板 / 代理 / 顾问 / 技能 / 连接；模板内按 工作/生活/学校 + Use Case |",
      f"| Figma | {FIGMA} | 团队资源库板块：AI workflows / Website templates / UI kits / Skills…；文件 URL 形如 /community/file/<id>、/community/weave_workflow/<id> |",
      ""]
md += block("gamma", "Gamma（app.gamma.app）", [("format","格式"),("category","类别"),("theme","主题"),("style","风格"),("color","颜色")])
md += block("notion", "Notion（app.notion.com/marketplace）", [("marketplace_tab","市集入口"),("template_scope","模板范围"),("use_case","Use Case"),("skill_category","技能分类"),("skill_example","技能示例")])
md += block("figma", "Figma（团队资源库）", [("section","资源板块"),("ai_workflow_subcategory","AI workflows 子类")])
md += ["## Agent 怎么用这张表", "",
       "- 问「Gamma 有哪些营销类模板」→ 查 platform=gamma & category=营销材料（173）→ 再按 theme/style 收窄。",
       "- 问「Notion 有没有咨询行业模板」→ 查 platform=notion & use_case=咨询。",
       "- 问「Figma 有没有 AI 广告工作流」→ 查 platform=figma & facet=ai_workflow_subcategory & value=Marketing，再去 08/11 找已解剖样本。",
       "- 表里只有「有什么」，具体模板的结构去 `08-template-modules` / `11-template-fit`；两者用产品名关联。"]
md_path = os.path.join(BASE, "16-template-taxonomy.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md))
print("written:", md_path, len(md), "lines")
