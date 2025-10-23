# 🚀 ByteClassic_crack — Crackme.one

![level](https://img.shields.io/badge/level-Easy-brightgreen) ![platform](https://img.shields.io/badge/platform-Windows-blue) ![arch](https://img.shields.io/badge/arch-x86__64-orange) ![lang](https://img.shields.io/badge/lang-C%2FC%2B%2B-lightgrey) ![tool](https://img.shields.io/badge/tool-Ghidra-orange)

- **Author:** ByteClassic  
- **Uploaded:** 03:40 PM 06/16/2025  
- **Difficulty:** 1.0  
- **Quality:** 2.9  
- **File:** `ByByteClassic`  
- **Size:** `1881KB`

---

## 🔎 Description
- A simple Windows x86-64 CrackMe written in C/C++.    
- Goal: discover the password that makes the program print the success message, or patch the binary to force the success path.

---

## ⚙️ Prerequisites
- Windows VM (recommended) or Wine to run the executable safely.  
- Tools: Ghidra (CodeBrowser / Decompiler) for static analysis and x64dbg for dynamic debugging.   


---

## ▶️ Start
1. Open the executable with ghidra (more info go to the Ghidra.md file)
2. Filter in the Symbol Tree for a "main" function
3. In the Decompile window you can see the main function in C
4. Analise the main function code ,solution underneath 




---

## 📜 code

```c
  __main();
  std::string::string(local_28);
  std::allocator<char>::allocator();
  std::string::string(local_38,"secret123");
  std::allocator<char>::~allocator();
  std::operator<<(&std::cout,"Enter password: ");
  std::getline<>(&std::cin,local_28);
  uVar1 = std::operator==(local_28,local_38);
  if ((char)uVar1 == '\0') {
    plVar2 = std::operator<<(&std::cout,"Incorrect password!");
    std::ostream::operator<<(plVar2,std::endl<>);
  }
  else {
    plVar2 = std::operator<<(&std::cout,"Correct password!");
    std::ostream::operator<<(plVar2,std::endl<>);
  }
```
<details>
  <summary>Solution (steps)</summary>

5. We want this `"Correct password!"` 
6. `std::string::string(local_28);` Constructs a std::string object (named local_28 in the decompilation). In real C++ this is `std::string input;`
7. `std::allocator<char>::allocator()` Another decompiler artifact showing allocator construction for `std::string`. (NOT IMPORTANT)

8. `std::string::string(local_38,"secret123");`Constructs a second `std::string` named `local_38` initialized to the literal `"secret123"`. 

9. `std::allocator<char>::~allocator();`Destructor call for the temporary allocator — another artifact, not important for behavior.

10. `std::operator<<(&std::cout,"Enter password: ");`Prints the prompt: `Enter password: ` (equivalent to `std::cout << "Enter password: ";`).

11. `std::getline<>(&std::cin,local_28);`Reads a full line from standard input into `local_28` (equivalent to `std::getline(std::cin, input);`). This reads everything up to the newline (spaces included).

12. `uVar1 = std::operator==(local_28,local_38);` Compares the two strings: `input == secret`. The result (true/false) is stored in `uVar1` (a boolean-like value).

13. `if ((char)uVar1 == '\0') { ... }` The decompiler shows the test as comparing `(char)uVar1` with `'\0'`. That means: if the comparison returned **false** (i.e., strings are **not equal**), enter the `if` block.

14. The password is `secret123` 
15. Execute the program and enter `secret123`
</details>