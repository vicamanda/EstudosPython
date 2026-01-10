numeros = [10, -5, 3, -2, 7, 0]

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / len(numeros)

positivos = 0
negativos = 0

for n in numeros:
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print("Maior:", maior)
print("Menor:", menor)
print("Soma:", soma)
print("Média:", media)
print("Positivos:", positivos)
print("Negativos:", negativos)
