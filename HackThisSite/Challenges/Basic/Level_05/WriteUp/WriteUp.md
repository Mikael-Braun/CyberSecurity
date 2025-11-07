# 🚀 Basic - Level 05 — HackThisSite

![level](https://img.shields.io/badge/level-5-brightgreen) ![platform](https://img.shields.io/badge/platform-HackThisSite-blue) ![lang](https://img.shields.io/badge/lang-HTML-lightgrey) ![tool](https://img.shields.io/badge/tool-DevTools-orange)

- **Source:** HackThisSite  
- **Type of challenge:** Basic - Level 05  
- **Difficulty:** Easy  
- **Goal:** Retrieve the password that is emailed when the form is submitted

---

## 🔎 Description / Context

**Objective**  
Retrieve the password that the application sends via email and use it to complete the level.

**Context**  
Sam attempted to make the email helper a bit more secure after people scripted submissions. The mechanism is the same idea as Level 04: a hidden email field controls where the password is sent. This level demonstrates that client-side values (hidden inputs) can be inspected and changed to alter behavior — unless the server validates them.

---

## ⚙️ Prerequisites
- Any modern web browser (Chrome, Firefox, Edge)  
- Basic familiarity with browser DevTools / View Page Source (`Ctrl+U`)  
- A registered HackThisSite account with an accessible email

---

## ▶️ Quick steps / Approach
1. Open the target level page in your browser.  
2. Inspect the page (Inspect Element or View Source).  
3. Locate the hidden input that contains the recipient email (e.g. `<input type="hidden" name="email" value="...">`).  
4. Edit that `value` to your registered HTS email.  
5. Submit the form.  
6. Check your email for the password, then submit it on the challenge page.

---

## 🧭 Solution (SPOILER)
<details>
<summary>Solution (step-by-step)</summary>

1. Open the level page and inspect the HTML (Elements panel or **Ctrl+U**).  
2. Find the hidden input controlling the recipient email, for example:

```html
<input type="hidden" name="email" value="sam@example.com">
```
3. Edit the value in DevTools (right‑click → Edit attribute) and set it to your registered HackThisSite email
4. Submit the form. The site will send the password to the address specified in that hidden field.
5. ``Password:c5b81392 ``
</details>

## ❌ Common mistakes

- Not changing the hidden email field and expecting the site to email you anyway.
- Using an email address that isn't registered with your HackThisSite account.
- Overlooking the hidden input because it isn't visible in the rendered page.
- Assuming client-side changes always work sometimes the server validates and rejects unrecognized addresses.
---
## ✅ What I learned

- Client-side controls (including hidden inputs) can be inspected and modified — they are not a secure means of enforcing behavior.
- Always validate important actions on the server side; never trust client-provided values for security-critical flows.
- DevTools and viewing source are fundamental for basic web challenge reconnaissance.

## 🔗 Useful links

- MDN — Form validation and controls: https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation
- Chrome DevTools — Elements panel: https://developer.chrome.com/docs/devtools/elements/
- MDN — <input type="hidden">: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/hidden
- HackThisSite — Basic challenges: https://www.hackthissite.org/