class Conta:
    # Método construtor
    def __init__(self, numero, senha, titular, saldo, limite):
        # ATRIBUTOS DA CLASSE CONTA
        print(self)
        self.numero = numero
        self.senha = senha
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    # Métodos gerais
    def sacar(self, valor):
        self.saldo = self.saldo - valor
        print("Saque efetuado! Saldo atual: ", self.saldo)
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print("Depósito efetuado! Saldo atual: ", self.saldo)

    def verifica_saldo(self):
        print("Saldo atual: ", self.saldo)




