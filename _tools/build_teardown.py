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


def build(dirname):
    d = os.path.join(ROOT, dirname)
    cf = os.path.join(d, "content.json")
    if not os.path.exists(cf):
        raise SystemExit("缺少 content.json: " + cf)
    c = json.load(open(cf, encoding="utf-8"))
    out = []
    for lang in ("zh", "en"):
        tpl_path = os.path.join(TOOLS, "template-%s.html" % lang)
        tpl = open(tpl_path, encoding="utf-8").read()
        html = fill(tpl, c[lang])
        html = clean(html, lang, c)
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
