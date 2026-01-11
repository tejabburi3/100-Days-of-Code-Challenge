# Silent Auction with Re-Bidding 🏷️

## 📌 Description
This project is a **command-line Silent Auction system** built using Python.
It allows multiple users to place bids anonymously and determines the winner
based on the highest bid.

If two or more bidders place the **same highest bid**, the system automatically
starts a **re-bidding round only for the tied candidates** until a single
winner is determined.

---

## 🛠 Concepts Used
- Python dictionaries
- While loops
- Conditional statements
- List comprehensions
- User input handling
- Real-world auction logic

---

## 🔄 How the Auction Works
1. Users enter their names and bid amounts.
2. All bids are stored securely.
3. The highest bid is identified.
4. If there is:
   - ✅ One highest bidder → winner is declared.
   - ⚠️ Multiple highest bidders → only those bidders are asked to rebid.
5. Re-bidding continues until a single winner emerges.

---

## ▶ Program Flow
- Initial bidding phase
- Tie detection
- Re-bidding phase (only tied bidders)
- Winner declaration

---

## 🧪 Example Scenario

### Initial Bids
-Ravi → 500
-Akhil → 500
-Teja → 300

### Re-Bidding Round
-Ravi → 650
-Akhil → 700

### Result
🏆 Akhil wins the auction with 700
