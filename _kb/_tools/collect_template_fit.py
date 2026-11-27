# -*- coding: utf-8 -*-
"""模板适配表：适合谁 / 什么场景 / 怎么用。
- what_it_is / how_to_use / value：优先抓官方页原文
- for_whom / scenario：关键词抓不准，改为人工判断（fit_basis 标「推断」）
生成 11-template-fit.csv
"""
import re, csv, os, urllib.request

BASE = r"D:\claudework\teardown-100\_kb"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130 Safari/537.36"

def fetch(url, accept="text/markdown"):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")

def strip_tags(html):
    t = re.sub(r"(?s)<script.*?</script>", " ", html)
    t = re.sub(r"(?s)<style.*?</style>", " ", t)
    t = re.sub(r"<[^>]+>", "\n", t)
    return re.sub(r"\n{2,}", "\n", t)

def clean(s):
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    return re.sub(r"\*\*", "", s).strip()

def section(md, title):
    m = re.search(r"#{2,3}\s*" + re.escape(title) + r"\s*(.*?)(?:\n#{1,3}\s|\Z)", md, re.S | re.I)
    return m.group(1).strip() if m else ""

def bullets(block, limit=5):
    out = []
    for line in block.split("\n"):
        s = line.strip()
        m = re.match(r"^[-*]\s+(.+)$", s) or re.match(r"^\d+[.)]\s+(.+)$", s)
        if m:
            out.append(clean(m.group(1)))
        if len(out) >= limit:
            break
    return " → ".join(out)

# 人工判断：模板 → (适合谁, 什么场景)
FIT = {
    "TP-TD-web-app-bug-tracker": ("SaaS / Web 产品的研发与 QA 团队", "缺陷从登记、分级、回归到发布说明的全流程"),
    "TP-TD-agency-client-onboarding": ("营销 / 创意 / 咨询代理公司", "新客户签约后的交接与 30 天启动"),
    "TP-TD-saas-marketing-plan": ("B2B SaaS 市场团队", "市场计划、预算分配与投放归因"),
    "TP-TD-ai-project-dashboard-template": ("项目经理 / 交付团队", "项目进度、里程碑与风险看板"),
    "TP-TD-expense-tracker": ("个人 / 小团队财务", "费用记录、分类与统计"),
    "TP-TD-saas-product-roadmap": ("SaaS 产品团队", "路线图、主题聚类与公开 changelog"),
    "TP-TD-ai-crm-dashboard-template": ("销售团队", "线索、商机、跟进与加权预测"),
    "TP-TD-app-data-model": ("运营 / 内部工具团队", "业务对象建模与决策视图"),
    "TP-SL-project-management-starter-kit": ("项目经理与跨职能团队", "项目从立项到发布"),
    "TP-SL-feedback-intake-triage": ("客户成功 / 产品团队", "反馈收集、分诊与跟踪"),
    "TP-SL-new-hire-onboarding": ("HR / 团队负责人", "新员工入职第一周"),
    "TP-SL-marketing-campaign-starter-kit": ("市场团队", "一次营销战役的作战室"),
    "TP-SL-external-partner-starter-kit": ("销售 / 合作团队", "与外部伙伴协作"),
    "TP-SL-sales-deal-tracking": ("销售团队", "商机跟踪与推进"),
}

TD_URLS = [
    "https://www.taskade.com/templates/bug-tracker/web-app-bug-tracker",
    "https://www.taskade.com/templates/client-onboarding/agency-client-onboarding",
    "https://www.taskade.com/templates/marketing-plan/saas-marketing-plan",
    "https://www.taskade.com/templates/project-management/ai-project-dashboard-template",
    "https://www.taskade.com/templates/finance-tracking/expense-tracker",
    "https://www.taskade.com/templates/product-roadmap/saas-product-roadmap",
    "https://www.taskade.com/templates/sales/ai-crm-dashboard-template",
    "https://www.taskade.com/templates/operations-intelligence/app-data-model",
]
SLACK_URLS = [
    ("project-management-starter-kit", "Project Management Template"),
    ("feedback-intake-triage", "Feedback Intake & Triage"),
    ("new-hire-onboarding", "New Hire Onboarding"),
    ("marketing-campaign-starter-kit", "Marketing Campaign Starter Kit"),
    ("external-partner-starter-kit", "External Partner Starter Kit"),
    ("sales-deal-tracking", "Sales Deal Tracking"),
]

rows = []

for url in TD_URLS:
    slug = url.rstrip("/").split("/")[-1]
    tid = "TP-TD-" + slug
    try:
        md = fetch(url)
    except Exception as e:
        rows.append([tid, "taskade", slug, "", "", "", "", "", "", url, "抓取失败:" + str(e)])
        continue
    mt = re.search(r"^# (.+)$", md, re.M)
    name = mt.group(1).strip() if mt else slug
    desc = ""
    after = md[mt.end():] if mt else md
    for line in after.split("\n"):
        s = line.strip()
        low = s.lower()
        if not s or low.startswith(("description:", "title:", "image:", "[", "!", "#", "|", ">", "-", "*")):
            continue
        if "·" in s or "STATUS" in s.upper() or "TASKADE.TEMPLATE" in s.upper():
            continue
        if len(s) > 40 and re.search(r"[a-z]", s):
            desc = s
            break
    how = bullets(section(md, "How to Use"), 5)
    why = bullets(section(md, "Why This Template Wins"), 3)
    comp = ""
    mc = re.search(r"(\d+)\s+projects?,\s*(\d+)\s+agents?\s+and\s+(\d+)\s+automations?", md)
    if mc:
        comp = f"{mc.group(1)} projects / {mc.group(2)} agent / {mc.group(3)} automations"
    who, scen = FIT.get(tid, ("", ""))
    rows.append([tid, "taskade", name, who, scen, how or "官方页未给步骤", why, desc, comp, url,
                 "适合谁/场景=推断（基于模板描述与模块）；怎么用/价值=原文"])

for slug, name in SLACK_URLS:
    tid = "TP-SL-" + slug
    url = f"https://slack.com/templates/{slug}"
    try:
        txt = strip_tags(fetch(url, accept="text/html"))
    except Exception as e:
        rows.append([tid, "slack", name, "", "", "", "", "", "", url, "抓取失败:" + str(e)])
        continue
    m = re.search(r"About this template\s*(.*?)(?:\n#{0,3}\s*(?:What is|Create|Related|Share|Slack templates)|\Z)", txt, re.S)
    about = ""
    if m:
        for line in m.group(1).split("\n"):
            s = line.strip()
            if len(s) > 60:
                about = s
                break
    who, scen = FIT.get(tid, ("", ""))
    rows.append([tid, "slack", name, who, scen,
                 "Get Template → 生成预配置的频道/画布/列表/工作流（Slack 页未给逐步说明）",
                 "", about, "", url,
                 "适合谁/场景=推断；怎么用=推断（页面只给 features）"])

out = os.path.join(BASE, "11-template-fit.csv")
with open(out, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["template_id", "product", "template_name", "for_whom", "scenario", "how_to_use", "value", "what_it_is", "composition", "evidence_url", "fit_basis"])
    w.writerows(rows)
print("written:", out, len(rows), "rows")

# 人读版：12-template-fit.md
md = ["# 模板适配表：适合谁 / 什么场景 / 怎么用", "",
      "> 用法：先在这张表里按「适合谁 + 场景」筛，选中后再去 `09-template-anatomy.md` 看模块，最后点模板链接。",
      "> `适合谁 / 场景` 是人工判断（基于模板描述与模块，标「推断」）；`怎么用 / 价值` 是官方原文。", ""]
md.append("| 模板 | 产品 | 适合谁（推断） | 什么场景（推断） | 怎么用（官方步骤，节选） | 组合 | 链接 |")
md.append("|---|---|---|---|---|---|---|")
for r in rows:
    tid, product, name, who, scen, how, value, what, comp, url, basis = r
    how_s = (how or "").replace("|", "／")
    if len(how_s) > 90:
        how_s = how_s[:90] + "…"
    md.append(f"| {name} | {product} | {who} | {scen} | {how_s} | {comp} | {url} |")
md.append("")
md.append("## 每个模板的一句话")
md.append("")
for r in rows:
    tid, product, name, who, scen, how, value, what, comp, url, basis = r
    md.append(f"### {product} · {name}")
    md.append("")
    if what:
        md.append(f"- **是什么**：{what}")
    md.append(f"- **适合谁**：{who}（推断）")
    md.append(f"- **什么场景**：{scen}（推断）")
    if comp:
        md.append(f"- **组合**：{comp}")
    if how:
        md.append(f"- **怎么用**：{how}")
    if value:
        md.append(f"- **为什么用它**：{value}")
    md.append(f"- **模板页**：{url}")
    md.append("")

md_path = os.path.join(BASE, "12-template-fit.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md))
print("written:", md_path, len(md), "lines")
