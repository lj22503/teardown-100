# -*- coding: utf-8 -*-
"""回填 001–012 的资源层（05-resources.csv）。幂等：先删 RS-HIST-* 再加。"""
import csv, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE, "05-resources.csv")
HEADER = ["resource_id","product","resource_name","resource_type","problem_solved","how_to_access","reuse_form","reuse_score","migration_cost","evidence_strength","evidence_url"]

R = []
def add(pid, product, name, typ, problem, access, reuse, rs, mc, ev, url):
    R.append([pid, product, name, typ, problem, access, reuse, rs, mc, ev, url])

# 001 Notion
add("RS-HIST-001-1","notion","模板市场（30,000+）","模板","不知道从哪开始、要现成工作流","notion.com/templates 搜索/分类 → Duplicate","克隆后改字段与视图",5,4,"A","https://www.notion.com/templates")
add("RS-HIST-001-2","notion","Custom Agent 模板（166 个）","Agent","要一个能执行任务的 agent","notion.com/custom-agent-templates","套用模板 → 接自己的数据库",4,3,"A","https://www.notion.com/custom-agent-templates")
add("RS-HIST-001-3","notion","认证顾问（281 位）","服务","要人帮忙搭系统","notion.com/explore-consultants","按行业/语言找顾问",3,5,"A","https://www.notion.com/explore-consultants")
add("RS-HIST-001-4","notion","Connections（集成）","集成","要接外部系统","notion.com/connections","授权连接",4,4,"A","https://www.notion.com/connections")

# 002 Obsidian
add("RS-HIST-002-1","obsidian","社区插件库","插件","缺功能（日历/看板/同步等）","community.obsidian.md/plugins","装插件；或读源码改成自己的",4,2,"A","https://community.obsidian.md/plugins")
add("RS-HIST-002-2","obsidian","社区主题库","主题","想换外观/排版","community.obsidian.md/themes","装主题；或照它的 CSS 改",3,4,"A","https://community.obsidian.md/themes")
add("RS-HIST-002-3","obsidian","核心 Templates 插件","模板","新建笔记想套固定结构","help.obsidian.md/plugins/templates","设模板文件夹 → 新建时插入",3,5,"A","https://help.obsidian.md/plugins/templates")

# 003 Capacities
add("RS-HIST-003-1","capacities","Object 类型系统","结构","笔记散、想变成结构化对象","capacities.io/why-capacities","按 object 建自己的类型",4,3,"A","https://capacities.io/why-capacities")
add("RS-HIST-003-2","capacities","AI 助手（问答/生成）","Agent","想用自己的库回答问题","capacities.io（应用内 AI）","在 object/每日笔记里调用",3,3,"B","https://capacities.io/")
add("RS-HIST-003-3","capacities","每日笔记（Daily Note）","结构","每天要有一个固定收件箱","capacities.io/why-capacities","每日笔记 → 碎片升级成 object",3,5,"A","https://capacities.io/why-capacities")

# 004 Reflect
add("RS-HIST-004-1","reflect-notes","AI 助手","Agent","写/问笔记时要 AI 帮忙","reflect.app（应用内）","选中文本调用",3,3,"B","https://reflect.app/")
add("RS-HIST-004-2","reflect-notes","双链 + 每日笔记","结构","知识之间要建立关联","reflect.app","每日笔记 + [[双链]]",4,4,"A","https://reflect.app/")
add("RS-HIST-004-3","reflect-notes","Reflect Open（GitHub，MIT）","工具/源码","想自托管或改格式","github.com/team-reflect/reflect-open","拉源码/自己部署",4,2,"A","https://github.com/team-reflect/reflect-open")

# 005 HyNote
add("RS-HIST-005-1","hynote-ai","AI 笔记/转写","Agent","不想手记，想要现成摘要","hynote.ai","录音/上传 → 生成笔记",4,3,"A","https://hynote.ai/")
add("RS-HIST-005-2","hynote-ai","MCP 接入","集成","让外部 AI 读自己的笔记","hynote.ai（MCP）","配置 MCP → 外部 agent 调用",3,3,"B","https://hynote.ai/")

# 006 Claude
add("RS-HIST-006-1","claude","Prompt Library","模板","不会写提示词/想要现成范式","docs.anthropic.com/en/prompt-library","抄提示词 → 换变量",4,5,"A","https://docs.anthropic.com/en/prompt-library")
add("RS-HIST-006-2","claude","MCP 连接器","集成","要让 Claude 接外部工具/数据","modelcontextprotocol.io","装 MCP server → 授权",4,3,"A","https://modelcontextprotocol.io/")
add("RS-HIST-006-3","claude","Projects（项目上下文）","知识","每次都要重新贴背景","claude.ai（Projects）","建项目 → 放资料 → 项目内对话",4,4,"B","https://www.anthropic.com/claude")

# 007 Framer
add("RS-HIST-007-1","framer","模板市场","模板","要快速起一个站","framer.com/marketplace/templates","Remix → 换内容 → 发布",5,5,"A","https://www.framer.com/marketplace/templates/")
add("RS-HIST-007-2","framer","插件市场","插件","要扩展建站能力","framer.com/marketplace/plugins","装插件",4,4,"A","https://www.framer.com/marketplace/plugins/")
add("RS-HIST-007-3","framer","组件市场","组件","要复用 UI/交互","framer.com/marketplace/components","拖入画布/复制组件",4,5,"A","https://www.framer.com/marketplace/components/")
add("RS-HIST-007-4","framer","Agent Templates","Agent","想让 agent 直接改站","framer.com/marketplace/templates/categories/agents/","选 agent 模板 → 让 agent 改",4,3,"A","https://www.framer.com/marketplace/templates/categories/agents/")

# 009 Figma
add("RS-HIST-009-1","figma","Community 文件库","模板","要现成设计文件/UI kit","figma.com/community","Duplicate → 改",5,4,"A","https://www.figma.com/community")
add("RS-HIST-009-2","figma","团队资源库（AI workflows / Website / UI kits）","模板/资源","团队内要找可参考的成品","团队资源库（需登录）","按板块/子类筛 → 打开 → Duplicate",5,3,"A","https://www.figma.com/files/team/1666643033011782866/resources/community")
add("RS-HIST-009-3","figma","插件市场","插件","扩展设计/交付能力","figma.com/community/plugins","装插件",4,4,"A","https://www.figma.com/community/plugins")
add("RS-HIST-009-4","figma","Skills（可复用指令）","Agent","让 Figma agent 按固定方式干活","团队资源库 → Skills","选 skill → Try in…",4,4,"A","https://www.figma.com/files/team/1666643033011782866/resources/community")

# 010 Fathom
add("RS-HIST-010-1","fathom","集成（CRM/Slack/Notion/Asana/Zapier）","集成","会议结果要有去处","fathom.ai 集成页","授权连接",4,4,"A","https://www.fathom.ai/")
add("RS-HIST-010-2","fathom","Public API 与 MCP","接口","要让 ChatGPT/Claude 查会议","fathom.ai（API/MCP）","申请 key → 接 MCP",4,3,"A","https://www.fathom.ai/")
add("RS-HIST-010-3","fathom","自定义摘要模板","模板","团队有固定纪要格式","fathom.ai/pricing（功能）","建模板 → 应用到会议",4,4,"A","https://www.fathom.ai/pricing")

# 011 ElevenLabs
add("RS-HIST-011-1","elevenlabs","Voice Library","资源","要现成声音，不想自己录","elevenlabs.io/voice-library","挑声音 → 直接用/克隆",5,4,"A","https://elevenlabs.io/voice-library")
add("RS-HIST-011-2","elevenlabs","Agents 平台","Agent","要做语音 agent（电话/网页）","elevenlabs.io/agents","配 agent → 接电话/网页",4,3,"A","https://elevenlabs.io/agents")
add("RS-HIST-011-3","elevenlabs","API / SDK","接口","要把语音接进产品","elevenlabs.io/docs","接 API/SDK",3,3,"A","https://elevenlabs.io/docs")

# 012 Gamma
add("RS-HIST-012-1","gamma-3","模板库（19 类 / 100+）","模板","要快速出一份 deck/文档/网页","gamma.app/templates","选模板 → 输入内容 → 生成",5,5,"A","https://gamma.app/templates")
add("RS-HIST-012-2","gamma-3","主题/风格筛选（18 主题 / 16 风格）","主题","要统一视觉风格","gamma.app/templates 左侧筛选","按主题/风格收窄",4,5,"A","https://gamma.app/templates")
add("RS-HIST-012-3","gamma-3","生成格式（演示/文档/网页/社交卡片）","工具","同一内容要换载体","gamma.app（新建时选格式）","选格式 → 生成 → 导出",4,4,"A","https://gamma.app/")

# —— 第二轮：补模板/集成/插件/客户端等资源类型 ——
# 001 Notion
add("RS-HIST-001-5","notion","Skills（技能模板）","Agent","想让 AI 按固定流程干活","notion.com/skills-templates","选技能 → 加到 agent",4,4,"A","https://www.notion.com/skills-templates")
# 002 Obsidian
add("RS-HIST-002-4","obsidian","Web Clipper","工具","网页内容要进库","obsidian.md/clipper","浏览器扩展剪藏",4,5,"A","https://obsidian.md/clipper")
add("RS-HIST-002-5","obsidian","Canvas","界面","要白板式组织笔记","obsidian.md/canvas","建 canvas → 拖笔记/网页",3,4,"A","https://obsidian.md/canvas")
add("RS-HIST-002-6","obsidian","CLI","工具","要脚本化操作 vault","obsidian.md/cli","命令行调用",3,3,"A","https://obsidian.md/cli")
# 003 Capacities
add("RS-HIST-003-4","capacities","移动端 App（iOS/Android）","工具","手机上随手记","capacities.io","装 App → 同步",3,4,"A","https://capacities.io/")
add("RS-HIST-003-5","capacities","导入/导出（本地 Markdown）","工具","不想被锁死/要迁移","capacities.io（设置内）","导出 Markdown → 迁移",4,3,"B","https://capacities.io/")
# 004 Reflect
add("RS-HIST-004-4","reflect-notes","端到端加密 + 本地文件","工具","笔记要私密/可迁移","reflect.app","本地文件 + E2E 加密",4,3,"A","https://reflect.app/")
add("RS-HIST-004-5","reflect-notes","Mac / iOS 客户端","工具","苹果生态内使用","reflect.app","装客户端 → 同步",3,4,"A","https://reflect.app/")
# 005 HyNote
add("RS-HIST-005-3","hynote-ai","Templates（7 个）","模板","要有固定结构的输出（FAQ/简历/大纲/案例分析/SWOT/头脑风暴/访谈）","hynote.ai/features/faq-template 等 7 个模板页","选模板 → 填内容 → 生成",4,4,"A","https://hynote.ai/features/faq-template")
add("RS-HIST-005-4","hynote-ai","Integrations（20+）","集成","要把笔记接到 ChatGPT/Claude/Notion/Slack/Zoom 等","hynote.ai/integrations","授权连接",4,4,"A","https://hynote.ai/integrations")
add("RS-HIST-005-5","hynote-ai","AI Skills / AI Recipes","Agent","把笔记变成日历/提醒/邮件等动作","hynote.ai/features/ai-skills","选中文本 → 点技能",4,3,"A","https://hynote.ai/features/ai-skills")
# 006 Claude
add("RS-HIST-006-4","claude","Anthropic Cookbook","模板/示例","想看官方怎么调 API/提示词","github.com/anthropics/anthropic-cookbook","抄 notebook/示例",4,4,"A","https://github.com/anthropics/anthropic-cookbook")
add("RS-HIST-006-5","claude","Connectors（连接器目录）","集成","要让 Claude 接外部工具","claude.ai（Connectors）","授权连接",4,3,"B","https://www.anthropic.com/claude")
# 007 Framer
add("RS-HIST-007-5","framer","Vectors 市场","资源","要现成矢量素材","framer.com/marketplace/vectors","挑素材 → 用",3,5,"A","https://www.framer.com/marketplace/vectors/")
# 009 Figma
add("RS-HIST-009-5","figma","Widgets","插件/组件","要在文件里加互动小组件","figma.com/community/widgets","装 widget",3,4,"A","https://www.figma.com/community/widgets")
# 010 Fathom
add("RS-HIST-010-4","fathom","Resource Hub","模板/案例","要案例、对比、use case 参考","fathom.ai/resource-hub","按场景找案例",4,5,"A","https://www.fathom.ai/resource-hub")
add("RS-HIST-010-5","fathom","集成目录（视频会议/LLM/CRM）","集成","按类别找该接哪个","fathom.ai/integrations","按类别选 → 授权",4,3,"A","https://www.fathom.ai/integrations")
add("RS-HIST-010-6","fathom","API","接口","要程序化取会议数据","fathom.ai/features/api","申请 key → 调 API",4,3,"A","https://www.fathom.ai/features/api")
add("RS-HIST-010-7","fathom","MCP Server","接口","要让 Claude/ChatGPT 查会议","fathom.ai/features/mcp-server","配 MCP → 调用",4,3,"A","https://www.fathom.ai/features/mcp-server")
# 011 ElevenLabs
add("RS-HIST-011-4","elevenlabs","Voice Design / Cloning","工具","要定制声音","elevenlabs.io","描述生成/上传样本克隆",4,3,"A","https://elevenlabs.io/")
add("RS-HIST-011-5","elevenlabs","Dubbing / Music / SFX","工具","要多语言配音/音效","elevenlabs.io","按产品线进入",4,4,"A","https://elevenlabs.io/")

with open(PATH, "r", encoding="utf-8-sig", newline="") as f:
    old = list(csv.reader(f))
kept = [r for r in old[1:] if r and len(r) == len(HEADER) and not r[0].startswith("RS-HIST-")]
with open(PATH, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(HEADER)
    w.writerows(kept)
    w.writerows(R)
print("resources:", len(kept), "+", len(R), "=", len(kept) + len(R))

