login = input("""
Welcome to the World Games Store register system!

If you are a new employee, type 'Help' to get instructions.
If not, type 'Enter' to log in to the registration system.
""").lower()

while True:
    try:
        if login in ["help", "hel", "he", "h"]:

    except ValueError:
        print("Something went wrong, value error.")