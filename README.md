# Snake Water Gun Game

Welcome to the **Snake Water Gun Game**! 🎮 This is a simple yet fun Python game where you can compete against the computer by choosing between "Snake", "Water", or "Gun". Built using `tkinter` for the graphical user interface and `pygame` for sound effects, this game is a great example of a classic game with a modern touch.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Game Rules](#game-rules)
- [Screenshots](#screenshots)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

The **Snake Water Gun Game** is a graphical application where players choose one of three options to play against the computer. The game follows the classic rules where each choice can win against, lose to, or draw with another choice. The project showcases the use of Python for creating games with interactive UI elements and sound effects.

## Features

- **Graphical User Interface:** A clean and interactive interface built with `tkinter`.
- **Sound Effects:** Engaging sounds for actions like button clicks, winning, losing, and drawing, using the `pygame` mixer.
- **Game Logic:** Implemented rules for the classic game where:
  - **Snake** beats **Water**
  - **Water** beats **Gun**
  - **Gun** beats **Snake**
- **Custom Font:** A unique signature font for the developer’s credit.

## Installation

To get started with the **Snake Water Gun Game**, you will need Python 3.x installed on your system. Additionally, you need to install the `pygame` and `Pillow` libraries. 

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/bibhu2727/Snake-Water-Gun-Game.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd Snake-Water-Gun-Game
    ```

3. **Install the Required Libraries:**

    You can install the necessary libraries using pip:

    ```bash
    pip install pygame pillow
    ```

## How to Run

After setting up your environment, you can run the game with the following command:

```bash
python main.py

# Snake Water Gun Game

Ensure that you have the following files in the same directory as `main.py`:

- `click.wav`: Sound effect for button clicks.
- `win.wav`: Sound effect for winning.
- `lose.wav`: Sound effect for losing.
- `draw.wav`: Sound effect for a draw.
- `snake.png`: Image representing "Snake".
- `water.png`: Image representing "Water".
- `gun.png`: Image representing "Gun".

## Game Rules

In the game, you and the computer will choose one of three options:

- Snake beats Water.
- Water beats Gun.
- Gun beats Snake.

The outcome of the game is determined based on these rules, and the result is displayed along with an appropriate sound effect.

## Screenshots

Here’s what the game looks like:

![Game Screenshot](https://raw.githubusercontent.com/bibhu2727/Snake-Water-Gun-Game/main/screenshot.png)


## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- `tkinter` for the graphical user interface components.
- `pygame` for the sound effects.
- `Pillow` for image handling.
