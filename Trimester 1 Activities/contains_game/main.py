import random
import time
import word_bank
from functions import generate_round
sort_words, correct_answer, match_letter = generate_round()

#In this game, you need to type the word that matches with the letter provided by the system.

print("Welcome to the Contains Game!" )
input("Press any button to start: ")

i = 0

try:
    for l in range(5):
        for c in range (5):
            word = sort_words[i]
            print(word.ljust(15), end="")
            i += 1
        print()
except IndexError:
    print("Error")       

start_time = time.time()
answer = input(f"Type the word that starts with {match_letter}: ").lower()
end_time = time.time()
total_time = end_time - start_time

if answer.startswith(match_letter) and total_time<7:
    print("Whoa! Someone's in a hurry!!")
elif answer.startswith(match_letter) and 7<total_time<13:
    print("Congratulations! You finished with a great time!")
elif answer.startswith(match_letter) and 13<total_time:
    print("Nice try, but I've seen turtles with more hustle.")
else:
    print("Sorry, you lose, what about restart and try again?")
        
     

            

    