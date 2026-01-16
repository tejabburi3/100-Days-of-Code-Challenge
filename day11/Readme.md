# ♠️ Black Jack Game (Python)

A simple console-based Black Jack game built using Python.  
This project was created as part of **Day 11 practice**, focusing on loops, conditions, and game logic.

---

## 🎮 Game Rules (Custom Version)

- Cards have values between **1 and 11**
- Each player starts with **2 cards**
- The user can choose to **draw cards (`yes`) or stop (`no`)**
- The user is **NOT forced to stop at 21**
- If user score exceeds **21**, the user busts
- Computer draws cards until its score is between **18 and 21**
- Final scores decide the winner

---

## 🧠 Game Logic Summary

### User
- Can draw as many cards as desired
- Busts if score > 21
- Score = 21 is allowed (user decides when to stop)

### Computer
- Draws cards while score < 18
- Holds cards when score is between 18 and 21
- Busts if score > 21

---

## 🏆 Winning Conditions

- User busts → ❌ User loses
- Computer busts → 🎉 User wins
- User score > computer score → 🎉 User wins
- Scores equal → 🤝 Draw
- Otherwise → 😎 Computer wins

---

## 🔁 Play Again Feature

After each round, the user is asked:
