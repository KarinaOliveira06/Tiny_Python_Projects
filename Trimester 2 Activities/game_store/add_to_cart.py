from cart import cart
from main import game_sale

def add_to_cart(game_sale, cart_value):
    if game_sale in ["Minecraft", "Mine", "Mini", "Minecreft", "Minicreft"]:
        cart_value += 80
        print(f"{cart}")
        print(f"Total: {cart_value}")
        return True
    elif game_sale in ["GTA V", "GTA", "GT", "V"]:
        cart_value += 120
        print(f"{cart}")
        print(f"Total: {cart_value}")
        return True
    elif game_sale in ["FIFA", "FIF", "FI"]:
        cart_value += 90
        print(f"{cart}")
        print(f"Total: {cart_value}")
        return True
    else:
        print("Invalid product, please try again.")
        return False

