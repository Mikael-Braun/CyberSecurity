# 🚀 Cryptography - Mod 26 — PicoCTF

![level](https://img.shields.io/badge/easy-brightgreen) ![platform](https://img.shields.io/badge/platform-PicoCTF-blue) ![lang](https://img.shields.io/badge/lang-EN-lightgrey) ![tool](https://img.shields.io/badge/tool-CyberChef-orange)

- **Source:** PicoCTF  
- **Type of challenge:** Cryptography  
- **Difficulty:** Easy  
- **Goal:** Decode the flag encrypted with ROT13

---

## 🔎 Description / Context

**Objective**  
Given the ciphertext `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}` and the hint “do you know what ROT13 is?”, apply ROT13 to recover the flag.

---

## ⚙️ Prerequisites
- A modern web browser and access to CyberChef (or any tool/script that performs ROT13)  
- Basic knowledge of how to use CyberChef or how to run a small Python script

---

## ▶️ Quick steps / Approach
1. Open CyberChef.  
2. Paste the ciphertext into the input panel.  
3. From the operations list, add **ROT13** (or search for “ROT13”).  
4. CyberChef will apply ROT13 and display the decoded text in the output panel.  
*(Alternative: run a short Python script using `codecs.decode(s, 'rot_13')`.)*

---

## 🧭 Solution (SPOILER)
<details>
<summary>Solution (step-by-step)</summary>

1. Ciphertext:  cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}
2.  Applying **ROT13** (CyberChef → ROT13) yields: picoCTF{next_time_I'll_try_2_rounds_of_rot13_Aphnytiq}
</details>

## ❌ Common mistakes

- Not trying ROT13 first (e.g., attempting manual Caesar shifts without testing ROT13).
- Removing or altering characters (quotes, underscores, braces) before decoding.
- Assuming a more complex cipher when the hint explicitly indicates ROT13.

---

## ✅ What I learned (notes)

- ROT13 is symmetric and frequently used in beginner CTFs; it’s one of the first transforms to try when encountering obfuscated text.
- CyberChef is excellent for quickly testing transformations and viewing results in real time.
- Flags sometimes include seemingly odd suffixes — that’s intended by challenge designers.

## 🔗 Useful links

- CyberChef https://gchq.github.io/CyberChef/ 
