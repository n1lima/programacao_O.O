class ContaBancaria:
    titular: str
    saldo: float
    limite: float

    def __init__(self, titular, saldo, limite):
        self.titular: titular
        self.saldo: saldo
        self.limite: limite

    def depositar(self):
        depositando += self.saldo

    def sacar(self):
        sacando -= self.saldo
        if sacando > self.limite:
            return 'Excedou o Limite da sua Conta!'

    #def verificandoSaldo(self):
