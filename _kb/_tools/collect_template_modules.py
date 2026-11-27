# -*- coding: utf-8 -*-
"""抓取 Slack / Taskade 代表模板的「模块解剖」，生成 08-template-modules.csv + 09-template-anatomy.md。
- Taskade：用 Accept: text/markdown 抓分类页→取第一个详情页→抽 What's Included 与组合计数
- Slack：抓 HTML→抽 "Template features:" 列表
"""
import re, csv, os, json, urllib.request, urllib.error, time

BASE = r"D:\claudework\teardown-100\_kb"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130 Safari/537.36"

def fetch(url, accept="text/html"):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
        ct = r.headers.get("Content-Type", "")
        return data.decode("utf-8", errors="replace"), ct

def strip_tags(html):
    t = re.sub(r"(?s)<script.*?</script>", " ", html)
    t = re.sub(r"(?s)<style.*?</style>", " ", t)
    t = re.sub(r"<[^>]+>", "\n", t)
    t = re.sub(r"\n{2,}", "\n", t)
    return t

# ---------- Slack ----------
SLACK_TEMPLATES = [
    ("project-management-starter-kit", "Project Management Template"),
    ("feedback-intake-triage", "Feedback Intake & Triage"),
    ("new-hire-onboarding", "New Hire Onboarding"),
    ("marketing-campaign-starter-kit", "Marketing Campaign Starter Kit"),
    ("bug-tracker", "Bug Tracker"),
    ("external-partner-starter-kit", "External Partner Starter Kit"),
    ("sales-deal-tracking", "Sales Deal Tracking"),
    ("incident-summary", "Incident Summary"),
]

def slack_features(slug, name):
    url = f"https://slack.com/templates/{slug}"
    try:
        html, _ = fetch(url)
    except Exception as e:
        return name, url, [], "抓取失败: " + str(e)
    txt = strip_tags(html)
    m = re.search(r"Template features:\s*(.*?)(?:\s*Tags:|\Z)", txt, re.S)
    if not m:
        return name, url, [], "未找到 Template features"
    body = m.group(1)
    feats = [x.strip() for x in body.split("\n") if x.strip()]
    feats = [f for f in feats if len(f) < 60]
    return name, url, feats, ""

# Slack 模块类型推断
def slack_type(f):
    fl = f.lower()
    if any(k in fl for k in ["form", "intake", "request"]):
        return "表单"
    if any(k in fl for k in ["overview", "brief", "agenda", "document", "guide", "faq", "canvas"]):
        return "文档/Canvas"
    if any(k in fl for k in ["tracker", "list", "okr", "deal", "task"]):
        return "列表/List"
    if any(k in fl for k in ["notification", "check-in", "welcome", "reminder", "workflow", "status", "approv", "alert"]):
        return "工作流"
    return "模块"

# ---------- Taskade ----------
TD_CATEGORIES = [
    "bug-tracker", "client-onboarding", "marketing-plan", "project-management",
    "finance-tracking", "product-roadmap", "sales", "operations-intelligence",
]

def td_first_detail(cat):
    url = f"https://www.taskade.com/templates/{cat}"
    md, _ = fetch(url, accept="text/markdown")
    # 找第一个详情链接 /templates/<cat>/<slug>
    m = re.search(r"https://www\.taskade\.com/templates/" + re.escape(cat) + r"/([a-z0-9\-]+)", md)
    return (f"https://www.taskade.com/templates/{cat}/{m.group(1)}", m.group(1)) if m else (None, None)

def td_detail(url):
    md, _ = fetch(url, accept="text/markdown")
    title = ""
    mt = re.search(r"^# (.+)$", md, re.M)
    if mt:
        title = mt.group(1).strip()
    # 一句话描述：标题后第一段 >40 字的正文
    desc = ""
    after = md[mt.end():] if mt else md
    for line in after.split("\n"):
        s = line.strip()
        if not s:
            continue
        low = s.lower()
        if low.startswith(("description:", "title:", "image:", "last-updated:", "[", "!", "#", "|", ">", "-", "*")):
            continue
        # 跳过装饰性横幅行（全大写 / 含 · / 含 STATUS / TASKADE.TEMPLATE）
        if "·" in s or "STATUS" in s.upper() or "TASKADE.TEMPLATE" in s.upper():
            continue
        # 必须像一句正常句子：含小写字母、长度够
        if len(s) > 40 and re.search(r"[a-z]", s):
            desc = s
            break
    # What's Included（大小写/标点容错）
    inc = []
    mi = re.search(r"#{2,3}\s*What'?s\s+Included\s*(.*?)(?:\n#{1,3}\s|\Z)", md, re.S | re.I)
    if mi:
        for line in mi.group(1).split("\n"):
            line = line.strip()
            if not line:
                continue
            mm = re.match(r"^[-*]\s+\*\*(.+?)\*\*\s*[:：]?\s*(.*)$", line)
            if mm:
                inc.append((mm.group(1).strip().rstrip(":："), mm.group(2).strip()))
                continue
            mm2 = re.match(r"^[-*]\s+(.{2,40}?)\s*[:：]\s*(.+)$", line)
            if mm2:
                inc.append((mm2.group(1).strip(), mm2.group(2).strip()))
                continue
            mm3 = re.match(r"^[-*]\s+(.+)$", line)
            if mm3 and len(mm3.group(1)) < 80:
                inc.append((mm3.group(1).strip()[:40], ""))
    # 组合计数
    comp = ""
    mc = re.search(r"(\d+)\s+projects?,\s*(\d+)\s+agents?\s+and\s+(\d+)\s+automations?", md)
    if mc:
        comp = f"{mc.group(1)} projects / {mc.group(2)} agent / {mc.group(3)} automations"
    return title, desc, inc, comp

def td_type(name):
    n = name.lower()
    if "agent" in n:
        return "Agent"
    if any(k in n for k in ["form", "intake", "submission"]):
        return "表单"
    if any(k in n for k in ["board", "view", "dashboard", "pipeline", "matrix", "calendar", "timeline"]):
        return "视图/看板"
    if any(k in n for k in ["sync", "github", "gitlab", "integration", "slack", "linear"]):
        return "集成/同步"
    if any(k in n for k in ["generat", "report", "notes", "summary", "digest"]):
        return "生成/报告"
    if any(k in n for k in ["portal", "page", "site", "app", "store", "booking"]):
        return "门户/App"
    if any(k in n for k in ["automation", "reminder", "escalat", "notify", "alert"]):
        return "自动化"
    return "模块"

rows = []
detail_md = []

# Slack
for slug, name in SLACK_TEMPLATES:
    tname, url, feats, err = slack_features(slug, name)
    detail_md.append({"product": "Slack", "name": tname or name, "desc": "", "url": url, "composition": "", "modules": feats, "err": err})
    for i, f in enumerate(feats, 1):
        rows.append([f"TP-SL-{slug}", "slack", name, "", i, f, slack_type(f), "", "", url])
    time.sleep(0.3)

# Taskade
for cat in TD_CATEGORIES:
    try:
        durl, slug = td_first_detail(cat)
        if not durl:
            detail_md.append({"product": "Taskade", "name": cat, "url": f"https://www.taskade.com/templates/{cat}", "composition": "", "modules": [], "err": "未找到详情页"})
            continue
        title, desc, inc, comp = td_detail(durl)
        detail_md.append({"product": "Taskade", "name": title or slug, "desc": desc, "url": durl, "composition": comp, "modules": [f"{a}：{b}" if b else a for a, b in inc], "err": ""})
        for i, (mod, d) in enumerate(inc, 1):
            rows.append([f"TP-TD-{slug}", "taskade", title or slug, desc, i, mod, td_type(mod), d, comp, durl])
        time.sleep(0.3)
    except Exception as e:
        detail_md.append({"product": "Taskade", "name": cat, "url": f"https://www.taskade.com/templates/{cat}", "composition": "", "modules": [], "err": str(e)})

# ---------- 输出 CSV ----------
csv_path = os.path.join(BASE, "08-template-modules.csv")
with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["template_id", "product", "template_name", "template_one_liner", "module_no", "module_name", "module_type", "detail", "composition", "evidence_url"])
    w.writerows(rows)
print("csv:", csv_path, len(rows), "module rows")

# ---------- 输出 MD ----------
md_lines = ["# 模板解剖：这些模板里到底有哪些模块", "",
            "> 用途：**不用点开 URL 也能知道一个模板由哪些模块组成**；决定参考哪个之后，再点最后的链接。",
            "> 生成方式：Taskade 用官方 `Accept: text/markdown` 抓详情页的「What's Included」；Slack 抓详情页的「Template features」。", ""]
for d in detail_md:
    md_lines.append(f"## {d['product']} · {d['name']}")
    md_lines.append("")
    if d.get("desc"):
        md_lines.append(f"**一句话**：{d['desc']}")
        md_lines.append("")
    if d["composition"]:
        md_lines.append(f"**组合**：{d['composition']}")
        md_lines.append("")
    if d["err"]:
        md_lines.append(f"> 抓取备注：{d['err']}")
    elif d["modules"]:
        for i, m in enumerate(d["modules"], 1):
            md_lines.append(f"{i}. {m}")
    else:
        md_lines.append("（无模块信息）")
    md_lines.append("")
    md_lines.append(f"模板页：{d['url']}")
    md_lines.append("")

md_path = os.path.join(BASE, "09-template-anatomy.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))
print("md:", md_path, len(md_lines), "lines")

# 控制台摘要
for d in detail_md:
    print(d["product"], "|", d["name"], "| modules:", len(d["modules"]), "|", d["composition"], "|", d["err"])
