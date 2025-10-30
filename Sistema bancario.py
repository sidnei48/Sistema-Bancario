usuarios= []
from funcoes import deposito, saque, extrato, sair

print("Bem vindo ao nosso Banco!")
while True:

    # Cadastro de usuario

    usuario = {
        "nome": "", "data_nascimento": "", "endereco": "",
          "cpf": "", "saldo": 0.0, "depositos": 0, "saques": 0, "historico": []
    }
    cadastro = input("Voce ja possui uma conta? (s/n): ")

    if cadastro == "n":
        print("Por favor, preencha os dados abaixo para criar sua conta.")

        usuario["nome"] = input("Digite seu nome completo: ")
        usuario["data_nascimento"] = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        usuario["endereco"] = input("Digite sua cid: ")
        usuario["cpf"] = input("Digite seu CPF (somente numeros): ")
        usuario["saldo"] = 0.0
        usuario["depositos"] = 0
        usuario["saques"] = 0
        usuario["historico"] = []


        usuarios.append(usuario)

        print("Conta criada com sucesso!")
    
    # Acesso de usuario

    else:
        busca_cpf = input("Digite seu CPF para acessar sua conta:")
        if usuario["cpf"] == busca_cpf:
            print("Bem vindo de volta,", usuario["nome"])
        else:
            print("CPF nao encontrado. Por favor, crie uma conta.")
            break

    executando = True
    while executando:      

        # Menu

        print("Bem vindo, ", usuario["nome"])
        print("\n-------- Menu --------")
        print("Escolha a operacao que deseja realizar:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        print("----------------------")
        operacao = input("Digite o numero da operacao desejada: ")

        # Deposito

        if operacao == "1":
            deposito(usuario)
            

        # Saque

        elif operacao == "2":
            saque(usuario)
        
        # Extrato

        elif operacao == "3":
            extrato(usuario)
        
        # Sair

        elif operacao == "4":
            executando = sair()
            break
        else:
            print("Operacao invalida. Por favor, escolha uma operacao valida.")