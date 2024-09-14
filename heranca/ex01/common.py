class Animal:
    __nome: str
    __idade: int
    __especie: str

    def __init__(self, nome, idade, especie):
        self.__nome = nome
        self.__idade = idade
        self.__especie = especie 

    #leitura dos atributos privado
    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_especie(self):
        return self.__especie
    
    #atribuição para os atributos privado
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_idade(self, idade):
        self.__idade = idade
    
    def set_especie(self, especie):
        self.__especie = especie

    #print dos atributos privado
    def __str__(self):
        info = (f'O nome do animal: {self.get_nome()}\n'
               f'A idade: {self.get_idade()}\n'
               f'E sua especie: {self.get_especie()}')
        return info
    
class Mamifero (Animal):
    def __init__(self, nome, idade, especie, tipoDePelo):
        super().__init__(nome, idade, especie)#recebendo os atributos da Classe Pai -> Animal
        self._tipoDePelo  = tipoDePelo 

    #leitura dos atributos privado
    def get_tipoDePelo(self):
        return self._tipoDePelo

    #atribuição para os atributos privado
    def set_tipoDePelo(self, tipoDePelo):
        self._tipoDePelo = tipoDePelo

    def __str__(self):
        info = super().__str__()#recebendo o 'print()' da Classe Pai -> Animal
        info += f'\ntipo de Pelo: {self.get_tipoDePelo()}'
        return info 
    
class Ave (Animal):
    def __init__(self, nome, idade, especie, tipoDeNinho):
        super().__init__(nome, idade, especie)
        self._tipoDeNinho = tipoDeNinho

    def get_tipoDeNinho(self):
        return self._tipoDeNinho
    
    def set_tipoDeNinho(self, tipoDeNinho):
        self._tipoDeNinho = tipoDeNinho

    def __str__(self):
        info = super().__str__()
        info += f'\ntipo de ninho: {self.get_tipoDeNinho()}'
        return info


        

