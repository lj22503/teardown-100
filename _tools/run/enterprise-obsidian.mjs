const task = await taskSpace("ai-product-sense-20261109");
const page = task.page("p1");
const fs = await import("node:fs/promises");
await page.goto("https://obsidian.md/enterprise", { timeout: 90000, waitUntil: "domcontentloaded" });
await page.waitForTimeout(3000);
const txt = await page.evaluate(() => document.body.innerText);
await fs.writeFile("D:/claudework/teardown-100/_raw/obsidian-enterprise.md", "# Enterprise 页原文\n\nURL: https://obsidian.md/enterprise\n\n" + txt, "utf8");
console.log("LEN", txt.length);
console.log(txt.slice(0, 1800));
