lista = [1, 2, 2, 3, 3, 3, 4]
contagem = {}

for elemento in lista:
    if elemento in contagem:
        contagem[elemento] += 1
    else: 
        contagem[elemento] = 1

print("Ocorrências:", contagem)