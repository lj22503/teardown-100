# -*- coding: utf-8 -*-
"""把一个产品的 content.json 渲染成中英双语 HTML 报告。

用法：
    python _tools/build_teardown.py 001-notion

输入：
    <dir>/content.json        该产品的全部文案（zh / en 两套）+ 来源 + 关键信号卡
    _tools/template-zh.html   报告模板（中文）
    _tools/template-en.html   报告模板（英文）

输出：
    <dir>/teardown-zh.html
    <dir>/teardown-en.html
"""
import json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "_tools")

FOOTER = {
    "zh": ('<footer>\n  <div class="brand-block">\n    <div>\n'
           '      <div class="brand-sub">Created by <strong>ranbing</strong> · 拆解100个AI+产品。</div>\n'
           '      <div class="brand-sub">— 产品拆解 · Principal PM 分析</div>\n'
           '    </div>\n  </div>\n</footer>'),
    "en": ('<footer>\n  <div class="brand-block">\n    <div>\n'
           '      <div class="brand-sub">Created by <strong>ranbing</strong> · 100 AI Product Teardowns.</div>\n'
           '      <div class="brand-sub">— Product Teardown · Principal PM Analysis</div>\n'
           '    </div>\n  </div>\n</footer>'),
}


def fill(tpl, d):
    return re.sub(r"\{\{([^{}]+)\}\}", lambda m: str(d.get(m.group(1), "")), tpl)


def brand(html, lang, c):
    label = c.get("product_label") or c.get("product") or ""
    date = c.get("date", "")
    html = html.replace('<div class="brand-chip">📊 产品拆解</div>',
                        '<div class="brand-chip">📊 拆解100个AI+产品</div>')
    if lang == "zh":
        meta = ('<div class="meta-strip">\n  <span>产品拆解 · Principal PM 分析</span>\n  <span class="dot"></span>\n'
                '  <span>生成于 %s</span>\n  <span class="dot"></span>\n  <span>产品：%s</span>\n</div>') % (date, label)
    else:
        meta = ('<div class="meta-strip">\n  <span>Product Teardown · Principal PM Analysis</span>\n  <span class="dot"></span>\n'
                '  <span>Generated %s</span>\n  <span class="dot"></span>\n  <span>Product: %s</span>\n</div>') % (date, label)
    html = re.sub(r'<div class="meta-strip">.*?</div>', meta, html, count=1, flags=re.S)

    # 来源
    src = c.get("sources_" + lang) or []
    head = "引用来源" if lang == "zh" else "Sources"
    note = ("该报告的事实层均来自以下公开页面；一手体验来自实测（燃冰）。" if lang == "zh"
            else "Every factual claim comes from the public pages below; first-hand observations come from the hands-on test.")
    if src:
        rows = "\n".join('    <li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, t) for t, u in src)
        block = ('<section id="sources" class="notice" style="margin-bottom:32px">\n'
                 '  <strong>%s：</strong>%s\n'
                 '  <ul style="margin:10px 0 0;padding-left:20px;line-height:1.9;font-size:13px">\n%s\n  </ul>\n'
                 '</section>\n\n') % (head, note, rows)
        html = html.replace("<footer>", block + "<footer>", 1)

    html = re.sub(r"<footer>.*?</footer>", FOOTER[lang], html, count=1, flags=re.S)
    html = re.sub(r'\s*<h2 class="brand-mark">[^<]*</h2>', "", html)
    return html


def clean(html, lang, c):
    # 不做未经验证的量化：隐藏体验条与星级
    hide = "<style>.ux-bar{display:none!important}.stars{display:none!important}</style>"
    html = html.replace("</head>", hide + "\n</head>", 1)
    # 关键信号：用 content.json 里写好的卡片（未公开的标 [推断]）
    cards = c.get("metrics_" + lang)
    if cards:
        html = re.sub(r'<section id="metrics" class="numbers">.*?</section>',
                      '<section id="metrics" class="numbers">\n' + cards + "\n</section>",
                      html, count=1, flags=re.S)
    return html


def append_sections(html, lang, c):
    """追加 16-19 四段（竞品地图 / 竞品技术底座 / 迁移机会 / 流量与变现），来自 content["extra_"+lang]"""
    extra = c.get("extra_" + lang) or []
    if not extra:
        return html
    na = "附录 A" if lang == "zh" else "Appendix A"
    blocks = []
    toc = []
    for i, sec in enumerate(extra, 1):
        sid = "s%d" % (15 + i)
        title = sec.get("title", "")
        body = sec.get("body", "")
        blocks.append(
            '<section id="%s">\n  <div class="section-head">\n    <span class="num">%02d</span>\n'
            '    <h3>%s</h3>\n    <span class="pill">%s</span>\n  </div>\n  %s\n</section>\n' % (sid, 15 + i, title, na, body)
        )
        toc.append('    <li><a href="#%s">%d. %s</a></li>' % (sid, 15 + i, title))
    html = html.replace("</ol>", "\n".join(toc) + "\n  </ol>", 1)
    html = html.replace("<footer>", "\n".join(blocks) + "\n<footer>", 1)
    return html


def build(dirname):
    d = os.path.join(ROOT, dirname)
    cf = os.path.join(d, "content.json")
    if not os.path.exists(cf):
        raise SystemExit("缺少 content.json: " + cf)
    c = json.load(open(cf, encoding="utf-8"))

    # 从队列里取 AI 类型（原生 / 中间态 / 嵌入），不信 content.json 里手填的标记
    ai_type, ai_reason = "待判", ""
    try:
        import csv as _csv
        _no = int(os.path.basename(d)[:3])
        for _r in _csv.DictReader(open(os.path.join(ROOT, "_data", "queue.csv"), encoding="utf-8-sig")):
            if _r.get("no") and int(_r["no"]) == _no:
                ai_type = _r.get("ai_type") or "待判"
                ai_reason = _r.get("ai_reason") or ""
                break
    except Exception:
        pass
    out = []
    _type_map = {"原生": ("NATIVE", "拔电测试：拿走 AI，产品消失 → AI 原生"),
                 "中间态": ("HYBRID", "拔电测试：拿走 AI，产品残废（能看不能用）→ AI 中间态"),
                 "嵌入": ("EMBEDDED2", "拔电测试：拿走 AI，产品照常卖 → AI 嵌入")}
    for lang in ("zh", "en"):
        tpl_path = os.path.join(TOOLS, "template-%s.html" % lang)
        tpl = open(tpl_path, encoding="utf-8").read()
        # 语言切换链接强制用实际文件名，忽略 content.json 里可能残留的旧名字
        c[lang]["LANG_ZH_HREF"] = "teardown-zh.html"
        c[lang]["LANG_EN_HREF"] = "teardown-en.html"
        c[lang]["ACTIVE_IF_ZH"] = "active" if lang == "zh" else ""
        c[lang]["ACTIVE_IF_EN"] = "active" if lang == "en" else ""
        for _k in ("NATIVE", "HYBRID", "EMBEDDED2"):
            c[lang]["ACTIVE_IF_" + _k] = ""
        _key, _text = _type_map.get(ai_type, ("", ""))
        if _key:
            c[lang]["ACTIVE_IF_" + _key] = "active"
        _six_missing = [k for k in ("SIX_1", "SIX_2", "SIX_3", "SIX_4", "SIX_5", "SIX_6")
                        if not str(c[lang].get(k, "")).strip()]
        if _six_missing:
            c[lang]["SIX_INTRO"] = ("本篇按旧框架（八维+九字段）完成，应用层六维从第 007 篇起开始填。"
                                    if lang == "zh" else
                                    "This piece used the older framework; the six-dim review starts from entry 007.")
            for _k in _six_missing:
                c[lang][_k] = "—"
        else:
            c[lang]["SIX_INTRO"] = ("六维是本系列的主框架：前三条看值不值，后三条看敢不敢用、会不会留下。"
                                    if lang == "zh" else
                                    "Six dimensions are the main framework: the first three are about value, the last three about trust and switching cost.")
        c[lang]["AI_TYPE_REASON"] = ("本片判为 **%s**。%s。（依据：%s）" % (ai_type, _text, ai_reason)) if lang == "zh" else \
            ("Classified as **%s**. %s (basis: %s)" % (ai_type, _text, ai_reason))
        html = fill(tpl, c[lang])
        html = clean(html, lang, c)
        html = append_sections(html, lang, c)
        html = brand(html, lang, c)
        left = sorted(set(re.findall(r"\{\{([^{}]*)\}\}", html)))
        dst = os.path.join(d, "teardown-%s.html" % lang)
        open(dst, "w", encoding="utf-8").write(html)
        out.append((dst, len(html), left))
    for dst, size, left in out:
        print("WROTE %s (%d bytes) 残留占位符=%d" % (os.path.basename(dst), size, len(left)))
        if left:
            print("  !!", left[:10])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("用法: python _tools/build_teardown.py 001-notion")
    build(sys.argv[1])
