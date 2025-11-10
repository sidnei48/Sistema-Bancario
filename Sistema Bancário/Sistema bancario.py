from funcoes import (
    deposito,
    saque,
    extrato,
    sair,
    cadastro_usuario,
    busca_cpf,
    mostrar_logs,
    salvar_usuarios,
    carregar_usuarios,
)


usuarios = carregar_usuarios()

print("Bem vindo ao nosso Banco!")
while True:

    # Cadastro de usuario

    usuario = {
        "nome": "",
        "data_nascimento": "",
        "endereco": "",
        "cpf": "",
        "saldo": 0.0,
        "depositos": 0,
        "saques": 0,
        "historico": [],
    }
    cadastro = input("Voce ja possui uma conta? (s/n): ")

    if cadastro == "n":
        cadastro_usuario(usuarios)
        salvar_usuarios(usuarios)

    # Busca de usuario

    else:
        usuario = busca_cpf(usuarios)
        if usuario is None:
            print("Tente novamente ou cadastre-se.")
            continue

    executando = True
    while executando:

        # Menu

        print("Bem vindo, ", usuario["nome"])
        print("\n-------- Menu --------")
        print("Escolha a operacao que deseja realizar:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Logs")
        print("5 - Sair")
        print("----------------------")
        operacao = input("Digite o numero da operacao desejada: ")

        # Deposito

        if operacao == "1":
            valor = float(input("Digite o valor que deseja depositar: "))
            deposito(usuario, valor)

        # Saque

        elif operacao == "2":
            valor = float(input("Digite o valor que deseja sacar: "))
            saque(usuario, valor)

        # Extrato

        elif operacao == "3":
            extrato(usuario)

        # logs

        elif operacao == "4":
            mostrar_logs()

        # Sair

        elif operacao == "5":
            executando = sair()
            break
        else:
            print("Operacao invalida. Por favor, escolha uma operacao valida.")

input("\nPressione ENTER para sair...")
