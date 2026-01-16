# ♠️ Black Jack Game (Python)

A console-based Black Jack game built using Python.  
This project was developed as part of **Day 11 learning**, focusing on control flow, functions, and state management.

---

## 🎮 Game Overview

This is a **custom implementation of Black Jack**, created for learning purposes.  
It does not follow all casino rules but is logically consistent and intentionally designed.

---

## 🧩 Game Rules

### Player (User)
- Starts with **2 cards**
- Can choose to **draw (`yes`) or stop (`no`)**
- Is **not forced to stop at 21**
- Busts if score **exceeds 21**

### Computer
- Starts with **2 cards**
- Draws cards **only until it decides to hold**
- Automatically holds when score is between **18 and 21**
- Busts if score **exceeds 21**
- Once holding, **never draws again**

---

## 🧠 Core Logic

- Card values range from **1 to 11**
- Computer behavior is controlled using a **state flag**
- Computer decisions are evaluated using a function that returns:
  - `"draw"` → can continue drawing
  - `"hold"` → stop drawing
  - `"bust"` → round ends
- Game continues until:
  - User busts
  - Computer busts
  - User chooses to stop

---

## 🏆 Winning Conditions

- User busts → ❌ User loses
- Computer busts → 🎉 User wins
- Both bust → ❌ Both lose
- User score > computer score → 🎉 User wins
- Scores equal → 🤝 Draw
- Otherwise → 😎 Computer wins

---

## 🔁 Play Again Feature

After each round, the user is asked:

