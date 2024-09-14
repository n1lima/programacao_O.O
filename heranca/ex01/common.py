class Animal:
    __nome: set
    __idade: int
    __especie: str

    def __init__(self, nome, idade, especie):
        self.__nome = nome
        self.__idade = idade
        self.__especie = especie 

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_especie(self):
        return self.__especie
    
class Mamifero (Animal):
    def tipo_de_pelo(self):


class Ave (Animal):
    def tipo_de_ninho(self):

        

