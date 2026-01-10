fila = []

while True:
    print("\n1 - Entrar na fila")
    print("2 - Atender cliente")
    print("3 - Ver fila")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        fila.append(nome)

    elif opcao == "2":
        if fila:
            atendido = fila.pop(0)
            print(f"Cliente atendido: {atendido}")
        else:
            print("Fila vazia.")

    elif opcao == "3":
        print("Fila:", fila)

    elif opcao == "4":
        break
