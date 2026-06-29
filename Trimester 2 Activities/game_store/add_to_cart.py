from cart import print_cart_matrix

def add_to_cart(game_sale, cart_value, shopping_cart):
    if game_sale in ["minecraft", "mine", "mini", "minecreft", "minicreft"]:
        cart_value += 80
        shopping_cart.append(["Minecraft"]) 
        print_cart_matrix(shopping_cart)
        print(f"Total: ${cart_value}")
        return cart_value
        
    elif game_sale in ["gta v", "gta", "gt", "v"]:
        cart_value += 120
        shopping_cart.append(["GTA V"])
        print_cart_matrix(shopping_cart)
        print(f"Total: ${cart_value}")
        return cart_value

    elif game_sale in ["fifa", "fif", "fi"]:
        cart_value += 90
        shopping_cart.append(["FIFA"])
        print_cart_matrix(shopping_cart)
        print(f"Total: ${cart_value}")
        return cart_value

    else:
        print("Invalid product, please try again.\n")
        return False