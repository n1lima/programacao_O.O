from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def racao(self):
        pass

class Cachorro(Animal):

    def falar(self):
        print("au au!")

    def racao(self):
        print("golden")

class Gato(Animal):

    def falar(self):
        print("miau maiau!")

    def racao(self):
        print("frisk")