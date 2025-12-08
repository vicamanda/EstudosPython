num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}.")
elif num2 > num1:
    print(f"{num2} é maior que {num1}.")
else:
    print("Os dois números inseridos são iguais.")