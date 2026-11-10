// G2 评论采集器（第二源）：改 SLUG / NAME 后运行
//   ego-browser nodejs -e "await import('file:///D:/claudework/ljg%20OPC%20harness%20agent/.ego/reviews-g2-notion.mjs')"
// 产物：D:\ObsidianVault\03-Resources\product sense\_采集\<slug>-G2评论.md
// 关键：G2 的星级 URL 筛选不生效，必须用 "Lowest Rated" 排序；dislike 是结构化字段（连 5 星也有）

const SLUG = "obsidian";
const NAME = "Obsidian";

const fs = await import("node:fs/promises");
const OUT = "D:/claudework/teardown-100/_raw";
await fs.mkdir(OUT, { recursive: true });

const task = await taskSpace("ai-product-sense-20261109");
const page = task.page("p1");
const dismiss = async () => {
  await page.keyboard.press("Escape").catch(() => {});
  try { await page.cdp("Browser.setPermission", { permission: { name: "notifications" }, setting: "denied" }); } catch (e) {}
};

const extract = () =>
  page.evaluate(() => {
    const t = (document.body.innerText || "").replace(/\r/g, "");
    // 星级分布：直接从筛选链接抓，最可靠
    const dist = [...document.querySelectorAll('a[href*="nps_score"]')]
      .map((a) => (a.innerText || "").replace(/\s+/g, " ").trim())
      .filter((x) => /\d\s*star/i.test(x));
    const overall = (t.match(/([\d.]+)\/5\s*\(([\d,]+)\)/) || []).slice(1);
    const blocks = [];
    const re = /What do you like best about [^\n?]*\?\s*([\s\S]*?)\s*What do you dislike about [^\n?]*\?\s*([\s\S]*?)\s*(?:What problems|Show More|Validated Reviewer|Current User)/g;
    let m;
    let lastIdx = 0;
    while ((m = re.exec(t)) !== null) {
      const before = t.slice(Math.max(0, m.index - 400), m.index);
      const rm = [...before.matchAll(/([1-5])\/5/g)];
      const rating = rm.length ? rm[rm.length - 1][1] : null;
      const tm = [...before.matchAll(/“([^”]{8,140})”/g)];
      const title = tm.length ? tm[tm.length - 1][1] : "";
      const like = m[1].replace(/Review collected by and hosted on G2\.com\./g, "").trim();
      const dislike = m[2].replace(/Review collected by and hosted on G2\.com\./g, "").trim();
      if (dislike.length > 8) blocks.push({ rating, title, like: like.slice(0, 800), dislike: dislike.slice(0, 800) });
      lastIdx = m.index;
    }
    return { dist, overall, blocks };
  });

const out = { slug: SLUG, name: NAME, dist: [], overall: [], lowRated: [], default: [] };

// 1) 默认页：拿分布 + 总和
try {
  await page.goto(`https://www.g2.com/products/${SLUG}/reviews`, { timeout: 90000, waitUntil: "domcontentloaded" });
  await page.waitForTimeout(5000);
  await dismiss();
  await page.waitForTimeout(2500);
  const a = await extract();
  out.dist = a.dist;
  out.overall = a.overall;
  out.default = a.blocks.slice(0, 5);
  console.log("DEFAULT dist=" + JSON.stringify(a.dist) + " overall=" + JSON.stringify(a.overall));
} catch (e) {
  console.log("DEFAULT FAIL " + String(e).slice(0, 150));
}

// 2) 按 Lowest Rated 排序：拿差评（URL 参数才生效，select 是隐藏控件）
try {
  await page.goto(`https://www.g2.com/products/${SLUG}/reviews?order=lowest_rated`, { timeout: 90000, waitUntil: "domcontentloaded" });
  await page.waitForTimeout(5500);
  await dismiss();
  await page.waitForTimeout(2000);
  for (let i = 0; i < 4; i++) { await page.mouse.wheel(0, 1700).catch(() => {}); await page.waitForTimeout(1300); }
  const b = await extract();
  out.lowRated = b.blocks.slice(0, 12);
  console.log("LOWRATED blocks=" + b.blocks.length + " ratings=" + JSON.stringify(b.blocks.slice(0, 12).map((x) => x.rating)));
} catch (e) {
  console.log("LOWRATED FAIL " + String(e).slice(0, 200));
}

const today = new Date().toISOString().slice(0, 10);
const L = [];
L.push("# G2 用户评论采集：" + NAME + "（" + today + "）");
L.push("");
L.push("> 来源：https://www.g2.com/products/" + SLUG + "/reviews");
L.push("> 总分/评论数：" + (out.overall.join(" / ") || "?") + " ｜ 分布：" + (out.dist.join(" · ") || "?"));
L.push("> 抓法：按 **Lowest Rated** 排序（G2 的星级 URL 筛选不生效）。");
L.push("> **G2 的『What do you dislike』是结构化字段，连 5 星用户也会写——这是改进空间的直接来源。**");
L.push("");
L.push("## 差评（按 Lowest Rated 排序，带星级）");
L.push("");
if (!out.lowRated.length) L.push("（抓取失败）");
out.lowRated.forEach((b, i) => {
  L.push("### " + (i + 1) + ". " + (b.rating ? b.rating + "/5" : "星级未读到") + " · " + (b.title || "（无标题）"));
  L.push("");
  L.push("**不满：** " + b.dislike);
  L.push("");
  L.push("> 喜欢： " + b.like.slice(0, 260));
  L.push("");
});
L.push("## 默认页混采（含 4-5 星，看他们也不满意什么）");
L.push("");
out.default.forEach((b, i) => {
  L.push("- " + (b.rating || "?") + "/5 ｜ 不满：" + b.dislike.slice(0, 300));
});
await fs.writeFile(OUT + "/" + SLUG + "-G2评论.md", L.join("\n"), "utf8");
await fs.writeFile(OUT + "/" + SLUG + "-G2评论.json", JSON.stringify(out, null, 1), "utf8");
console.log("WROTE " + OUT + "/" + SLUG + "-G2评论.md");
