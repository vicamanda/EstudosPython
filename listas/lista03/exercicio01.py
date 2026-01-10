matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(3):
    soma_linha = sum(matriz[i])
    print(f"Soma da linha {i}: {soma_linha}")

for j in range(3):
    soma_coluna = 0
    for i in range(3):
        soma_coluna += matriz[i][j]
    print(f"Soma da coluna {j}: {soma_coluna}")
