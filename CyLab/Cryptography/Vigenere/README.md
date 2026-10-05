# 🚀 Cryptography - Vigenère Cipher — CyLab

![level](https://img.shields.io/badge/medium-orange) ![platform](https://img.shields.io/badge/platform-CyLab-blue) ![lang](https://img.shields.io/badge/lang-EN-lightgrey) ![tool](https://img.shields.io/badge/tool-CyberChef-orange)

- **Source:** CyLab  
- **Type of challenge:** Cryptography
- **Difficulty:** Medium
- **Goal:** Decrypt the message using the key "CYLAB"

---

## 🔎 Description / Context

**Objective**  
You are given an encrypted message and the key `"CYLAB"`. The task is to use the Vigenère cipher decryption method to reveal the hidden flag. The hint points to: [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

---

## ⚙️ Prerequisites
- A modern web browser and access to CyberChef (or any tool/script that can perform Vigenère decryption)  
- Basic knowledge of the Vigenère cipher (poly-alphabetic substitution using a repeated key)

---

## ▶️ Quick steps / Approach
1. Copy the encrypted message from the file.  
2. Use CyberChef to decrypt it.  
3. CyberChef will decrypt the message and reveal the plaintext / flag. 

---

## 🧭 Solution (SPOILER)
<details>
<summary>Solution</summary>

- Vigenère Decrypt
- CYLAB

</details>


## ❌ Common mistakes

- Not repeating the key properly across the entire ciphertext.
- Confusing Vigenère decryption with Caesar or ROT13.
- Ignoring case sensitivity in the cipher (uppercase/lowercase handling).
- Trying to decrypt before confirming the correct key from hints.

## ✅ What I learned (notes)

- Vigenère is a polyalphabetic substitution cipher that repeats a key across the message.
- Tools like CyberChef simplify the process with a ready-made “Vigenère Decrypt” operation.
- Always check for non-alphabetic characters — they usually remain unchanged in Vigenère.
- Knowing the key is crucial — without it, frequency analysis is needed (harder for beginners).

## 🔗 Useful links

- CyberChef https://gchq.github.io/CyberChef/
