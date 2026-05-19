def help_function():
    instructions = input("""
    To login at the system, you need to create a new account;
    To create a new account type 'register';
    To get some usage instructions type 'instructions' or 'more help';
    To exit, type 'Exit'.
    """).lower()

    if instructions in ["register", "regis", "r"]:
        employee = input("type your name: ").lower()
        password = input("type your password: ").lower()
        with open ("register.txt", "a", encoding="UTF-8") as archive:
            archive.write(f"{employee},{password}\n")
        print(f"Congratulations {employee}! You registered your account, now try log in.")

    elif instructions in ["instructions", "i", "ins", "more help", "help", "more", "morehelp"]:
        input("""
        After create an account, you need to login at first page;
        When you are logged in, you can register a product selecting 'register product' (1) option;
        You can see your products menu typing number 2;
        To apply a discount, simply type the name of a product from the menu;
        You can see the total value and total products typing 'total' at the menu.
        """)
    elif instructions in ["3", "tres", "three", "exit", "ext", "sair"]:
        return
    else:
        print("Something went wrong, please try again.")

    input("Press enter to continue.")

def register_function():
    p_name = input("Type the product name: ")
    p_price = input("type the product price: ")

    with open("products.txt", "a", encoding="UTF-8") as archive:
        archive.write(f"{p_name},{p_price}\n")
    print(f"Well done, you've registered {p_name} for ${p_price}")

def show_menu(cart):
    with open ("products.txt", "r", encoding="UTF-8") as archive:
        for line in archive:
            line = line.strip()
            data = line.split(",")
        
            if len(data) >= 2:
                p_name = data[0]
                p_price = data[1]

                print(f"""
                Product: {p_name}
                Price: {p_price}
                """)

    while True:
        c_product = input("\nType the product name to add to the cart or type 'exit' to exit: ").strip().lower()

        if c_product in ["3", "tres", "three", "exit", "ext", "sair"]:
            return

        product_found = False

        with open("products.txt", "r", encoding="UTF-8") as archive:
            for line in archive:
                line = line.strip()
                data = line.split(",")
            
                if len(data) >= 2:
                    p_name = data[0]
                    p_price = data[1]

                    if c_product == p_name.lower():
                        cart.append(data)
                        print(f"\n>> {p_name} added to your cart.")
                        product_found = True
                        break

        if product_found == False:
            print("Product not found. Please try again.")
            continue

        while True:
            next_step = input("Do you want to add another product (yes) or finish purchase (finish)? ").strip().lower()
            
            if next_step in ["yes", "y", "sim", "s"]:
                break 
                
            elif next_step in ["finish", "f", "finalizar", "total"]:
                total_price = 0.0
                print("\n=== RECEIPT ===")
                for item in cart:
                    print(f"- {item[0]}: ${item[1].strip()}")
                    clean_price = item[1].replace("$", "").strip()
                    total_price += float(clean_price)
                
                # --- Lógica de Desconto de 3% Acima de 400 ---
                if total_price > 400.0:
                    discount = total_price * 0.03
                    final_price = total_price - discount
                    print(f"\nSubtotal: ${total_price:.2f}")
                    print(f"Discount (3%): -${discount:.2f}")
                    print(f"Total to pay: ${final_price:.2f}")
                else:
                    print(f"\nTotal to pay: ${total_price:.2f}")
                # ----------------------------------------------

                print("===============\n")
                
                cart.clear()
                return 
                
            else:
                print("Invalid option. Type 'yes' or 'finish'.")