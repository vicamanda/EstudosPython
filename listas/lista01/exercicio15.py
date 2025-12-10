user = str(input("Cadastre o nome de usuário: "))
password = str(input("Cadastre a senha: "))

userTest = str(input("Insira o nome de usuário cadastrado: "))
passwordTest = str(input("Insira a senha cadastrada: "))

if user == userTest and password == passwordTest:
    print("Acesso permitido.")
else:
    print("Acesso negado.")