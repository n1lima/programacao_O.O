class Carro:
    marca = str
    modelo = str
    ano = int
    velocidade_atual = float

    def __init__(self, marca, modelo, ano, velocidade_atual):
        self.marca = marca
        self.modelo = modelo 
        self.ano = ano 
        self.velocidade_atual = velocidade_atual

    def acelerar (self, incrementando):
        self.velocidade_atual += incrementando #aqui apenas a váriavel atual está sendo mudada o valor

    def frear (self, decrementando):
        self.velocidade_atual -= decrementando
        
        if self.velocidade_atual < 0:
            self.velocidade_atual = 0

    def __str__ (self):
        return f'a velocidade atual do seu veiculo eh de ${self.velocidade_atual:.2f}'