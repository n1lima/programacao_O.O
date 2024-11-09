from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self): #Como Forma é uma classe abstrata, as assinaturas dos métodos das subclasses devem ser idênticas à assinatura do método calcular_area na classe base (sem parâmetros específicos, já que Forma não os define)
        print(f'Area de um quadrado eh igual: {self.lado * self.lado}\n')
    
class Triangulo(Forma):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self):
       print(f'Area de um triangulo eh igual:{self.base * self.altura/2}\n')
        
        