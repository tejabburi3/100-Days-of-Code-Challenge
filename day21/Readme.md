🐍 Snake Game – Python (Turtle Graphics)

A classic Snake Game built using Python and Turtle graphics.
The player controls a snake to eat food, increase the score, and avoid collisions with walls and itself.

This project demonstrates object-oriented programming, event handling, and basic game development concepts in Python.

🚀 Demo

Run the game locally to play.
(Screenshots or GIFs can be added here later)

✨ Features

Arrow-key controlled snake movement

Random food generation

Snake growth after eating food

Live score display

Game over detection:

Wall collision

Self-collision

🛠️ Tech Stack

Language: Python 3

Graphics: Turtle module

Concepts: OOP, game loop, collision detection

📁 Project Structure
snake-game/
│
├── main.py           # Main game loop
├── snake_main.py     # Snake movement and controls
├── food.py           # Food logic
├── scoreboard.py     # Score display and game over message
├── README.md         # Documentation

▶️ Getting Started
Prerequisites

Python 3.x installed

Verify installation:

python --version

Installation & Run

Clone the repository:

git clone https://github.com/your-username/snake-game.git


Navigate to the project folder:

cd snake-game


Run the game:

python main.py

🎮 Controls
Key	Action
⬆️ Up Arrow	Move Up
⬇️ Down Arrow	Move Down
⬅️ Left Arrow	Move Left
➡️ Right Arrow	Move Right
🧠 How It Works

The snake moves continuously using a timer-based loop

Food appears at random positions

When the snake eats food:

Score increases

Snake length increases

Game ends if:

Snake hits the wall

Snake touches itself

❌ Game Over

When the game ends, “GAME OVER” is displayed at the center of the screen, and movement stops.
