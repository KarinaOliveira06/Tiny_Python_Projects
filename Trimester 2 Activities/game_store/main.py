from add_to_cart import add_to_cart

cart_value = 0
shopping_cart = [] 

print("Welcome to World Games Store!\n")
print("We have a lot of games on sale, and a promotion!")
print("If you spend $200, you will receive 10% off!!!\n")

while True:
    try:
        game_sale = input("Games on sale:\n"
        "Minecraft $80\n"
        "GTA V $100\n"
        "FIFA $90\n"
        "Type a game to add to cart or 'finish' to finish: ").lower()
        print("")

        if game_sale in ["finish", "fini", "fi", "f", "fish"]:
            print("\n--- Final Receipt ---")
            
            if cart_value >= 200:
                discount = cart_value * 0.10
                final_total = cart_value - discount
                
                print(f"Subtotal: ${cart_value:.2f}")
                print(f"Discount (10%): -${discount:.2f}")
                print(f"Total to pay: ${final_total:.2f}")
            else:
                print(f"Total to pay: ${cart_value:.2f}")
                
            print("Thank you for shopping at World Games Store!")
            break
        
        new_value = add_to_cart(game_sale, cart_value, shopping_cart)
        
        if new_value is not False:
            cart_value = new_value 
            print("Item added!\n")

    except ValueError:
        print("Something went wrong.")