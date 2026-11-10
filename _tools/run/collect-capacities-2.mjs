const SLUG = "capacities";
const NAME = "Capacities";

const URLS = [
  "https://capacities.io/why-capacities",
  "https://capacities.io/whats-next",
  "https://capacities.io/whats-not-next",
  "https://capacities.io/compare/obsidian",
  "https://capacities.io/compare/evernote",
  "https://capacities.io/compare/tana",
  "https://capacities.io/compare/heptabase",
  "https://capacities.io/compare/anytype",
  "https://apps.apple.com/us/app/capacities-notes-pkm/id1542498201",
];

const fs = await import("node:fs/promises");
const OUT = "D:/claudework/teardown-100/_raw";
await fs.mkdir(OUT, { recursive: true });

const task = await taskSpace("ai-product-sense-20261109");
const page = task.page("p1");

try { await page.cdp("Emulation.setLocaleOverride", { locale: "en-US" }); } catch (e) {}
try { await page.setExtraHTTPHeaders({ "Accept-Language": "en-US,en;q=0.9" }); } catch (e) {}

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
    const info = await page.evaluate(() => ({
      title: document.title,
      url: location.href,
      text: (document.body ? document.body.innerText : "").replace(/\n{3,}/g, "\n\n").trim(),
    }));
    chunks.push("## " + info.title + "\nURL: " + info.url + "\n\n" + info.text.slice(0, 16000));
    console.log(url, "len=" + info.text.length, "title=" + info.title);
  } catch (e) {
    chunks.push("## FAILED " + url + "\n" + String(e).slice(0, 300));
    console.log(url, "FAIL", String(e).slice(0, 150));
  }
}

const today = new Date().toISOString().slice(0, 10);
const header = "# Collect round 2: " + NAME + " (" + today + ")\n\n> why / roadmap / official compare pages per rival / App Store. Raw text.\n\n";
await fs.writeFile(OUT + "/" + SLUG + "-round2.md", header + chunks.join("\n\n---\n\n"), "utf8");
console.log("WROTE", OUT + "/" + SLUG + "-round2.md");
