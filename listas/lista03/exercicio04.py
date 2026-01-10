notas = []

while len(notas) < 5:
    nota = float(input("Digite uma nota (0 a 10): "))
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida!")

media = sum(notas) / len(notas)
print("Média:", media)
