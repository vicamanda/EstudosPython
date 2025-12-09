num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if (num1 >= num2) and (num1 >= num3):
    print(f"Maior número: {num1}")
elif (num2 >= num1) and (num2 >= num3):
    print(f"Maior número: {num2}")
else:
    print(f"Maior número: {num3}")