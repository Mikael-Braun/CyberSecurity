# 🚀 Basic - Level 01 — HackThisSite

![level](https://img.shields.io/badge/level-Easy-brightgreen) ![platform](https://img.shields.io/badge/platform-HackThisSite-blue) ![lang](https://img.shields.io/badge/lang-HTML-lightgrey) ![tool](https://img.shields.io/badge/tool-Browser-orange)

- **Source:** HackThisSite  
- **Type of chalenge:** Basic - Level 01
- **Difficulty:** Easy  
- **Goal:** Find the password for the next level

---

## 🔎 Description / Context
"This level is what we call "The Idiot Test." If you can't complete it, don't give up on learning as much as you can. But don't go asking others for the answer—that's one way to get disliked or made fun of. Enter the password and you can continue."

**Objective**  
Find the password for the next level.

---

## ⚙️ Prerequisites
- Any modern web browser (Chrome, Firefox, Edge)  
- Basic familiarity with browser Dev Tools / View Source (Ctrl+U)  
- Ability to read HTML comments and basic text scanning

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

1. Open the page in the browser.  
2. Press **Ctrl+U** or right‑click → **View Page Source**.  
3. Search the source for HTML comments (look for `<!--`).  
4. Locate the comment:


5. The password is **`265efd1f`** submit it to proceed to the next level.
```html
<!-- the first few levels are extremely easy: password is 265efd1f -->
```
</details>

---

## ❌ Common mistakes
- Not checking the source code and only looking at the visible page.  
- Missing HTML comments because they are hidden in the rendered page.  
- Searching only in the DOM (Elements panel) rather than using **View Source** when the comment is static in the page HTML.

---

## ✅ What I learned (notes)
- Inspecting the source code of a webpage is a simple but powerful skill that helps uncover hidden information. 
- HTML comments and leftover debug text are common places for trivial hints in early challenges.

---

## 🔗 Useful links
- HackThisSite — Basic challenges: https://www.hackthissite.org/  
- Chrome DevTools docs: https://developer.chrome.com/docs/devtools/  
- Example/support link: https://support.google.com/surveys/answer/6172725?hl=en


