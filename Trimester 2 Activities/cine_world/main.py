from functions import movie_register
from functions import digital_poster

print("""
Welcome to the Cine World System!
""")

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
    movie_register(select_movie)
    print(f"Congratulations, you've registered {select_movie}!")
elif system_select in ["2", "digital" "poster", "digital", "poster", "post"]:
    digital_poster()
elif system_select in ["3", "pos", "pos system", "system", "sys", "ops", "pos sys", "possystem", "posys"]: 