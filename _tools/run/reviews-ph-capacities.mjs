// 评论采集器：改最上面两行，然后运行
//   ego-browser nodejs -e "await import('file:///D:/claudework/ljg%20OPC%20harness%20agent/.ego/reviews-<slug>.mjs')"
// 产物：D:\ObsidianVault\03-Resources\product sense\_采集\<slug>-评论.md
// 抓什么：①AI 汇总的 Pros/Cons 抱怨计数 ②最新评论正文 ③1 星 ④2 星 原话

const SLUG = "capacities";      // ← PH 产品页 slug
const NAME = "Capacities";      // ← 产品名

const fs = await import("node:fs/promises");
const OUT = "D:/claudework/teardown-100/_raw";
await fs.mkdir(OUT, { recursive: true });

const task = await taskSpace("ai-product-sense-20261109");
const page = task.page("p1");
const dismiss = async () => {
  await page.keyboard.press("Escape").catch(() => {});
  await page.evaluate(() => {
    try { Object.defineProperty(window, "Notification", { configurable: true, writable: true, value: { requestPermission: () => Promise.resolve("denied") } }); } catch (e) {}
  }).catch(() => {});
};

const extract = () =>
  page.evaluate(() => {
    const SEL = '[data-test^="detailed-review-"][data-test$="-actionbar"]';
    const bars = [...document.querySelectorAll(SEL)];
    const seenId = new Set();
    const seenText = new Set();
    const items = [];
    for (const b of bars) {
      const id = b.getAttribute("data-test").replace("detailed-review-", "").replace("-actionbar", "");
      if (seenId.has(id)) continue;
      // 向上找到第一层"只包住这一条评论"的容器，避免把整个列表吸进来
      let el = b;
      let card = null;
      for (let i = 0; i < 8 && el.parentElement; i++) {
        el = el.parentElement;
        if (el.querySelectorAll(SEL).length === 1) {
          card = el;
          break;
        }
      }
      const text = ((card || b).innerText || "").replace(/\s+/g, " ").trim();
      const key = text.slice(0, 120);
      if (seenText.has(key)) continue;
      seenId.add(id);
      seenText.add(key);
      items.push({ id, text: text.slice(0, 1500) });
    }
    const body = (document.body.innerText || "").replace(/\s+/g, " ");
    const m = body.match(/Summarized with AI(.{0,1600}?)(?:Loom|Promoted|All Reviews)/);
    const total = (body.match(/([\d.,KkMm]+)\s+reviews/) || [])[1] || null;
    return { items, summary: m ? m[1].trim() : null, total };
  });

const out = { slug: SLUG, name: NAME, total: null, summary: null, latest: [], one: [], two: [] };

// 先把通知权限关掉，避免站点弹权限框打断采集
try {
  await page.cdp("Browser.setPermission", { permission: { name: "notifications" }, setting: "denied" });
} catch (e) {}

try {
  await page.goto("https://www.producthunt.com/products/" + SLUG + "/reviews", { timeout: 90000, waitUntil: "domcontentloaded" });
  await page.waitForTimeout(3000);
  await dismiss();
  await page.waitForTimeout(1500);
  for (let i = 0; i < 2; i++) { await page.mouse.wheel(0, 1800); await page.waitForTimeout(1200); }
  const base = await extract();
  out.total = base.total;
  out.summary = base.summary;
  out.latest = base.items.slice(0, 8);

  for (const star of ["1", "2"]) {
    try {
      const clicked = await page.evaluate((s) => {
        const el = document.querySelector('[data-test="rating-filter-' + s + '"]');
        if (!el) return false;
        el.scrollIntoView({ block: "center" });
        el.click();
        return true;
      }, star);
      if (!clicked) throw new Error("filter not found");
      await page.waitForTimeout(4000);
      await page.mouse.wheel(0, 1200);
      await page.waitForTimeout(1500);
      const got = await extract();
      out[star === "1" ? "one" : "two"] = got.items.slice(0, 8);
      console.log("star" + star + " -> " + got.items.length + " reviews");
    } catch (e) {
      console.log("star" + star + " FAIL " + String(e).slice(0, 120));
    }
  }
} catch (e) {
  console.log("FAIL " + String(e).slice(0, 200));
}

const today = new Date().toISOString().slice(0, 10);
const L = [];
L.push("# 用户评论采集：" + NAME + "（" + today + "）");
L.push("");
L.push("> 来源：Product Hunt 评论区 `https://www.producthunt.com/products/" + SLUG + "/reviews`");
L.push("> 总评论数：" + (out.total || "未知"));
L.push("");
L.push("## AI 汇总的 Pros / Cons（抱怨计数就是痛点分布）");
L.push("");
L.push(out.summary || "（未抓到汇总段，手动看页面）");
L.push("");
for (const [label, list] of [["最新评论（全星级）", out.latest], ["1 星评论", out.one], ["2 星评论", out.two]]) {
  L.push("## " + label + "（" + list.length + " 条）");
  L.push("");
  if (!list.length) L.push("（无 / 抓取失败）");
  for (const it of list) {
    L.push("- " + it.text);
    L.push("");
  }
}
await fs.writeFile(OUT + "/" + SLUG + "-评论.md", L.join("\n"), "utf8");
await fs.writeFile(OUT + "/" + SLUG + "-评论.json", JSON.stringify(out, null, 1), "utf8");
console.log("WROTE " + OUT + "/" + SLUG + "-评论.md  latest=" + out.latest.length + " 1star=" + out.one.length + " 2star=" + out.two.length);

