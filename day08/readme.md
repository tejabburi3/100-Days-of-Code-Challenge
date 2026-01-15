# Caesar Cipher 🔐

## 📌 Description
This project implements a **Caesar Cipher** using Python.  
It allows users to **encrypt or decrypt text** by shifting letters forward or backward by a given number.

Both **uppercase and lowercase letters** are handled correctly, while **non-alphabet characters** (spaces, symbols, numbers) remain unchanged.

---

## 🛠 Concepts Used
- Python functions
- String manipulation
- Lists
- Conditional statements
- Modular arithmetic (`%`)
- ASCII alphabets (`string.ascii_uppercase`, `string.ascii_lowercase`)

---

## 🔄 How It Works
- Each letter is converted to its index in the alphabet.
- The index is shifted by the given number.
- Modulo `26` is used to wrap around the alphabet.
- Uppercase and lowercase letters are preserved.

---

## ▶ Program Flow
1. User enters the text.
2. User chooses:
   - `e` → Encryption
   - `d` → Decryption
3. User enters a shift number.
4. The program outputs the encrypted or decrypted text.

---

## 🧪 Example

### Input

Text: Hello World
Choice: e
Shift: 3


### Output
Encrypted text: Khoor Zruog
