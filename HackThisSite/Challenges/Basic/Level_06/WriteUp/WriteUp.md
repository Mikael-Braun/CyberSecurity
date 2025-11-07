# 🚀 Basic - Level 06 — HackThisSite

![level](https://img.shields.io/badge/level-6-brightgreen) ![platform](https://img.shields.io/badge/platform-HackThisSite-blue) ![lang](https://img.shields.io/badge/lang-HTML-lightgrey) ![tool](https://img.shields.io/badge/tool-Paper%20%26%20Pen-orange)

- **Source:** HackThisSite  
- **Type of challenge:** Basic - Level 06  
- **Difficulty:** Medium  
- **Goal:** Retrieve the password by decrypting a simple cipher

---

## 🔎 Description / Context

**Objective**  
Retrieve the password that has been encrypted using a simple, predictable cipher.

**Context**  
Network Security Sam has encrypted his password using a basic cipher. The encryption system is publicly available via the form on the page. By observing how the cipher transforms input, you can reverse the pattern to decode the given string and obtain the password.

---

## ⚙️ Prerequisites
- Paper and pen for manually analyzing patterns  
- Patience and logical reasoning to detect the cipher rules  
- Optional: spreadsheet or calculator to help track transformations

---

## ▶️ Quick steps / Approach
1. Observe how the input text is transformed when entered in the cipher box.  
2. Test simple patterns (e.g., `aaaaa`, `12345`, `abcabc`) to see how characters shift.  
3. Identify the transformation rule or algorithm from the observed patterns.  
4. Apply the reverse of the cipher to the given encoded string to retrieve the original password.  
5. Submit the decoded password to complete the level.

---

## 🧭 Solution (SPOILER)
<details>
<summary>Solution (step-by-step)</summary>

1. Open the level page and type simple test patterns in the cipher box, such as:
``aaaaa
12345
abcabc``

2. Observe how each character is transformed. For example, numbers may be shifted by +2, letters may rotate forward in the alphabet, etc.  
3. Deduce the underlying algorithm by comparing input and output patterns.  
4. Once the transformation pattern is understood, reverse it on the provided encrypted password.  
5. From the positions 12345 they shift: 01234 (alphanumeric)

**Tip:** Write down the transformations for each character position to make it easier to reverse the cipher.

</details>

---

## ❌ Common mistakes
- Ignoring the possibility of simple, predictable patterns.  
- Assuming a complex algorithm and skipping basic pattern testing.  
- Not recording observed transformations systematically.

---

## ✅ What I learned
- Simple ciphers teach pattern recognition and logical deduction.  
- Observing input-output relationships can help deduce unknown algorithms.  
- Manual analysis is still valuable, even in the age of automated cryptography tools.

---

## 🔗 Useful links
- GeeksforGeeks — Simple Substitution Cipher: https://www.geeksforgeeks.org/simple-substitution-cipher/  
- Cryptography basics: https://en.wikipedia.org/wiki/Substitution_cipher  
- HackThisSite — Basic challenges: https://www.hackthissite.org/

