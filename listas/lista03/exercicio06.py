import random

numero = random.randint(1, 100)
tentativas = []

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas.append(palpite)

    if palpite == numero:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero:
        print("Número maior.")
    else:
        print("Número menor.")

print("Histórico de tentativas:", tentativas)
