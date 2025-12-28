# 🚀 Cryptography - interencdec — PicoCTF

![level](https://img.shields.io/badge/easy-brightgreen) ![platform](https://img.shields.io/badge/platform-PicoCTF-blue) ![lang](https://img.shields.io/badge/lang-EN-lightgrey) ![tool](https://img.shields.io/badge/tool-CyberChef-orange)

- **Source:** PicoCTF  
- **Type of challenge:** Cryptography  
- **Difficulty:** Easy  
- **Goal:** Decode the flag encrypted with layered encodings (Base64 ×2, then Caesar shift)

---

## 🔎 Description / Context

**Objective**  
You were given the file content: YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg==

---

## ⚙️ Prerequisites
- A modern web browser and access to CyberChef (or any tool/script that can do Base64 and Caesar shifts)  
- Basic familiarity with Base64 and Caesar cipher (mod 26)

---

## ▶️ Quick steps / Approach
1. decode the provided string 
2. Base64-decode the inner payload  
3. Apply a Caesar shift
4. The result is the readable flag.


---

## 🧭 Solution (SPOILER)
<details>
<summary>Solution </summary>
- Base64
- Caesar shift-7
</details>

## ❌ Common mistakes

- Trying only one decoding method (e.g., a single Base64 decode) and stopping.  
- Applying ROT13 instead of identifying the correct Caesar shift.  
- Applying the Caesar shift before fully decoding the Base64 layers.  
- Altering non-letter characters (digits, underscores, braces) when shifting — only letters should be shifted.

---

## ✅ What I learned (notes)

- Challenges often layer simple encodings; try peeling layers iteratively.  
- After Base64 decodes, check whether the result is raw bytes, a quoted string, or another encoded blob.  
- Caesar shifts can use any offset — try small shifts if the result looks close to readable text.  
- CyberChef lets you chain operations (From Base64 → From Base64 → Caesar) for rapid experimentation.

## 🔗 Useful links

- [CyberChef](https://gchq.github.io/CyberChef/) — chain `From Base64` and `Caesar` operations  
- Caesar cipher explanation: https://en.wikipedia.org/wiki/Caesar_cipher
