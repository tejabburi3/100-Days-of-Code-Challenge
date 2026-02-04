# Mail Merge Letter Generator ✉️

## 📌 Description
This project is a Python-based Mail Merge Letter Generator.  
It reads a list of names from a text file and creates personalized letters by replacing a placeholder word inside a template file. Each person receives their own generated letter automatically.

---

## 🛠 Concepts Used
- Python File Handling
- Reading & Writing Files
- String Replacement (`replace`)
- Loops
- Context Managers (`with open`)

---

## 📂 Project Structure
Day25/
- my_text.txt        → List of names
- matter.txt         → Template letter
- mail_merge.py      → Main program
- letter_for_*.txt   → Generated letters

---

## ▶ How It Works
1. The program reads names from **my_text.txt**.
2. It reads the template from **matter.txt**.
3. The word `name` inside the template is replaced with each person's name.
4. A new letter file is generated for every person automatically.

---

## 🧪 Example

Template (matter.txt):
Hello name,
Welcome to our event!

Names (my_text.txt):
Ravi
Akhil

Generated Output:
letter_for_Ravi.txt
letter_for_Akhil.txt

---

## ▶ How to Run
python mail_merge.py

---

## 🎯 Learning Outcome
- Learned file automation using Python
- Practiced reading and writing multiple files
- Understood dynamic content generation

---

## 🚀 Part of
100 Days of Code Challenge — Day 25
