# 🚀 Very_easy — Crackme.one

![level](https://img.shields.io/badge/level-Easy-brightgreen) ![platform](https://img.shields.io/badge/platform-Windows-blue) ![arch](https://img.shields.io/badge/arch-x86__64-orange) ![lang](https://img.shields.io/badge/lang-C%2FC%2B%2B-lightgrey) ![tool](https://img.shields.io/badge/tool-Ghidra-orange)

- **Author:** korshunK  
- **Uploaded:** 07:45 PM 08/02/2025  
- **Difficulty:** 1.0  
- **Quality:** 1.9  
- **File:** `very_easy.exe`  
- **Size:** `420KB`

---

## 🔎 Description
- Simple Windows x86-64 crackme written in C/C++.  
- Goal: **hack the password** :find the password of the executable analizing code

---

## ⚙️ Prerequisites
- Windows virtual machine (recommended) or Wine to run the binary safely.  
- Recommended tools: Ghidra (CodeBrowser / Decompiler) and/or a debugger (x64dbg, WinDbg).

---

## ▶️ Start
1. Open the executable with ghidra (more info go to the Ghidra.md file)
2. Filter in the Symbol Tree for a "main" function there will be more than one function with the name main
3. In the Symbol Tree, look for the `main` function or functions that call `scanf`, `fgets`, `strcmp`, `memcmp`, etc.  
4. Open the Decompile window for the main/validation function and read the generated pseudocode.  
5. Look for common patterns:
   - input reading (`scanf`, `fgets`, `ReadFile`),
   - direct comparisons (`if (x == CONST)` or `strcmp(buf, "literal")`),

---

## 📜 Code
Below are two example patterns you might find in the decompiled code.

**String comparison (literal)**:
```c
int __cdecl main(int _Argc,char **_Argv,char **_Env)
{
  int iVar1;
  char local_78 [112];
  
  __main();
  scanf("%s",local_78);
  iVar1 = strcmp(local_78,"your mum is very sexy");
  if (iVar1 == 0) {
    printf("you loose!");
  }
  else {
    puts("you win!");
    system("pause");
  }
  return 0;
  }
 ``` 
<details>
  <summary>Solution (steps)</summary>

6. `puts("you win!");` is what we want
7. For that we need the conditon `if (iVar1 == 0) ` to be true
8. `iVar1` is a variable that stores the result of a comparison
9. `strcmp(local_78,"your mum is very sexy");` strcmp is a function that compares the variable `local_78` with the string "your mum is very sexy" if they are equal the function will return a 0 
10. the variable `local_78` is the input
11. The password is `"your mum is very sexy"` 
9. Execute the program and enter `your mum is very sexy`

</details>