from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def tipo_combustivel(self):
        pass

    @abstractmethod
    def velocidade_maxima(self):
        pass

class Carro(Veiculo):
    def __init__(self, marca:str, modelo:str, ano_fabricado:int, cor:str):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricado = ano_fabricado
        self.cor = cor

    def tipo_combustivel(self):
        return 'gasolina'
    
    def velocidade_maxima(self):
        return 180
    
    def __str__(self):
        info = (f'Marca: {self.marca}\n'
                f'Modelo: {self.modelo}\n'
                f'Ano Fabricado: {self.ano_fabricado}\n'
                f'Cor: {self.cor}\n')
        return info 
    
class Bicicleta(Veiculo):
    def __init__(self, marca:str, modelo:str, tipo_bicicleta:str, cor:str):
        self.marca = marca
        self.modelo = modelo
        self.tipo_bicicleta = tipo_bicicleta
        self.cor = cor

    def tipo_combustivel(self):
        return 'nenhum'
    
    def velocidade_maxima(self):
        return 25
    
    def __str__(self):
        info = (f'Marca: {self.marca}\n'
                f'Modelo: {self.modelo}\n'
                f'Tipo De Bicicleta: {self.tipo_bicicleta}\n'
                f'Cor: {self.cor}\n')
        return info 