lista = [1, 2, 2, 3, 4, 3, 5]
nova_lista = []

for item in lista:
    if item not in nova_lista:
        nova_lista.append(item)

print(nova_lista)