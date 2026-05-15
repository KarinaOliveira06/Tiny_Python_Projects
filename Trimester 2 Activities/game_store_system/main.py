from functions import help

login = input("""
Welcome to the World Games Store register system!

If you are a new employee, type 'Help' to get instructions.
If not, type 'Login' to log in to the registration system.
If you want to exit, type 'Exit'.

""").lower()

while True:
    try:
        if login in ["help", "hel", "he", "h"]:
            help()
        elif login in ["login", "log", "in", "log in", "l"]:
            name_login = input("Type your name: ")
            password_login = input("Type your password: ")

    except ValueError:
        print("Something went wrong, value error.")