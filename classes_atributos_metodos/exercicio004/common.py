class ContaBancaria:
    titular: str
    saldo: float
    limite: float

    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor
        return f'Deposito de R${valor} feito com sucesso!'

    def sacar(self, valorDeSaque):
        if  valorDeSaque  > self.limite:
            return 'Excedou o Limite da sua Conta!'
        if  valorDeSaque > self.saldo:
            return 'Saldo Insuficiente!'
        self.saldo -= valorDeSaque
        return f'Saque de {valorDeSaque} feito com sucesso'

    def verificandoSaldo(self):
        return f'Você tem R${self.saldo} em sua conta'
    
    def __str__(self):
        return f'O titular: {self.titular}\nestá com o saldo atual de {self.saldo}'
