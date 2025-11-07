---
title: "Modular Arithmetics — CryptoHack Writeup"
author: "your_nick"
date: 2025-11-02
platform: "CryptoHack"
category: "Category (Modular Arithmetics)"
difficulty: "easy"
points: 50

---

# Summary

This writeup documents the full solutions to **Modular Arithmetics** course on CryptoHack with a .py file for some exercices

**Goal:** Solve a series of mathematical problems

---

# Problem Statement

> The problems are a sequence of small exercises designed to teach and test basic modular arithmetic and the (extended) Euclidean algorithm.


---

# Tools & Environment

- **Language:** Python 3.9+  
- **Libraries:** Libraries: None required for the core math (built-in pow and % suffice). Optionally gmpy2 or sympy for very large involved tasks.
- **CLI utilities:** none necessary 
- **Optional:** SageMath for symbolic math

Run environment example:
```bash
python --version   # Python 3.9+
pip install pycryptodome gmpy2 sympy
```

---

# Theory

![alt text](image.png)

---

![alt text](image-1.png)

---

![alt text](image-2.png)

---

![alt text](image-3.png)
![alt text](image-5.png)

**Therefore the result is`` 1 ``**

---

![alt text](image-4.png)

**Therefore the result is`` 9 ``**

## 6.  
- Modulo p = 29
- ints = [14,6,11]

![alt text](image-6.png) <br>
 We have to check if :<br>
 ![alt text](image-7.png)<br>
 But we never get 14 so 14 is non-residue<br>
 For X= 11 we never get 11 so 11 is non-residue<br>
 For x= 6 we get 6 so 6 is the only quadratic residue<br>