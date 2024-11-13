from abc import ABCMeta, abstractmethod
from typing import List

class IDispositivo (ABCMeta):
    def __init__(self):
        pass
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Televisao(IDispositivo):

    def ligar(self):
        return 'TV ligada'
    
    def desligar(self):
        return 'TV desligada'
    
class Radio(IDispositivo):

    def ligar(self):
        return 'Radio Ligado'
    
    def desligar(self):
        return 'Radio Desligado'
    
def lista_Dipositivos(d: List[IDispositivo]):
    for dispositivo in d:
        print(dispositivo.ligar())
        print(dispositivo.desligar())