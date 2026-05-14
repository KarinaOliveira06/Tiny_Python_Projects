from cart import cart

cart_value = 0

print("Welcome to World Games Store!" "\n")
print("We have a lot of games on sale, and a promotion!")
print("If you spend $200, you will receive 10% off!!!""\n")

while True:
    try:
        game_sale = input("Games on sale:""\n"
        "Minecraft $80""\n"
        "GTA V $100""\n"
        "FIFA $90""\n"
        "Type a game to add to cart or 'finish' to finish: ").lower()
        print("")

        if game_sale in ["finish", "fini", "fi", "f", "fish"]:
            break
        elif add_to_cart():
            print("Item added!")
        else:
            print("Type a valid product.")

    except ValueError:
        print("Something went wrong.")

