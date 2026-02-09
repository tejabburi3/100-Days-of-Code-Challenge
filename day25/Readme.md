# U.S. States Guessing Game 🗺️

This is an interactive Python game where the player guesses the names of all 50 U.S. states. A blank map of the United States is displayed using the Turtle module, and each correct guess appears on the map at the correct location. The game continues until all states are guessed or the user chooses to exit.

## How the Game Works
- A blank U.S. map is shown on the screen.
- The user types the name of a U.S. state.
- If the guess is correct, the state name is written on the map.
- The title bar shows how many states have been guessed.
- If the user types **Exit**, the game ends and saves all unguessed states to a CSV file.

## Features
- Interactive graphical interface using Turtle
- Uses Pandas to read and process CSV data
- Displays state names at accurate coordinates
- Tracks guessed and missed states
- Automatically generates a CSV file of missed states

## Files Used
- `blank_states_img.gif` – Image of the U.S. map
- `50_states.csv` – State names with x and y coordinates
- `States_Missed.csv` – Generated file of unguessed states
- `us_states_game.py` – Main game file

## Concepts Used
- Turtle graphics
- Pandas DataFrames
- CSV file handling
- Lists and list comprehensions
- Loops and conditional statements
- User input handling

## Example
5/50 States Correct
What's another state's name? California

Typing `Exit` will end the game and save the remaining states.
