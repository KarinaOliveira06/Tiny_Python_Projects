def help_function():
    instructions = input("""
    To login at the system, you need to create a new account.
    To create a new account type 'register'.
    To get some usage instructions type 'instructions' or 'more help'
    """)

    if instructions in ["register", "regis", "r"]:
        employee = input("type your name: ")
        password = input("type your password: ")
        with open ("register.txt", "a", encoding = "UTF-8") as archive:
            archive.write(f"{employee},{password}" "\n")
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

    input("Press enter to continue.")

def register_function():
    p_name = input("Type the product name: ")
    p_price = input("type the product price: ")

    with open("products.txt", "a", encoding = "UTF-8") as archive:
        archive.write(f"{p_name},{p_price}" "\n")
        print("Well done, you've registered {product} for ${p_price}")
