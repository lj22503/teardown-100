// 采集模板：复制这个文件改最上面 3 行，然后用
//   ego-browser nodejs -e "await import('file:///D:/claudework/ljg%20OPC%20harness%20agent/.ego/collect-<slug>.mjs')"
// 运行（注意：ego-browser 脚本不继承 shell 环境变量，路径必须写绝对路径；中文只能写在文件里）
//
// 产物：D:\ObsidianVault\03-Resources\product sense\_采集\<slug>.md

const SLUG = "product-slug";          // ← 改这里：PH 产品页 slug
const NAME = "产品名";                 // ← 改这里：产品名
const URLS = [                         // ← 改这里：要采集的页面
  "https://www.producthunt.com/products/" + SLUG,
  "https://example.com/pricing",
];

const fs = await import("node:fs/promises");
const OUT = "D:/claudework/teardown-100/_raw";
await fs.mkdir(OUT, { recursive: true });

const task = await taskSpace(7);
const page = task.page("p1");

const dismiss = async () => {
  await page.keyboard.press("Escape").catch(() => {});
  await page.evaluate(() => {
    try {
      Object.defineProperty(window, "Notification", { configurable: true, writable: true, value: { requestPermission: () => Promise.resolve("denied") } });
    } catch (e) {}
  }).catch(() => {});
};

const chunks = [];
for (const url of URLS) {
  try {
    await page.goto(url, { timeout: 90000, waitUntil: "domcontentloaded" });
    await page.waitForTimeout(2500);
    await dismiss();
    await page.waitForTimeout(1500);
    const info = await page.evaluate(() => ({
      title: document.title,
      url: location.href,
      text: document.body.innerText.replace(/\n{3,}/g, "\n\n").trim(),
    }));
    chunks.push("## " + info.title + "\nURL: " + info.url + "\n\n" + info.text.slice(0, 14000));
    console.log(url, "len=" + info.text.length);
  } catch (e) {
    chunks.push("## FAILED " + url + "\n" + String(e).slice(0, 300));
    console.log(url, "FAIL", String(e).slice(0, 150));
  }
}

const today = new Date().toISOString().slice(0, 10);
const header = "# 采集：" + NAME + "（" + today + "）\n\n> 自动抓取原文，未加工。用于拆解卡的事实来源。\n\n";
await fs.writeFile(OUT + "/" + SLUG + ".md", header + chunks.join("\n\n---\n\n"), "utf8");
console.log("WROTE", OUT + "/" + SLUG + ".md");
