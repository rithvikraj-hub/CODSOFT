# Tic-Tac-Toe AI

## Overview

This project implements an intelligent Tic-Tac-Toe game where a human player competes against an AI agent. The AI uses the Minimax Algorithm to evaluate all possible game states and select the optimal move, making it extremely difficult to beat.

The project demonstrates fundamental concepts of Artificial Intelligence, Game Theory, and Search Algorithms.

## Features

* Human vs AI gameplay
* AI powered by the Minimax Algorithm
* Unbeatable AI strategy
* Detects wins, losses, and draws
* Interactive command-line interface
* Simple and beginner-friendly implementation

## Technologies Used

* Python 3
* Minimax Algorithm
* Game Theory
* Recursive Functions

## Project Structure

```text
FUTURE_ML_02/
│
├── tic_tac_toe_ai.py
├── README.md
└── requirements.txt
```

## How It Works

1. The human player plays as **X**.
2. The AI plays as **O**.
3. The player enters the row and column positions for their move.
4. The AI evaluates all possible future game states using the Minimax Algorithm.
5. The AI selects the best possible move.
6. The game continues until a player wins or the match ends in a draw.

## Minimax Algorithm

The Minimax Algorithm is a decision-making algorithm used in two-player games. It recursively explores all possible game states and assigns scores based on the outcome.

* AI Win = +1
* Human Win = -1
* Draw = 0

The AI always chooses the move with the highest score, ensuring optimal gameplay.

## Sample Output

```text
Welcome to Tic-Tac-Toe!
You are X, AI is O

  |   |
---------
  |   |
---------
  |   |

Enter row (0-2): 1
Enter column (0-2): 1

O |   |
---------
  | X |
---------
  |   |
```

## Learning Outcomes

* Understanding Game Theory concepts
* Implementing the Minimax Algorithm
* Using recursion in Python
* Developing AI agents for games
* Designing interactive command-line applications

## Future Enhancements

* Add Alpha-Beta Pruning for optimization
* Create a graphical user interface using Tkinter or Pygame
* Add difficulty levels
* Support multiplayer mode
* Improve board visualization

## Requirements

This project uses only Python's standard library.

Example `requirements.txt`:

```text
# No external dependencies required
```

## How to Run

Run the following command in the terminal:

```bash
python tic_tac_toe_ai.py
```

## Conclusion

This project demonstrates how Artificial Intelligence can be applied to strategic games. By implementing the Minimax Algorithm, the AI can make optimal decisions and provide a challenging gameplay experience for users.
