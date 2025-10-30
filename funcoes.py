
# Depositos
def deposito(usuario):
    valor_deposito = float(input("Digite o valor que deseja depositar: "))
    if valor_deposito > 0:
        usuario["saldo"] += valor_deposito
        usuario["historico"].append(f"Deposito: +R$ {valor_deposito:.2f}")
        usuario["depositos"] += 1
        print(f'Deposito realizado com sucesso! Saldo atual: R$ {usuario["saldo"]:.2f}')
    else:
        print("Valor invalido. O valor do deposito deve ser maior que zero.")

#Saques
def saque(usuario):
    valor_saque = float(input("Digite o valor que deseja sacar: "))
    if valor_saque > usuario["saldo"]:
        print("Saldo insuficiente para realizar o saque.")
    else:
        usuario["saldo"] -= valor_saque
        usuario["historico"].append(f"Saque: -R$ {valor_saque:.2f}")
        usuario["saques"] += 1
        print(f"Saque realizado de {valor_saque} com sucesso!")
        print(f"Saldo atual: {usuario['saldo']}")

# Extrato
def extrato(usuario):
    print('\n====Extrato====')
    for mov in usuario["historico"]:
        print(mov)
    print(f'Saldo atual: {usuario["saldo"]}')
    print(f'Depósitos realizado: {usuario["depositos"]}')
    print(f'Saques realizados: {usuario["saques"]}')
    print('====Fim do Extrato====\n')

# sair
def sair():

    print('Obrigado por usar nosso banco. Ate mais!')
    return False

def cadastro_usuario(usuarios):
    usuario = {
        "nome": "", "data_nascimento": "", "endereco": "",
          "cpf": "", "saldo": 0.0, "depositos": 0, "saques": 0, "historico": []
    }
    
    print("Por favor, preencha os dados abaixo para criar sua conta.")

    usuario["nome"] = input("Digite seu nome completo: ")
    usuario["data_nascimento"] = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    usuario["endereco"] = input("Digite sua cidade: ")
    usuario["cpf"] = input("Digite seu CPF (somente numeros): ")
    usuario["saldo"] = 0.0
    usuario["depositos"] = 0
    usuario["saques"] = 0
    usuario["historico"] = []

    usuarios.append(usuario)

    print("Conta criada com sucesso!")