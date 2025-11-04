usuarios= []
from funcoes import deposito, saque, extrato, sair, cadastro_usuario, busca_cpf, mostrar_logs

print("Bem vindo ao nosso Banco!")
while True:

    # Cadastro de usuario

    usuario = {
        "nome": "sidnei", "data_nascimento": "", "endereco": "",
          "cpf": "54923258845", "saldo": 0.0, "depositos": 0, "saques": 0, "historico": []
    }
    cadastro = input("Voce ja possui uma conta? (s/n): ")

    if cadastro == "n":
       cadastro_usuario(usuarios)
    
    # Busca de usuario

    else:
        busca_cpf(usuarios)

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
            deposito(usuario)
            

        # Saque

        elif operacao == "2":
            saque(usuario)
        
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