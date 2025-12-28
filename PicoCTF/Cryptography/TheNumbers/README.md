# 🚀 Cryptography - The Numbers — PicoCTF

![level](https://img.shields.io/badge/medium-orange) ![platform](https://img.shields.io/badge/platform-PicoCTF-blue) ![lang](https://img.shields.io/badge/lang-EN-lightgrey) ![tool](https://img.shields.io/badge/tool-CyberChef-orange)

- **Source:** PicoCTF  
- **Type of challenge:** Cryptography / Number encoding  
- **Difficulty:** Medium  
- **Goal:** Decode the numbers in the png to reveal the flag

---

## 🔎 Description / Context

**Objective**  
You are provided with an image file `numbers.png` that contains a sequence of numbers. The hint is that these numbers represent a hidden message or flag in the `PICOCTF{}` format. The challenge requires converting numbers into text.

---

## ⚙️ Prerequisites
- A modern web browser or Python environment  
- Basic understanding of ASCII codes and number-to-character conversion  
- Optional: CyberChef (for decoding sequences of numbers)  

---

## ▶️ Quick steps / Approach
1. Open `numbers.png` and extract the numbers. 
2. Convert each number  
3. Submit the flag in the format `PICOCTF{...}`.

---

## 🧭 Solution (SPOILER)
<details>
<summary>Solution </summary>

- Convert each number to its corresponding lowercase letter

</details>


## ❌ Common mistakes

- Forgetting to check whether numbers are decimal ASCII, hexadecimal, or binary.
- Concatenating numbers incorrectly (e.g., 80 73 → 8073 instead of separate characters).
- Ignoring non-visible characters (spaces or line breaks) that may appear in the number sequence.
- Submitting the flag without the correct PICOCTF{} format.

## ✅ What I learned (notes)

- Number sequences often represent ASCII codes in CTF challenges.
- CyberChef is very convenient to quickly convert lists of numbers to text.
- Always consider the format of the numbers (decimal, hex, binary).
- Visual hints (like an image) may contain hidden metadata or pixel encoding.

## 🔗 Useful links

- CyberChef https://gchq.github.io/CyberChef/ 
- PicoCTF official platform: https://picoctf.org/