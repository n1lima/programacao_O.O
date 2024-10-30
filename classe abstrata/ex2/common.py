from abc import ABC, abstractmethod

class Trabalhador(ABC):
    def __init__(self, nome: str):
        self.nome = nome 

    @abstractmethod
    def calcular_pagamento(self, horas_trabalhada: int):
        pass

class Empregado(Trabalhador):

    def calcular_pagamento(self, horas_trabalhada: int):
       return 3.000
    
    
