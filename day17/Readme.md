# A–Z Programming Word Generator 🔤

This is a Python program that generates **random programming-related words**
based on the letters entered by the user. The program reads data from a CSV file
and prints one random programming term for each alphabet letter provided.

---

## Description
The user enters any word or combination of letters.  
For every valid alphabet letter:
- The program searches the CSV file for matching programming terms.
- One random word is selected and displayed.
- Non-alphabet characters are ignored automatically.

---

## Features
- Uses Pandas to read CSV data
- Random programming word selection
- Supports multiple letters or words as input
- Ignores numbers, spaces, and symbols
- Clean formatted output

---

## How It Works
1. The CSV file contains letters (A–Z) and programming words.
2. User input is converted to uppercase.
3. Each letter is checked:
   - If it is not a letter → skipped.
   - If it exists in the dataset → one random word is printed.

---

## Example
### Input
Enter a word or words: code123
### Output
---
C : Compiler
O : Object
D : Debugger
E : Encapsulation
(Output may change because words are chosen randomly.)

---

## Files Used
- `a_to_z_words_programming_common.csv` – Programming words dataset
- `word_generator.py` – Main Python script

---

## Concepts Used
- Pandas DataFrame filtering
- CSV file handling
- Random module
- Loops and conditionals
- String processing

---

## Learning Outcome
Through this project, I learned how to:
- Work with structured CSV data
- Filter rows using Pandas
- Handle user input safely
- Build small data-driven programs

---


