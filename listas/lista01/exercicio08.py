valorOriginal = float(input("Insira o valor da compra: "))

desconto = 10

valorComDesconto = valorOriginal * (1- desconto / 100)

if valorOriginal >= 100:
    print(f"Valor a pagar: {valorComDesconto}.")
else:
    print(f"Valor a pagar: {valorOriginal}")