def clean_line():
    with open("movies.txt", "r", encoding = "UTF-8") as archive:
        movie_list = []
        for line in archive:
            data = line.split(",")
            line = line.strip()

            if len(data) == 2:
                movie_list.append(data)
            return movie_list

def movie_register(select_movie, select_price):
    with open("movies.txt", "a", encoding = "UTF-8") as archive:
            archive.write(f"{select_movie},{select_price}\n")

def digital_poster():
    print("---Movies---")
    all_movies = clean_line()
    for data in all_movies:
            print(f"""
    {data[0].title()} - ${data[1]}
            """)
    return_menu = input("Press [ENTER] to return to the menu.")

def pos_system(buy_ticket, cart, total_value):
    if buy_ticket in ["ticket", "tickets", "cricket", "tick", "t"]:
        selected_movie = input("Type the movie name: ").lower()
        ticket_amount = int(input("Tickets amount: "))
        all_movies = clean_line()

        for data in all_movies:
            if selected_movie == data[0]:
                ticket_price = int(data[1])
                total_value = ticket_price * ticket_amount

                print(f"""
(--- cart ---)

{data[0]} - ${total_value}

                """)
                break
            else:
                print("Invalid value, please try again.")

