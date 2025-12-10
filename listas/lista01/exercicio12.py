salAtual = float(input("Insira o salário atual: "))

desconto15 = 15
desconto8 = 8

if salAtual < 2000:
    salFinal = salAtual *(1 + desconto15 / 100)
    aumento = salFinal - salAtual
    print(f"Valor do aumento: {aumento:.2f}. Salário final: {salFinal:.2f}.")
else:
    salFinal = salAtual *(1 + desconto8 / 100)
    aumento = salFinal - salAtual
    print(f"Valor do aumento: {aumento:.2f}. Salário final: {salFinal:.2f}.")