# Day 03 – Password Generator 🔐

## 📌 Description
This project is a **Python-based Password Generator** that creates a secure password based on user preferences.  
The user can decide:
- Total password length
- Number of special characters
- Number of digits  

The remaining characters are automatically filled with letters, and the final password is shuffled for randomness.

---

## 🛠 Concepts Used
- Python standard libraries (`random`, `string`)
- Lists and strings
- User input handling
- Conditional validation
- Random password generation
- Shuffling using `random.shuffle()`

---

## ▶ How It Works
1. User enters the total password length.
2. User specifies how many special characters and digits are required.
3. The program validates the input.
4. A password is generated using letters, digits, and symbols.
5. Characters are shuffled to ensure randomness.
6. The final secure password is displayed.

---

## ❌ Input Validation
If the sum of special characters and digits exceeds the total password length, the program displays an error message and stops execution.

---
