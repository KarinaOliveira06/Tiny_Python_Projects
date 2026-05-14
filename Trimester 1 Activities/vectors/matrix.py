matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_total = 0
soma_diagonal = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):

        soma_total += matriz[i][j]
        

        if i == j:
            soma_diagonal += matriz[i][j]

print(f"Soma Total: {soma_total}")
print(f"Diagonal Principal: {soma_diagonal}")