# 🚀 Basic - Level 03 — HackThisSite

![level](https://img.shields.io/badge/level-3-brightgreen) ![platform](https://img.shields.io/badge/platform-HackThisSite-blue) ![lang](https://img.shields.io/badge/lang-HTML-lightgrey) ![tool](https://img.shields.io/badge/tool-DevTools-orange)

- **Source:** HackThisSite  
- **Type of challenge:** Basic - Level 03  
- **Difficulty:** Easy  
- **Goal:** Find the password hidden in a referenced file and submit it to progress

---

## 🔎 Description / Context

**Objective**  
Find the password hidden in a file that is referenced by the page and submit it to pass the level.

**Context**  
This time the password file has actually been uploaded, but the file is referenced only indirectly from the HTML (for example via a hidden input or an unlinked path). The lesson is to inspect the HTML source for references to hidden files and navigate directly to them.

---

## ⚙️ Prerequisites
- Any modern web browser (Chrome, Firefox, Edge)  
- Basic familiarity with browser DevTools / View Page Source (`Ctrl+U`)  
- Ability to type a URL directly into the address bar and open resources

---

## ▶️ Quick steps / Approach
1. Open the target level page in your browser.  
2. View the page source (`Ctrl+U`) or Inspect Element (DevTools).  
3. Look for references to hidden files — e.g. `<input type="hidden" name="file" value="password.php">`, comments or script variables that point to a file path.  
4. Construct the direct URL to the referenced file (for example `.../missions/basic/3/password.php`).  
5. Open that URL in your browser, copy the password from the file, and submit it on the challenge page.

---

## 🧭 Solution (SPOILER)
<details>
<summary>Solution (step-by-step)</summary>

1. Open the level page and inspect the HTML (Elements panel or **Ctrl+U**).  
2. Search for hidden inputs or any text that looks like a path or filename (look for `hidden`, `password`, `file`, `.php`, `.txt`, etc.). Example hint you might find:

```html
<input type="hidden" name="pwfile" value="password.php">
<!-- or a comment like: file: /missions/basic/3/password.php -->
 ```
</details>

## ❌ Common mistakes

- Ignoring hidden inputs or script variables that reference files.  
- Trying to guess the password instead of following the path found in the HTML.  
- Forgetting to check comments — authors often leave hints there.
---
## ✅ What I learned

- Hidden inputs and unlinked file references in HTML can point directly to resources containing secrets (on CTF-style sites).  
- Viewing source and navigating to referenced files is a fundamental reconnaissance skill for web challenges.  
- Never store real secrets in accessible files or in HTML comments on production sites.
---
## 🔗 Useful links

- MDN — ``<input type="hidden">``: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/hidden  
- Chrome DevTools — Elements panel: https://developer.chrome.com/docs/devtools/  
- HackThisSite — Basic challenges: https://www.hackthissite.org/
