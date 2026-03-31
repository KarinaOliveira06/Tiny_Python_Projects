def retry():
    retry = input("If you wanna play again type 'continue' or 'quit' to close the game: ")
    return retry in ["continue", "yes", "y", "play"]