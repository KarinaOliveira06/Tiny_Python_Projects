from functions import retry_function #retry restart the game
from functions import guess_function
from functions import gameover_function
from functions import save_coins, load_coins
import random #random generates sort_number 

coins = load_coins()
space = "      "

print("Welcome to the most generic guessing game you've ever seen!" "\n") #Title
print("Easy" + space + "Normal" + space + "Insane")

while True: #Game start
    
    if gameover_function(coins):
        
        try:
            level = input("Choose the difficulty level: ")
            level = str(level).lower()
            print(f"Current Balance: {coins}")
        except ValueError:
            print("Something went wrong, please try again.")
    
        try:
            if level in ["easy", "e", "1"]:
                sort_number = random.randint(1, 100)
                chances = 20

                for i in range(20): 
                    try:
                        guess = int(input(f"Chances: {chances} | Choose a number: "))
                        if guess_function(guess, sort_number):
                            coins += 20   
                            save_coins(coins) 
                            if retry_function():
                                break
                            else: exit()
                        else:
                            chances -= 1
                            print(f"Your chances: {chances}")
                            if chances <= 0:
                                coins -= 20
                                save_coins(coins)
                                if retry_function():
                                    break
                    except ValueError:
                        print("Something went wrong, please try again.")

            elif level in ["normal", "n", "2"]:
                sort_number = random.randint(1, 100)
                chances = 15

                for i in range(15): 
                    try:
                        guess = int(input(f"Chances: {chances} | Choose a number: "))
                        if guess_function(guess, sort_number):
                            coins += 30   
                            save_coins(coins) 
                            if retry_function():
                                break
                            else: exit()
                        else:
                            chances -= 1
                            print(f"Your chances: {chances}")
                            if chances <= 0:
                                coins -= 30
                                save_coins(coins)
                                if retry_function():
                                    break
                    except ValueError:
                        print("Something went wrong, please try again.")

            elif level in ["insane", "i", "3"]:
                sort_number = random.randint(1, 100)
                chances = 10

                for i in range(10): 
                    try:
                        guess = int(input(f"Chances: {chances} | Choose a number: "))
                        if guess_function(guess, sort_number):
                            coins += 40   
                            save_coins(coins) 
                            if retry_function():
                                break
                            else: exit()
                        else:
                            chances -= 1
                            print(f"Your chances: {chances}")
                            if chances <= 0:
                                coins -= 40
                                save_coins(coins)
                                if retry_function():
                                    break
                    except ValueError:
                        print("Something went wrong, please try again.")

            else:
                print("Invalid level! Please try again.")
                continue

        except ValueError:
            print("ValueError.")