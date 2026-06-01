import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "database.txt")

def retry_function():
    try:
        retry = input("If you wanna play again type 'continue' or 'quit' to close the game: ")
        if retry in ["continue", "yes", "y", "play"]:
            return True          
        else: exit()
    except ValueError:
        print("Something went wrong, please try again.")

def guess_function(guess, sort_number):
        if guess == sort_number:
            print("Player Wins!")
            return True
        elif guess > sort_number:
            print("Try lower...")
        else: print("Try higher...")
        return False

        
def gameover_function(coins):
    """Checks if the player has enough coins to play. Returns Boolean."""
        if coins <= 0:
            print("Game Over, you are broke!")
            return False
        return True

def load_coins ():
    """Reads the coin balance from database.txt. Returns 100 if file not found."""
    try:
        with open(DB_PATH, "r") as archive:
            return int(archive.read())
    except:
         return 100

def save_coins(value):
    """Writes the current coin balance to the local database.txt file."""
     with open(DB_PATH, "w") as archive:
          archive.write(str(value))

     
