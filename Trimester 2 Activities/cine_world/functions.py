def movie_register(select_movie):
    with open("movies.txt", "a", encoding = "UTF-8") as archive:
            archive.write(f"{select_movie}\n")

def digital_poster():
    with open("movies.txt", "r", encoding = "UTF-8") as archive:
        data = archive.read()
        print(f"""
(-movies-)
{data}
""")
    return_menu = input("Press [ENTER] to return to the menu.")

def pos_system():

