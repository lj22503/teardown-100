const SLUG = "obsidian";
const NAME = "Obsidian";
const URLS = [
  "https://www.producthunt.com/products/" + SLUG,
  "https://obsidian.md/",
  "https://obsidian.md/pricing",
  "https://obsidian.md/download",
  "https://obsidian.md/plugins",
];

const fs = await import("node:fs/promises");
const OUT = "D:/claudework/teardown-100/_raw";
await fs.mkdir(OUT, { recursive: true });

const task = await taskSpace("ai-product-sense-20261109");
const page = task.page("p1");

const dismiss = async () => {
  await page.keyboard.press("Escape").catch(() => {});
  try { await page.cdp("Browser.setPermission", { permission: { name: "notifications" }, setting: "denied" }); } catch (e) {}
};

const chunks = [];
for (const url of URLS) {
  try {
    await page.goto(url, { timeout: 90000, waitUntil: "domcontentloaded" });
    await page.waitForTimeout(3000);
    await dismiss();
    await page.waitForTimeout(2000);
    const info = await page.evaluate(() => ({
      title: document.title,
      url: location.href,
      text: (document.body ? document.body.innerText : "").replace(/\n{3,}/g, "\n\n").trim(),
    }));
    chunks.push("## " + info.title + "\nURL: " + info.url + "\n\n" + info.text.slice(0, 14000));
    console.log(url, "len=" + info.text.length);

    // PH 产品页：专门抓 Similar Products 段
    if (/producthunt\.com/.test(url)) {
      const sim = await page.evaluate(() => {
        const res = { found: false, block: [], links: [] };
        const nodes = [...document.querySelectorAll("h1,h2,h3,h4,div,span,p")];
        const h = nodes.find((e) => /similar products/i.test((e.innerText || "").trim()) && (e.innerText || "").trim().length < 60);
        if (!h) return res;
        res.found = true;
        let sec = h.closest("section") || h.parentElement;
        for (let i = 0; i < 4 && sec && (sec.innerText || "").length < 200; i++) sec = sec.parentElement;
        if (sec) {
          res.block = (sec.innerText || "").split("\n").map((s) => s.trim()).filter(Boolean).slice(0, 60);
          res.links = [...sec.querySelectorAll("a")].map((a) => ((a.innerText || "").trim() + " | " + a.href)).slice(0, 40);
        }
        return res;
      });
      chunks.push("## SIMILAR-PRODUCTS（产品页相似产品段）\nfound=" + sim.found + "\n\n[文本]\n" + sim.block.join("\n") + "\n\n[链接]\n" + sim.links.join("\n"));
      console.log("SIMILAR found=" + sim.found + " items=" + sim.block.length);

      // PH 页基础信息：投票数 / 评论数
      const meta = await page.evaluate(() => {
        const t = (document.body ? document.body.innerText : "").replace(/\r/g, "");
        return t.slice(0, 4000);
      });
      chunks.push("## PH-PAGE-HEAD\n" + meta);
    }
  } catch (e) {
    chunks.push("## FAILED " + url + "\n" + String(e).slice(0, 300));
    console.log(url, "FAIL", String(e).slice(0, 150));
  }
}

// 官方对比页探测：能不能打开，本身就是结论
const PROBE = [
  "https://obsidian.md/compare",
  "https://obsidian.md/vs",
  "https://obsidian.md/alternatives",
  "https://obsidian.md/switch",
];
const probes = [];
for (const u of PROBE) {
  try {
    const resp = await page.goto(u, { timeout: 60000, waitUntil: "domcontentloaded" });
    await page.waitForTimeout(2000);
    const info = await page.evaluate(() => ({
      title: document.title,
      url: location.href,
      text: (document.body ? document.body.innerText : "").replace(/\n{3,}/g, "\n\n").slice(0, 1200),
    }));
    let status = null;
    try { status = resp && resp.status ? resp.status() : (resp && resp.status) || null; } catch (e) {}
    probes.push("## PROBE " + u + "\nstatus=" + status + "\ntitle=" + info.title + "\nfinalURL=" + info.url + "\n" + info.text);
    console.log("PROBE", u, "status=" + status, "title=" + info.title);
  } catch (e) {
    probes.push("## PROBE " + u + "\nFAIL " + String(e).slice(0, 200));
    console.log("PROBE FAIL", u, String(e).slice(0, 120));
  }
}

const today = new Date().toISOString().slice(0, 10);
const header = "# 采集：" + NAME + "（" + today + "）\n\n> 自动抓取原文，未加工。用于拆解卡的事实来源。\n\n";
await fs.writeFile(OUT + "/" + SLUG + ".md", header + chunks.join("\n\n---\n\n") + "\n\n---\n\n# 官方对比页探测\n\n" + probes.join("\n\n"), "utf8");
console.log("WROTE", OUT + "/" + SLUG + ".md");
