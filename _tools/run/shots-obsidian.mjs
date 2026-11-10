const task = await taskSpace("ai-product-sense-20261109");
const page = task.page("p1");
const fs = await import("node:fs/promises");
const OUT = "D:/claudework/teardown-100/_raw";

const targets = ["https://obsidian.md/", "https://obsidian.md/pricing", "https://obsidian.md/sync", "https://obsidian.md/publish"];
const rows = [];
for (const u of targets) {
  try {
    await page.goto(u, { timeout: 90000, waitUntil: "domcontentloaded" });
    await page.waitForTimeout(3000);
    const info = await page.evaluate(() => {
      const imgs = [...document.querySelectorAll("img")].map((i) => ({
        src: i.currentSrc || i.src || "",
        alt: (i.alt || "").slice(0, 60),
        w: i.naturalWidth,
        h: i.naturalHeight,
      })).filter((x) => x.src && !x.src.startsWith("data:"));
      const og = document.querySelector('meta[property="og:image"]');
      const hero = [...document.querySelectorAll("video, source")].map((v) => v.src || v.getAttribute("src") || "").filter(Boolean);
      return { og: og ? og.content : "", imgs: imgs.slice(0, 40), hero };
    });
    rows.push("## " + u + "\nog:image=" + info.og + "\nvideo/source:\n" + info.hero.join("\n") + "\n\nimages:\n" + info.imgs.map((x) => `- [${x.w}x${x.h}] ${x.src}  alt="${x.alt}"`).join("\n"));
    console.log(u, "imgs=" + info.imgs.length);
  } catch (e) {
    rows.push("## FAILED " + u + " " + String(e).slice(0, 150));
    console.log("FAIL", u);
  }
}
await fs.writeFile(OUT + "/obsidian-shots.md", "# 截图候选\n\n" + rows.join("\n\n---\n\n"), "utf8");
console.log("WROTE");
