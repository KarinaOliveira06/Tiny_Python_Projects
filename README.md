# Tiny Python Projects 🐍
A collection of practical Python logic exercises and mini-games focused on clean code, modularization, and data persistence.

## 🕹️ Project: Common Guessing Game
A terminal-based guessing game with multiple difficulty levels and a persistent save system.

### ✨ Features
- **3 Difficulty Levels:** Easy, Normal, and Insane (with different retry counts and rewards).
- **Data Persistence:** Saves your coin balance in a `database.txt` file using Python's File I/O.
- **Robust Error Handling:** Validates user inputs to prevent crashes (Try/Except blocks).
- **Modular Architecture:** Logic separated into a dedicated `functions.py` file for better maintenance.
- **Path Management:** Uses `os.path` to ensure the database is always created in the correct folder.

### 🛠️ Technologies
- Python 3.x
- `os` module (Path handling)
- `random` module (Game logic)

### 🚀 How to run
1. Clone the repository.
2. Run `main.py`.
3. Your progress will be automatically saved in `database.txt`.
