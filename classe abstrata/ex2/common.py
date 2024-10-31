from abc import ABC, abstractmethod

class Trabalhador(ABC):
    def __init__(self, nome: str):
        self.nome = nome 

    @abstractmethod
    def calcular_pagamento(self, horas_trabalhada: int):
        pass

class Empregado(Trabalhador):

    def calcular_pagamento(self, horas_trabalhada: int):
       return '3.000'
    
class Freelancer(Trabalhador):

    def calcular_pagamento(self, horas_trabalhada: int):
        return horas_trabalhada * 80
    
class Estagiario(Trabalhador):

    def calcular_pagamento(self, horas_trabalhada: int):
        pagamento = horas_trabalhada * 15
        return min(pagamento, 1500) #irá retornar o menor valor entre o pagamento calculado e o limite de R$ 1500


