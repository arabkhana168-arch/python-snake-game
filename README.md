# 🐍 Snake Game (Python + Turtle)

A classic Snake game built using Python's built-in `turtle` module — move around, eat food, grow longer, and avoid hitting the walls or your own tail!

## 🎮 Features
- Smooth snake movement with keyboard controls (Arrow keys)
- Randomly spawning food
- Live scoreboard
- Wall collision & self-collision detection with "Game Over" screen

## 🕹️ Controls
| Key | Action |
|-----|--------|
| ↑   | Move Up |
| ↓   | Move Down |
| ←   | Move Left |
| →   | Move Right |

## 📁 Project Structure
```
snake-game/
├── main.py         # Game loop and setup
├── snake.py         # Snake class (movement, growth, direction)
├── food.py           # Food class (random spawning)
├── score_board.py  # Score tracking and game over display
└── README.md
```

## 🚀 How to Run
```bash
python main.py
```

Requires Python 3 (the `turtle` module is included in the standard library, no extra installs needed).

## 🛠️ Built With
- Python 3
- `turtle` module

## 📌 To Do / Possible Improvements
- Add speed increase as score grows
- Add a "Play Again" option after game over
- Add sound effects
