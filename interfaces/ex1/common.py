from abc import ABCMeta, abstractmethod

class IVeiculo(ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Carro(IVeiculo):

    def ligar(self):
        return 'Carro Ligado'
    
    def mover(self):
        return 'Carro em movimento'
    
class Bicicleta(IVeiculo):

    def ligar(self):
        return 'Bicicleta pronta para uso'
    
    def mover(self):
        return 'Bicicleta em Movimento'