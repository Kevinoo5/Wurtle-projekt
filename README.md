## Wurtle Word Game

## Description:
Wurtle is a simple word guessing game where the player tries to guess a hidden word of a specific length by entering words of the same length. The game interface is built using the Tkinter library in Python. The game randomly selects a word from a database and provides feedback to the player based on their guesses.

## Features:
- Allows the player to choose the length of the hidden word (5, 6, or 7 letters).
- Provides feedback on the correctness of the guessed word:
  - Shows which letters are correctly guessed and in the correct position.
  - Indicates letters that are correct but in the wrong position.
  - Alerts the player if the guessed word is not in the allowed list.
- Informs the player when they successfully guess the hidden word or run out of attempts.

## How to Play:
1. Launch the game.
2. Choose the desired word length (5, 6, or 7 letters).
3. Enter a word of the selected length into the text box provided.
4. Click the "Enter" button to submit your guess.
5. Receive feedback on your guess and continue guessing until you find the hidden word or run out of attempts.
6. If you guess the word correctly, a congratulatory message will appear.
7. Close the game window when finished.

## Requirements:
- Python 3.x
- Tkinter library
- SQLite3 library

## Instructions for Running the Game:
1. Ensure you have Python installed on your system.
2. Install the required libraries using `pip install tkinter` and `pip install sqlite3`.
3. Save the provided code in a Python file (e.g., `wurtle_game.py`).
4. Run the Python file using a Python interpreter.
5. The game window should appear, allowing you to play the game as described above.
