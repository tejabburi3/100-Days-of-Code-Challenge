# ☕ Coffee Machine Console App (Python(OOPS))

A simple **Python coffee machine simulation** that allows users to order drinks, check remaining ingredients, and track daily profit.
This project demonstrates modular programming using multiple Python files.

---

## 📌 Features

* ☕ Order **Cappuccino**, **Latte**, or **Espresso**
* 💰 Coin-based payment system (₹1, ₹2, ₹5, ₹10)
* 📊 View current ingredient **report**
* 📈 Track **total profit**
* 🧾 Automatic ingredient deduction after each order
* ❌ Handles insufficient stock or payment

---

## 🗂️ Project Structure

```
coffee-machine/
│
├── main.py               # Main program loop
├── coffee_items.py       # Menu & ingredient storage logic
├── coffee_pricecheck.py  # Payment system & profit tracking
└── README.md
```

---

## ⚙️ How It Works

### 1️⃣ `main.py`

Controls user interaction:

* Shows menu
* Accepts user input
* Calls ingredient checker
* Calls payment system

---

### 2️⃣ `coffee_items.py`

Contains:

* Ingredient storage
* Menu dictionary
* `Coffee()` function to check stock and deduct ingredients

---

### 3️⃣ `coffee_pricecheck.py`

Handles:

* Coin input
* Payment validation
* Profit calculation

---

## ▶️ How to Run

Make sure Python is installed.

```bash
python main.py
```

---

## 🧪 Example Usage

```
Here is today our menu
1.Cappuccino
2.Latte
3.Espresso

What do you want : Latte
How many 10₹ coins : 10
Here is your Change 💵12
Here is your ☕️ Latte
```

---

## 🛠️ Commands

| Command                       | Description                |
| ----------------------------- | -------------------------- |
| Cappuccino / Latte / Espresso | Order coffee               |
| Report                        | Show remaining ingredients |
| Profit                        | Show total earnings        |
| Off                           | Exit program               |

---

## 🎯 Learning Objectives

This project demonstrates:

* Python modules & imports
* Functions and dictionaries
* Control flow
* Basic project structure
* CLI-based application design

---

## 🚀 Future Improvements

* Convert to OOP (CoffeeMachine class)
* Add GUI using Tkinter
* Save profit & stock to file
* Add more drinks dynamically

---

## 👨‍💻 Author

Created as a Python practice project for learning modular programming and real-world logic building.

---
