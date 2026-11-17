# 007 · Framer

> 三方材料：**① 我的真实体验**（2026-11-17 整理，20 分钟实测表 `实测.md`）｜**② 用户评论**（Product Hunt 与 G2 页面本次抓取被拦/失败，改用第三方评测站点转述的 G2 / Trustpilot / r/framer 原话，逐条标明转述）｜**③ 公开材料**（framer.com 官网原文、framer.com/pricing 四档与附加包、MCP 端点、Marketplace、Compare 页竞品清单）
> 规则：事实都有来源；推断标 `[推断]` 或（我的判断）；体验结论只写我实测过的，没测的写没测。

## 〇、AI 类型判定（先判，再写别的）

**结论：嵌入（Embedded）。**

- **拔电测试**：拿走 AI，Framer 仍是一个可视化建站工具——画布还在、托管还在、CMS 还在、站能建能发能改。不是"能看不能用"，也不是"照常卖"，是**照常干活，只是慢一点**。所以判定为嵌入，不是 AI 原生。
- 与 006 Claude 的差别在这一点上是决定性的：Claude 拿掉模型就剩一个空输入框，Framer 拿掉模型剩下一门完整生意（28,915 个模板资源、99.99% uptime 的托管、CMS、分析、本地化）。
- **类型决定死法**：嵌入型的风险不在"被上游吞"，在"**被 AI 生成类的侧翼追平**"——当一句话生成站的工具把"可编辑的画布 + 托管"补齐，它的差异就只剩账单与锁定，而这两样恰好是它现在最招骂的地方。

## 一、8 维度速览

| # | 维度 | 一句话结论 | 依据 |
|---|---|---|---|
| D1 | 目标用户 | 官网按岗位切入口，真实付费主力是**设计驱动的市场团队与代理商**——所有客户证言都由设计负责人出镜 | Solutions 页分 Designers / Agencies / Marketers / Growth / Builders / Engineers / Site Teams / Founders；首页客户引用 Miro、Perplexity、Zapier、FLORA、Metalab、Cradle |
| D2 | 核心问题 | 它卖的不是"AI 做站"，是**"设计稿不必再交给开发"**：省掉的是交接，不是创意 | 实测（燃冰）六维①：替掉的是设计实现这一步，几个月变几小时；官网原话 no dev handoff |
| D3 | AI 是否不可替代 | **可替代，且它自己也这么定位**：AI 负责生成骨架、文案、代码片段，判断权仍在人手里 | 拔电测试（见第〇节）；实测（燃冰）③④：能直接用，但错的前提它不纠，靠人工兜底 |
| D4 | 工作流整合 | 一条线打通：**画布（设计）→ CMS（内容）→ 托管（发布）→ 分析 / A/B / 本地化（上线后）**，中间没有交接点 | 官网模块清单：Agents、CMS、Hosting、Analytics、SEO、AEO、Convert、Localization、Marketplace |
| D5 | 商业模式 | **按站点订阅 + 按席位 + 按附加包**，三层叠；免费档能建但不能绑自定义域名 | 定价页：Free / Basic / Pro / Enterprise；编辑器 HK$81/月、内容编辑 HK$41/月；语言包 HK$81/个、Convert HK$203/50 万事件、Advanced hosting HK$811 |
| D6 | 竞争差异化 | 差异化不在模型，在**"画布即生产环境"**的手感 + 默认达标的性能与 SEO + 模板生态 | 官网首页直接摆 Core Web Vitals 实测面板（LCP 1.1s / INP 95ms / CLS 0.01）；实测（燃冰）⑥：门槛在软件本身 |
| D7 | 成本结构 | 结构性张力：**卖订阅、付带宽与推理**，所以必须用 credits 与席位把人头的账算清楚 | 定价页 credits 分档（1,000 / 3,000 起，最高 100,000）+ 超额提示升级或加购 + 带宽可超一个月 |
| D8 | 技术边界 | 边界在**技术 SEO 与自定义能力**：robots.txt 不可编辑、静态文件被锁在附加包后，复杂电商与超大规模 CMS 也不覆盖 | 第三方评测转述（AI Tools Police、bestaiq）：robots.txt 不可编辑、静态上传需 Advanced hosting；定价页 FAQ 的 CMS 上限（Pro 加购后最多 40 个集合 / 40,000 条） |

## 二、9 字段卡片

| 字段 | 值 |
|---|---|
| 产品 | Framer（官网自称 the pro website builder with a world-class design agent） |
| 队列号 / slug | 007 / framer（第 6 篇之前出现过 007-cursor 目录，进度一律以 `daily.py next` 为准） |
| 分类 | 建站工具 / AI 设计代理（Website Builders） |
| 官网 / 一手页 | https://www.framer.com ｜ 定价 https://www.framer.com/pricing ｜ MCP 端点 https://mcp.framer.com/mcp ｜ Marketplace https://www.framer.com/marketplace/ |
| 定价 | **本次抓到的是港币区域价**（访问地决定币种，见 `_raw.md`）：Free（500 credits/月、Framer 子域名、1 GB 带宽）；Basic（1,000–15,000 credits、自定义域名、2 个 CMS 集合、50 GB）；Pro（3,000–100,000 credits、10 个集合、100 GB、重定向、Staging、分支预览，A/B 与 Advanced hosting 为加购）；Enterprise（自定义额度、SSO、SCIM、无限编辑器、uptime 保障）。附加：语言包 HK$81/个（至多 20 个）、Convert HK$203/50 万事件、Advanced hosting HK$811、编辑器 HK$81/人、内容编辑 HK$41/人。退款：EU 与土耳其 14 天。**美元价为第三方评测转述（Basic \$10 / Pro \$30 / 编辑器 \$20 / Advanced hosting \$200），不作官方口径。** |
| 规模（自述 + 平台） | 可核实：Marketplace 28,915 个资源；官网写 99.99% uptime；企业客户证言含 Miro、Perplexity、Zapier、FLORA、Metalab、Cradle。第三方转述：G2 约 4.5（约 142 条）、Trustpilot 约 1.6（约 127–140 条，74% 一星）、Capterra 易用性子分全项最低。**官方未披露 ARR、站点数、付费用户数，本卡不编。** |
| AI 能力 | 设计 Agent（在画布上生成布局、区块、组件、文案）、CMS Agent、Code Agent、本地化与图像/着色器生成（消耗 credits）、MCP 外接（Claude / Codex / Cursor 可直连改站，`mcp.framer.com/mcp`） |
| 官方「不做」清单 | 不提供**代码导出**（评论反复点名，是它的商业选择）；不做原生电商（需外挂）；不放开 robots.txt 编辑与静态文件上限（除非加购 Advanced hosting）；不做"一句话全站生成完事"——官方立场是 **everything stays editable**，人必须在画布上改 |
| 实测状态 | **已实测（20 分钟，2026-11-17）**。走完"生成 / 换部件 → 看能不能发 → 判错得起吗"这一圈，六维有记录。**未测**：真实计时（没做秒表）、多语言与 A/B、团队席位协作、超额计费实际触发、迁移可行性验证——全部未测，本卡不写结论。 |

## 三、校正后的四栏

- **一句话定位**：**它不是"AI 建站"，是"设计即上线"**——画布上的东西就是生产环境，AI 只负责把从零到骨架这一段压短。
- **核心优势（1 条）**：**没有交接点**。设计、内容、托管、SEO、分析在同一条线上，实测（燃冰）的结论很直接：原来几个月的事，几小时，而且**能直接用、能直接对外发布**。这条优势的根在架构（画布即生产），不在模型——所以竞品补不上模型也没用，得连架构一起补。
- **最大短板（1 条）**：**账单不可预测**。三层计量（站点 + 席位 + credits）再叠三个附加包，付费扳机又设在"绑域名"这一刻，用户在心里算不出总价。这不是产品能力问题，是定价表达问题——但它已经吃掉了 Trustpilot（约 1.6 分、74% 一星）几乎全部口碑。
- **失效场景**（实测 + 评论证据，四条）：
  1. **要代码主权的人**：不提供导出，第三方转述原话 impossible to leave framer without export and they do not provide it；r/framer 的共识是 lock-in and lack of code export are the trade-offs。
  2. **技术 SEO 有硬要求的人**：robots.txt 不可编辑、静态文件锁在 Advanced hosting（HK$811）后面。
  3. **内容体量大的 CMS 站**：Free 档 10 个集合 / 1,000 页，Pro 加购后到 40 个集合 / 40,000 条——写内容库与目录站会很早撞墙。
  4. **出问题需要人的人**：支持机器人优先、答复慢，Trustpilot 上有"不回复负评"的标记；对一人公司是最贵的一种失败。

## 四、我的实测（2026-11-17，20 分钟）

> 署名：实测（燃冰）。原始记录：`实测.md`（来源：`D:\ObsidianVault\03-Resources\product sense\01-拆解\007-framer.md`）。**本卡所有体验结论只来自这一份记录；没测的一律写未测。**

| 观察项 | 实测结论 |
|---|---|
| 上手用时（TTV） | **未计时**。记录只写"原来几个月的事，现在几小时"——是量级，不是秒表。本卡不把它换算成分钟 |
| 哪一步停下来想「下一步该干嘛」 | **不是界面，是审美判断**：它要求我找示例、给需求；界面本身没门槛（Figma 式画布） |
| 结果改了几次才敢用 | **能直接用**，要改的是每个组件的细节；可直接对外发布（一站式建站工具） |
| 最像智能的一刻 | **按描述换部件**：拿成品设计/截图，让它换掉某个区块，产出仍是可编辑的图层而不是一张图 |
| 它不管的部分 | **错误前提不纠**：给它错的前提，它不处理这种事——判断不归它负责，靠人工兜底 |
| 出错了怎么退 | 支持 undo、有记录；结构可拆解到组件级，所以**错得起** |
| 免费与付费的墙 | 墙在**自定义域名**（定价页写明绑域名需升级）；Free 档 500 credits / 月、1 GB 带宽、3 位编辑 |
| 它主卖什么 | **省的是制作过程**，不是创意。值这个价 |
| 会不会留下 | **会**。门槛在软件本身（SEO 与设计用户习惯），不在模型；免费用户也能拿到模板与社区的价值 |
| 没测的部分 | 计时、多语言与 A/B、席位协作、超额计费触发、真实迁移成本——全部未测 |

**实测之外的一条判断**（我的判断）：我原以为它卖的是"AI 帮我做站"，走完发现它卖的是"**不用等开发**"。这两个说法差的不是措辞，是收费点——前者按生成次数收，后者按站点收。它选了后者，于是账单必须复杂，而复杂账单正是它口碑的伤口。**这条缝不是 bug，是商业模式的必然副作用。**

## 五、用户评论证据（原话，未改写）

> 采集说明：`framer-评论.md`（Product Hunt）本次为 Cloudflare 拦截、0 条；`framer-G2评论.md` 抓取失败。以下原话来自第三方评测站点对 G2 / Trustpilot / r/framer 的**直接引用**，逐条标明转述来源，**不是本报告直接抓取**。

| 原话 | 它证明了什么 | 转述来源 |
|---|---|---|
| "impossible to leave framer without export and they do not provide it" | 无导出是真实迁移墙，不是传言 | AI Tools Police（转述用户评论） |
| "lock-in and lack of code export are the trade-offs for that simplicity" | 用户自己承认这是"用简单换锁定"的清醒交易 | AI Tools Police（转述 r/framer） |
| 关于计费的四类抱怨：升级/加购超出预期、credits 被用于修 AI 自己造成的问题、取消流程、客服机器人优先 | 账单体验是口碑主战场，不是设计能力 | AI Insiders、bestaiq（转述 Trustpilot） |
| "design ownership back in our hands"（客户证言） | 它卖的第一价值是"设计权回到自己手里" | framer.com 首页客户引用 |
| 表扬集中在断点调整与动效成本（同一处改动不用重做） | 优势在"改起来便宜"，不在"生成得快" | AI Tools Police、bestaiq（汇总 G2 好评） |
| Capterra 易用性子分全项最低 | 对非设计师，词汇门槛真实存在（Breakpoint / Collection / Locale / Credits） | bestaiq（转述 Capterra） |

**分数撕裂怎么读**：G2 约 4.5（约 142 条）与 Trustpilot 约 1.6（约 127–140 条、74% 一星）同时为真。**G2 评的是产品体验，Trustpilot 评的是交易体验**——买得顺的人写前者，被账单咬过的人写后者。做决策时两个都要看：产品可以放心试，账单要先算清。

## 六、附录四段摘要

- **16 对标竞品地图**：官网 Compare 页自己列了近 20 个对手（Webflow、Figma、Wix、Squarespace、WordPress、Readymag、Ceros、Unbounce、Lovable、Claude Code、ChatGPT、Codex、Contentful、Sanity、AEM、Replit、Astro、v0）。**抢同一段链路的是 Webflow 与 Figma Sites**（画布到上线），**抢同一个需求的是 Wix / Squarespace**（非设计师要上线）与 **Lovable / v0 / Claude Code**（要源码与自由部署）。Product Hunt 的 Similar Products 区块本次未取到（Cloudflare），已注明，不编名单。
- **17 竞品技术底座**：Framer＝自研画布 + 自建托管与 CDN + 内置 CMS/分析/本地化 + 开放 MCP；Webflow＝自研可视化 CSS 引擎 + 托管 + 更强导出；Wix / Squarespace＝模板 + 拖拽 + 全托管；WordPress＝PHP/MySQL 自托管；Lovable / v0＝LLM 生成 React/Tailwind、源码可导出。`[推断]` **真护城河不在模型层**（底层能力外部可得），在"画布 + 托管 + CMS + 模板市场"的耦合；"没有导出"是人造锁定，改政策就能失去——所以它同时是护城河与风险源。
- **18 可迁移的机会（我的判断）**：① **把"示例 + 需求"做成开工前的 brief**——它的 Agent 要人先给示例，实测就卡在这里，做成三步表单就能把门槛降下来（最轻，一天能上）；② **把改动做成 diff**——它支持 undo，但不告诉人这次动了什么，而审阅能力决定人敢不敢放手；③ **账单前置**——动手前给预估 credits 与涉及的附加包；④ **把迁移出口做成产品**——"进来容易、出去也容易"是可以收信任溢价的位置。**哪个最轻？①，一个表单 + 一次确认。**
- **19 流量与变现拆解**：钱从三方出——设计驱动的市场团队与代理商（按站点）、团队里每个编辑（按席位）、重度用 AI 的人（按 credits，再叠语言 / A-B / Advanced hosting 附加包）。流量吃**长尾为主**：28,915 个模板资源页 + 近 20 个对比页接选型意图 + 客户证言做社会证明；爆款来自发布与设计社区作品展示。变现三层：**订阅（广度）→ 席位（厚度）→ 附加包（深度）**。**最脆的一根梁是"免费先建、绑域名才付"与"三层计量"之间的落差**：入口干净、出口复杂，Trustpilot 的低分几乎全砸在这里。

## 附：证据索引

- 采集原文：`_raw.md`（官网功能与模块原文、定价页四档与附加包、FAQ 超额与退款、MCP 端点、Marketplace 28,915、Compare 竞品清单、Core Web Vitals 面板）
- 评论：`framer-评论.md`（PH，Cloudflare 拦截，0 条）｜`framer-G2评论.md`（抓取失败）｜第三方转述见上表，分别来自 AI Insiders、AI Tools Police、nqz.ai、bestaiq
- 官方页：https://www.framer.com ｜ https://www.framer.com/pricing ｜ https://mcp.framer.com/mcp ｜ https://www.framer.com/marketplace/ ｜ https://www.framer.com/compare/framer-vs-wix
- 实测：`实测.md`（2026-11-17，20 分钟实测表，署名 实测（燃冰））
- 渲染产物：`teardown-zh.html` / `teardown-en.html`（由 `content.json` 生成）

---
> 本卡所有事实均可在上述来源中逐条核对；凡推断已标 `[推断]` 或（我的判断）；实测结论均标注「实测（燃冰）」，未测项目明确写「未测」；原文抓取失败的评论页面已注明，改用第三方转述并逐条标注来源，未编造评论条数与星级。
