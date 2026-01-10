estoque = []

while True:
    print("\n1 - Adicionar")
    print("2 - Remover")
    print("3 - Listar")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        produto = input("Nome do produto: ")
        estoque.append(produto)

    elif opcao == "2":
        produto = input("Produto para remover: ")
        if produto in estoque:
            estoque.remove(produto)
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        print("Estoque:", estoque)

    elif opcao == "4":
        break
