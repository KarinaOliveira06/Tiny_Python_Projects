from functions import help_function
from functions import register_function
from functions import show_menu

while True:
    login_successful = False

    login = input("""
    Welcome to the World Games Store register system!

    If you are a new employee, type 'Help' to get instructions.
    If not, type 'Login' to log in to the registration system.
    If you want to exit, type 'Exit'.

    """).lower()

    if login in ["help", "hel", "he", "h"]:
        help_function()
    elif login in ["login", "log", "in", "log in", "l"]:
        name_login = input("Type your name: ")
        password_login = input("Type your password: ")

        with open("register.txt", "r") as archive:
            for line in archive:
                    line = line.strip()
                    data = line.split(",")
                    if name_login == data[0] and password_login == data[1]:
                        login_successful = True
                        print("login Successful!")
                        break

    if login_successful == True:
        break

while True:
        system_select = input("""
        === Game Store System ===
        
        (1) Register Product
        (2) Products Menu
        (3) Exit
        
        """).lower()

        if  system_select in ["1", "register", "register product", "registerproduct", "regis", "re", "um", "one"]:
            register_function()
        elif system_select in ["2", "dois", "two", "product", "products", "menu", "products menu"]:
            show_menu()
        elif system_select in ["3", "tres", "three", "exit", "ext", "sair"]:
            print("")