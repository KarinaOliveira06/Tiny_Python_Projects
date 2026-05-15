def help():
    instructions = input("""
    To login at the system, you need to create a new account.
    To create a new account type 'register'.
    To get some using instructions type 'instructions' or 'more help'
    """)

    try:

        if instructions in ["register", "regis", "r"]:
            employee = input("type your name: ")
            password = input("type your password: ")
            with open ("register.txt", "a", encoding = "UTF-8") as archive:
                archive.write(f"Name: {employee}," "\n"
                f"Password: {password}")
                print(f"Congratulations {employee}! You registered your account, now try log in.")

        elif instructions in ["instructions", "i", "ins", "more help", "help", "more", "morehelp"]:
            input("""
            After create an account, you need to login at first page;
            When you are logged in, you can register a product selecting 'register product' (1) option;
            You can see your products menu typing number 2;
            To apply a discount, simply type the name of a product from the menu;
            You can see the total value and total products typing 'total' at the menu.
            """)
        else:
            print("Something went wrong, please try again.")

    except ValueError:
        print("Type a valid value.")

    input("Press enter to continue.")
        