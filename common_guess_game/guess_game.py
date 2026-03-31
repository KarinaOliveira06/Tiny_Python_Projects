from functions import retry
import random

space = "      "
coins = 100
easy_try = 20
normal_try = 15
insane_try = 10

print("Welcome to the most generic guessing game you've ever seen!" "\n") #Title
print("Easy" + space + "Normal" + space + "Insane")

while True: #Game start

    try:
        level = input("Choose the difficulty level: ")
        level = str(level).lower()
    except ValueError:
        print("Something went wrong, please try again.")

    try:
        if level in ["easy", "e", "1"]: #easy mode starts here

            sort_number = random.randint(1,100)

            for i in range (20): 

                print(f"number: {sort_number}")

                guess = int(input("Choose a number between 1 and 100: "))

                if guess == sort_number:
                    coins += 20
                    print("Player Wins!")
                    if retry():
                        break
                    else: exit()
                else:
                    easy_try -= 1
                    if easy_try == 0:
                        if retry():
                            break
        else:
            print("Please type a valid value!")


    except ValueError:
        print ("ValueError.")            
    

    
        


