# -*- coding: utf-8 -*-
"""补录 Figma 团队资源库：3 个 Weave workflow + 2 个 UI kit（含模块清单）。"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")
MOD = os.path.join(DATA, "history-template-modules.csv")
FIT = os.path.join(DATA, "history-template-fit.csv")

MOD_HEADER = ["template_id","product","template_name","template_one_liner","module_no","module_name","module_type","detail","composition","evidence_url"]
FIT_HEADER = ["template_id","product","template_name","for_whom","scenario","how_to_use","value","what_it_is","composition","evidence_url","fit_basis"]

F = "https://www.figma.com/community/"

mods = [
    # Match UI kit
    ["TP-figma-match-ui-kit","figma","Match – 约会 App UI Kit","约会/社交产品的完整 UI kit 与设计系统",1,"55+ 屏（亮/暗）","界面","light + dark 两套，40+/55+ 屏","55+ 屏 / 6 组模块",F+"file/1523609597252271295"],
    ["TP-figma-match-ui-kit","figma","Match – 约会 App UI Kit","约会/社交产品的完整 UI kit 与设计系统",2,"模块化设计系统","工具","variables / components / tokens / auto-layout","55+ 屏 / 6 组模块",F+"file/1523609597252271295"],
    ["TP-figma-match-ui-kit","figma","Match – 约会 App UI Kit","约会/社交产品的完整 UI kit 与设计系统",3,"匹配与聊天","界面","smart match cards、chat UI、profile insights","55+ 屏 / 6 组模块",F+"file/1523609597252271295"],
    ["TP-figma-match-ui-kit","figma","Match – 约会 App UI Kit","约会/社交产品的完整 UI kit 与设计系统",4,"Onboarding","界面","目标与兴趣选择流程","55+ 屏 / 6 组模块",F+"file/1523609597252271295"],
    ["TP-figma-match-ui-kit","figma","Match – 约会 App UI Kit","约会/社交产品的完整 UI kit 与设计系统",5,"安全与信任","界面","verified badge、safe chat、block/report","55+ 屏 / 6 组模块",F+"file/1523609597252271295"],
    ["TP-figma-match-ui-kit","figma","Match – 约会 App UI Kit","约会/社交产品的完整 UI kit 与设计系统",6,"个人资料构建","界面","editable prompts、lifestyle tags、photos","55+ 屏 / 6 组模块",F+"file/1523609597252271295"],
    # Material 3 Expressive
    ["TP-figma-material3-expressive","figma","Material 3 Expressive（设计系统）","把 Google M3 Expressive 指南做成可交互 Figma 系统",1,"463 variable tokens","工具","6 种颜色模式（亮/暗/中/高对比）+ Web/Android/iOS 代码语法","463 tokens / 75 组件集",F+"file/1695747533279107617"],
    ["TP-figma-material3-expressive","figma","Material 3 Expressive（设计系统）","把 Google M3 Expressive 指南做成可交互 Figma 系统",2,"75 组件集","工具","3,200+ variants、9,600+ spring-based interactions","463 tokens / 75 组件集",F+"file/1695747533279107617"],
    ["TP-figma-material3-expressive","figma","Material 3 Expressive（设计系统）","把 Google M3 Expressive 指南做成可交互 Figma 系统",3,"35 个 Expressive 形状","界面","几何参数从 Android 移植","463 tokens / 75 组件集",F+"file/1695747533279107617"],
    ["TP-figma-material3-expressive","figma","Material 3 Expressive（设计系统）","把 Google M3 Expressive 指南做成可交互 Figma 系统",4,"151 图标 + 30 文字样式","界面","Material Symbols 图标与 text styles","463 tokens / 75 组件集",F+"file/1695747533279107617"],
    ["TP-figma-material3-expressive","figma","Material 3 Expressive（设计系统）","把 Google M3 Expressive 指南做成可交互 Figma 系统",5,"文档 + 可玩原型","知识","每个组件有文档，整套可交互原型","463 tokens / 75 组件集",F+"file/1695747533279107617"],
]

fits = [
    ["TP-figma-weave-automated-ads","figma","Automated Ads（Weave）","电商/健康产品营销团队","产品图 + 短描述 → 自动生成多格式广告素材","打开 workflow → 输入产品图与描述 → 运行 Weave → 导出各格式素材","自动提取视觉、创意文案与版式，覆盖多种格式（About 原文）","AI workflow（Figma Weave）","",F+"weave_workflow/29","适合谁/场景=推断；价值=About 原文；无模块清单"],
    ["TP-figma-weave-mockfit","figma","MockFit（Weave）","设计师、营销团队","把桌面/平板/手机设计放进正确透视的屏幕 mockup","选设备 → 放入设计 → 导出","保留 mockup、边框、灯光与阴影（About 原文）","AI workflow（Figma Weave）","",F+"weave_workflow/91","适合谁/场景=推断；价值=About 原文"],
    ["TP-figma-weave-meta-ads","figma","Meta Ads for a product（Weave）","DTC 产品营销","Meta 广告素材生成","打开 workflow → 输入产品信息 → 生成","About 仅一句：perfect for DTC product marketing（信息少，未详）","AI workflow（Figma Weave）","",F+"weave_workflow/95","适合谁/场景=推断；价值=About 原文（信息有限）"],
    ["TP-figma-match-ui-kit","figma","Match – 约会 App UI Kit","约会/社交产品设计师、创业团队","从 0 设计约会 App（onboarding→匹配→聊天→付费）","复制文件 → 用 variables/components → 按 55+ 屏改 → 交付开发","55+ 屏、完整设计系统、UX 模式（About 原文）","约会 App UI kit + 设计系统","55+ 屏 / 6 组模块",F+"file/1523609597252271295","适合谁/场景=推断；模块=Key Features 原文；怎么用=推断"],
    ["TP-figma-material3-expressive","figma","Material 3 Expressive（设计系统）","Android/设计系统团队","按 Google M3 Expressive 做可交互设计系统","复制文件 → 用 463 tokens/75 组件集 → 对照文档与代码语法","463 tokens、75 组件集、3,200+ variants、151 图标、可玩原型（原文）","Material 3 Expressive 的 Figma 实现","463 tokens / 75 组件集",F+"file/1695747533279107617","适合谁/场景=推断；模块=WHAT'S INSIDE 原文；怎么用=推断"],
]

def append(path, header, rows):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        old = list(csv.reader(f))
    ids = {r[0] for r in rows}
    kept = [r for r in old[1:] if r and len(r) == len(header) and r[0] not in ids]
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(kept)
        w.writerows(rows)
    print(path, "->", len(kept) + len(rows), "rows")

append(MOD, MOD_HEADER, mods)
append(FIT, FIT_HEADER, fits)
