lista = [1, 2, 3, 4, 5]
lista_invertida = []
tamanho = len(lista)

for i in range(tamanho - 1, -1, -1):
    lista_invertida.append(lista[i])

print("Lista invertida: ", lista_invertida)