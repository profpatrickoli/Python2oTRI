from conta import Conta
contas = []
print("### BEM VINDO A TELA DE CADASTRO DE CONTAS ###")
while(True):
    print("NOVO USUÁRIO: \n")
    numero = int(input("Digite o número da conta do cliente: \n"))
    senha = int(input("Solicite uma nova senha ao cliente: \n"))
    titular = input("Digite o nome completo do cliente: \n")
    saldo = 0.0
    limite = 100.0
    novaConta = Conta(numero, senha, titular, saldo, limite)

    contas.append(novaConta)
    # TESTE PARA VER SE O SISTEMA FUNCIONA:
    for conta in contas:
        print(conta.numero, " - ", conta.titular)

