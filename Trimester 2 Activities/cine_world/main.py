from functions import digital_poster, pos_system, movie_register, box_office
cart = []

print("""
Welcome to the Cine World System!
""")
while True:
    system_select = input("""
    --- Options ---
    (1) Movie register
    (2) Digital poster
    (3) POS System
    (4) Box office
    (5) Exit
    """).lower()

    if system_select in ["1", "movie", "movie register", "register", "reg", "regigigas"]:
        select_movie = input("Type the movie name: ").lower()
        select_price = input("Type the price: ").lower()
        movie_register(select_movie, select_price)
        print(f"Congratulations, you've registered {select_movie}!")
    elif system_select in ["2", "digital", "poster", "post"]:
        digital_poster()
    elif system_select in ["3", "pos", "pos system", "system", "sys", "ops", "pos sys", "possystem", "posys"]:
        buy_ticket = input("Hello, type 'ticket' to buy tickets: ").lower()
        pos_system(buy_ticket, cart) 
        print(f"\nCongratulations, you got a ticket!")
    elif system_select in ["4", "four", "quatro", "box", "box office", "boxoffice", "box_office"]:
        box_office(cart)
    elif system_select in ["exit", "ex", "sair", "quit", "5", "cinco", "five"]:
        break
    else:
        print("Value error, please try again.")