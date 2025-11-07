# 🚀 Basic - Level 04 — HackThisSite

![level](https://img.shields.io/badge/level-4-brightgreen) ![platform](https://img.shields.io/badge/platform-HackThisSite-blue) ![lang](https://img.shields.io/badge/lang-HTML-lightgrey) ![tool](https://img.shields.io/badge/tool-DevTools-orange)

- **Source:** HackThisSite  
- **Type of challenge:** Basic - Level 04  
- **Difficulty:** Easy  
- **Goal:** Retrieve the password that is emailed when the form is submitted

---

## 🔎 Description / Context

**Objective**  
Retrieve the password that the application sends via email and use it to complete the level.

**Context**  
Sam hardcoded a complex password into a script and wrote a helper that emails the password to him. The form contains a hidden `email` field — by changing that hidden field to your registered HackThisSite email, you can cause the password to be mailed to you.

---

## ⚙️ Prerequisites
- Any modern web browser (Chrome, Firefox, Edge)  
- Basic familiarity with browser DevTools / View Page Source (`Ctrl+U`)  
- A registered HackThisSite account with a valid email you can access

---

## ▶️ Quick steps / Approach
1. Open the target level page in your browser.  
2. Inspect the form with **Inspect Element** or **View Source**.  
3. Find the hidden email input: `<input type="hidden" name="email" value="...">`.  
4. Edit the `value` to your registered HTS email.  
5. Submit the form.  
6. Check your inbox for the emailed password, then submit that password on the challenge page.

---

## 🧭 Solution (SPOILER)
<details>
<summary>Solution (step-by-step)</summary>

1. Open the level page and inspect the HTML (Elements panel or **Ctrl+U**).  
2. Locate the hidden input that controls the recipient email, for example:

```html
<input type="hidden" name="email" value="sam@example.com">
```
3. Submit the form. The server-side script will email the password to the address in that hidden field.
4. ``Password: 6c58a59c``
</details>

## ❌ Common mistakes

- Not changing the hidden email field and expecting the site to email you anyway.
- Using an email address that isn't registered with your HackThisSite account.
- Overlooking the hidden input because it isn't visible in the rendered page.
---
## ✅ What I learned
- Hidden inputs can be manipulated client-side to redirect output or change recipients.
- Viewing source and using DevTools to change form fields is a core reconnaissance technique for web challenges.
- Never trust client-side controls for security server-side validation and not emailing secrets to arbitrary addresses are important.
---

## 🔗 Useful links
- Chrome DevTools — Elements panel: https://developer.chrome.com/docs/devtools/elements/
- MDN — <input type="hidden">: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/hidden
- HackThisSite — Basic challenges: https://www.hackthissite.org/