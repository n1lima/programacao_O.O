from abc import ABC, abstractmethod
from typing import List

class Animal(ABC):

    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):

    def emitir_som(self):
        return "AU AU"
    
class Gato(Animal):

    def emitir_som(self):
        return "Miau"
    

def emitir_sons(animais: List[Animal]):
    for animal in animais:
        print(animal.emitir_som())
    
    