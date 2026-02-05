# Coffee Machine Simulator ☕

## Description
This is a Python-based Coffee Machine program that simulates a real vending machine.
Users can choose a drink, insert coins, and receive coffee if enough ingredients
and money are provided. The machine tracks resources and total profit.

## Features
- Menu-driven coffee selection
- Supports expresso, latte, and cappuccino
- Coin-based payment system (₹1, ₹2, ₹5, ₹10)
- Automatic change calculation
- Resource availability check
- Profit tracking
- Machine report option
- Turn off machine using `off`

## Menu Commands
expresso → Order expresso  
latte → Order latte  
cappuccino → Order cappuccino  
report → Show ingredients and profit  
off → Stop the machine  

## How It Works
1. The user selects a drink from the menu.
2. The machine checks if enough ingredients are available.
3. The user inserts coins.
4. If payment is sufficient, the drink is prepared and change is returned.
5. Profit and ingredient storage are updated automatically.

## Concepts Used
- Python dictionaries
- Functions
- While loops
- Conditional logic
- Global variables
- Basic payment simulation

## Example
Menu: expresso / latte / cappuccino / report / off  
What do you want: latte  
☕ Here is your latte.

