a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

if a < b + c and b < a + c and c < a + b:
    print("forma triângulo")
else:
    print("não forma triângulo")