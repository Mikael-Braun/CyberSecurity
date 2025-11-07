# 🚀 Basic - Level 2 — HackThisSite

![level](https://img.shields.io/badge/level-2-brightgreen) ![platform](https://img.shields.io/badge/platform-HackThisSite-blue) ![lang](https://img.shields.io/badge/lang-HTML-lightgrey) ![tool](https://img.shields.io/badge/tool-DevTools-orange)

- **Source:** HackThisSite  
- **Type of challenge:** Basic - Level 2
- **Difficulty:** Easy  
- **Goal:** Find the password for the next level

---

## 🔎 Description / Context

**Objective**  
Complete the level by locating the password hidden in the page source and submitting it to advance.

**Context**  
This introductory challenge teaches the basic skill of checking a web page's source for hidden information. Often beginners forget that HTML comments (`<!-- ... -->`) are visible in the page source and can contain hints or credentials deliberately placed by the challenge author.

---

## ⚙️ Prerequisites
- Any modern web browser (Chrome, Firefox, Edge)  
- Basic familiarity with browser Dev Tools / View Page Source (`Ctrl+U`)  
- Ability to read HTML comments and perform simple text scanning

---

## ▶️ Quick steps / Approach
1. Open the target level page in your browser.  
2. Right‑click → **View Page Source** (or press `Ctrl+U`).  
3. Scan the HTML for comments (`<!-- ... -->`).  
4. The comment contains the password. Enter it to advance.

---

## 🧭 Solution (SPOILER)
<details>
<summary>Solution (step-by-step)</summary>

1. Open the level page in your browser.  
2. Press **Ctrl+U** (or right‑click → **View Page Source**) to view the raw HTML.  
3. Search the source for HTML comments (look for `<!--`).  
4. Locate the comment that contains the password. For this level the comment looks like:

```html
<!-- the first few levels are extremely easy: password is 265efd1f -->
```
</details>

## ❌ Common mistakes
- Not checking the page source and only inspecting visible UI elements.
- Assuming hidden information must be obfuscated or encoded — sometimes it’s plainly in a comment.
- Overcomplicating the task (looking for JS exploitation or network manipulation) when the level is intentionally trivial.
---
## ✅ What I learned
- Always check page source / comments for low-difficulty web challenges.
- Ctrl+U / View Source is a fast, reliable first step when hunting for hints.
- HTML comments are visible to anyone who can view source never place real secrets there on production sites.
---

## 🔗 Useful links

- HackThisSite — Basic challenges: https://www.hackthissite.org/
- Chrome DevTools — View page source & Elements: https://developer.chrome.com/docs/devtools/