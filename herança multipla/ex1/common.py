from abc import ABC, abstractmethod

class Atleta(ABC):
    def __init__(self, nome: str, idade: int, peso: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
  
    def aquecer(self):
        return f'O atleta {self.nome} está aquecendo'

    def __str__(self):
        info = (f'Nome do Atleta: {self.nome}\n'
                f'Idade do Atleta: {self.idade}\n'
                f'Peso do Atleta: {self.peso}\n')
        return info

class Corredor(Atleta):
    def __init__(self, nome: str, idade: int, peso: float):
        super().__init__(nome, idade, peso)

    def correr(self):
        return f'O atleta {self.nome} está correndo'

    def __str__(self):
        info = super().__str__()
        return info
    
class Nadador(Atleta):
    def __init__(self, nome: str, idade: int, peso: float):
        super().__init__(nome, idade, peso)

    def nadar(self):
        return f'O atleta {self.nome} está nadando'

    def __str__(self):
        info = super().__str__()
        return info
    
class Ciclista(Atleta):
    def __init__(self, nome: str, idade: int, peso: float):
        super().__init__(nome, idade, peso)

    def pedalar(self):
        return f'O atleta {self.nome} está pedalando'

    def __str__(self):
        info = super().__str__()
        return info
    
class Triatleta(Corredor, Nadador, Ciclista):
    def realizar_maratona(self): #note que as classe pai de Triatleta não tem construtor (__init__()), isso evita conflito de métodos, o que é um problema para a Herança Múltipla
        info = self.aquecer() + '\n'
        info += self.correr() + '\n'
        info += self.nadar() + '\n'
        info += self.pedalar() + '\n'
        return info
"""
● Caso Corredor, Nadador e Ciclista tivessem seus construtores, e em triatleta
você usa-se a palavra reservada super()? O que iria acontecer? Qual das
classes pais seria chamada?
● Para lidar com isso python usa MRO (Method Resolution Order), que define
uma ordem para encontrar o método encontrado.
"""

    

    
