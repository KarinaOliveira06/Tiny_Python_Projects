#O programa irá identificar e mostrar todos os números pares informados pelo usuário
pares = []
impares = []

for i in range(2):

    try:

        number = int(input("Type a number: "))
        if number % 2 == 0:
            pares.append(number)
        else: impares.append(number)

    except ValueError:
        print("Valor inválido!")

print(f"Os números pares são: {pares}")




