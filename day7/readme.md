# Hangman Game 🎯

## 📌 Description
This is a **console-based Hangman game** written in Python.
The game uses a **hard-mode rule**, where only **one occurrence of a letter**
is revealed per correct guess.

If a letter is guessed again after all its positions are already revealed,
the player **loses a chance**.

---

## 🛠 Concepts Used
- Python loops
- Conditional statements
- Lists and strings
- Index-based updates using `enumerate`
- Random word generation

---

## 🎮 Game Rules
- A random word of length **4–7** is generated.
- The player guesses **one letter at a time**.
- Only **one matching letter** is revealed per correct guess.
- Repeating a fully revealed letter costs **one chance**.
- Invalid inputs do **not** cost chances.
- The game ends when:
  - All letters are guessed (Win), or
  - Chances run out (Lose).

---

## ▶ How to Run
```bash
python hangman_game.py
