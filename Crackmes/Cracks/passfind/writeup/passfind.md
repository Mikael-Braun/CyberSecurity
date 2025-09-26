# 🚀 passfind — Crackme.one

![level](https://img.shields.io/badge/level-Easy-brightgreen) ![platform](https://img.shields.io/badge/platform-Windows-blue) ![arch](https://img.shields.io/badge/arch-x86__64-orange) ![lang](https://img.shields.io/badge/lang-C%2FC%2B%2B-lightgrey) ![tool](https://img.shields.io/badge/tool-Ghidra-orange)

- **Author:** meist
- **Uploaded:** 01:46 AM 09/08/2025
- **Difficulty:** 1.0
- **Quality:** 4.2
- **File:** `passfind.exe`
- **Size:** `419Kb`


---

## 🔎 Description
- Very simple Windows x86-64 crackme written in C/C++. 
- Goal: find the password of the executable analizing code




---

## ▶️ Start
1. Open the executable with ghidra (more info go to the Ghidra.md file)
2. Filter in the Symbol Tree for a "main" function
3. In the Decompile window you can see the main function in C
4. Analise the main function code ,solution underneath
<details>
  <summary>Solution (steps)</summary>

5. `_mingw_printf("correct");` is what we want to achieve
6. `if (local_c == 0x5e0)` — it compares the variable to the password
7. The password is `0x5e0` (1504 in decimal)
8. Execute the program and enter `1504`

</details>





