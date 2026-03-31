import random
space = "      "
coins = 100
easy_try = 20
normal_try = 15
insane_try = 10

print("Welcome to the most generic guessing game you've ever seen!" "\n")
print("Easy" + space + "Normal" + space + "Insane")
level = input("Choose the difficulty level: ")

level = str(level).lower()

while True:
    try:

        if level in ["easy", "e", "1"]: #easy mode starts here


            sort_number = random.randint(1,100)
            for i in range (20): 

                print(f"number: {sort_number}")

                guess = int(input("Choose a number between 1 and 100: "))
                if guess == sort_number:
                    coins += 20
                    print("Player Wins!")
                    retry = input("If you wanna play again type 'continue' or 'quit' to close the game: ")
                    if retry in ["continue", "yes", "y", "play"]:
                        continue
                    else:
                        break
                else:
                    easy_try -= 1
                    if easy_try == 0:
                        retry = print("If you wanna play again type 'continue' or 'quit' to close the game: ")
                        if retry in ["continue", "yes", "y", "play"]:
                            continue
                        else:
                            break




    except ValueError:
        print ("Please, type a valid value.")            
    

    
        


