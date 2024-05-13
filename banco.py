# ARMAZENAMENTO CHAVE-VALOR (dictionary em Python)
def cria_conta(numero, senha, titular, saldo, limite):
    conta = {
        "numero": numero,
        "senha": senha,
        "titular": titular,
        "saldo": saldo,
        "limite": limite
    }
    return conta

def sacar(conta, valor):
    conta["saldo"] -= valor

def depositar(conta, valor):
    conta["saldo"] += valor

def extrato(conta):
    print("O saldo da conta é ", conta["saldo"], "mais limite de ", conta["limite"])

contas = []
contas.append(cria_conta(123, 123, "Patrick", 50.0, 100.0))
contas.append(cria_conta(124, 124, "Bruno", 3000.0, 100.0))
contas.append(cria_conta(125, 125, "Guilherme", 3000.0, 100.0))


# FAZER A VERIFICAÇÃO SE O USUÁRIO TEM O SALDO PARA PODER SACAR.

contaUsuario = int(input("Digite o número da sua conta: "))
indice = 0
indiceConta = 0 
for conta in contas:
    if conta["numero"] == contaUsuario:
        indiceConta = indice
        print(indiceConta)
        break
    indice = indice + 1

while(True):    
    print("1 - Sacar \n2 - Depositar \n3 - Extrato\n")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        valor_saque = float(input("Digite o valor do saque: \n"))
        sacar(contas[indice], valor_saque)
    elif opcao == 2:
        valor_deposito = float(input("Digite o valor do depósito: \n"))
        depositar(contas[indice],valor_deposito)
    elif opcao == 3:
        extrato(contas[indice])
    else:
        print("Opção inválida")
