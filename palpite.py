import random

a1 = random.randint(1, 99)
r = random.uniform (1, 99)
value_adjustment = round(r, 1)

for i in range(3):
    print(f"Termo {i+1}: {a1+(i*value_adjustment)}")


while True:
    answer = input("Type the correct ratio or 'exit' to quit :" )

    if answer.lower().strip() == "exit":
        print("See u later!")
        break
    elif value_adjustment == float(answer):
        print("Congratulations, you won!")
        break
    else:
        print("Nop, try again!")

