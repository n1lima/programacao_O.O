from datetime import datetime

class Jogador:
    __nome: str
    __posicao: str
    __data_nascimento: datetime
    __nascionalidade: str
    __altura: float
    __peso: float

    def __init__(self, nome, posicao, data_nascimento, nascionalidade, altura, peso):
        self.__nome = nome
        self.__posicao = (posicao).strip().lower()
        #O strptime (string parse time) é usado para converter uma string que representa uma data e hora em um objeto datetime
        self.__data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        self.__nascionalidade = nascionalidade
        self.__altura = altura
        self.__peso = peso

    def calcular_idade(self):
        hoje = datetime.now().date()
        idade = hoje.year - self.__data_nascimento.year 
        return idade
    
    def aposentadoria(self):
        anosParaAposentar = 0 
        if self.__posicao == 'defesa':
            anosParaAposentar = 40 - self.calcular_idade()
        elif self.__posicao == 'meio-campo':
            anosParaAposentar = 38 - self.calcular_idade()
        elif self.__posicao == 'atacante':
            anosParaAposentar = 35 - self.calcular_idade()

        return anosParaAposentar

    def get_nome(self):
        return self.__nome
    
    def get_posicao(self):
        return self.__posicao
    
    def get_data_nascimento(self):
        return self.__data_nascimento
    
    def get_nascionalidade(self):
        return self.__nascionalidade
    
    def get_altura(self):
        return self.__altura
    
    def get_peso(self):
        return self.__peso
    
    def __str__(self):
        info = (f'O Jogador: {self.get_nome()}\n'
                f'Posicao: {self.get_posicao()}\n'
                f'Data de Nascimneto: {self.get_data_nascimento()}\n'
                f'Nascionalidade: {self.get_nascionalidade()}\n'
                f'Altura: {self.get_altura():.2f}\n'
                f'Peso: {self.get_peso()}\n'
                f'Idade: {self.calcular_idade()}\n'
                f'Anos para se aposentar: {self.aposentadoria()}\n')
        return info