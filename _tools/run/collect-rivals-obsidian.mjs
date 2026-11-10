const SLUG = "obsidian";
const URLS = [
  "https://www.g2.com/products/obsidian/competitors/alternatives",
  "https://logseq.com/",
  "https://reflect.app/",
  "https://capacities.io/",
  "https://bear.app/",
  "https://tana.inc/",
  "https://anytype.io/",
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
    await page.waitForTimeout(1500);
    for (let i = 0; i < 2; i++) { await page.mouse.wheel(0, 1500).catch(() => {}); await page.waitForTimeout(900); }
    const info = await page.evaluate(() => ({
      title: document.title,
      url: location.href,
      text: (document.body ? document.body.innerText : "").replace(/\n{3,}/g, "\n\n").trim(),
    }));
    chunks.push("## " + info.title + "\nURL: " + info.url + "\n\n" + info.text.slice(0, 4500));
    console.log(url, "len=" + info.text.length);
  } catch (e) {
    chunks.push("## FAILED " + url + "\n" + String(e).slice(0, 200));
    console.log("FAIL", url, String(e).slice(0, 120));
  }
}

await fs.writeFile(OUT + "/" + SLUG + "-rivals.md", "# 竞品技术底座采集（" + new Date().toISOString().slice(0, 10) + "）\n\n" + chunks.join("\n\n---\n\n"), "utf8");
console.log("WROTE", OUT + "/" + SLUG + "-rivals.md");
