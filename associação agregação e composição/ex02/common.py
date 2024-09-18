from typing import List

class Jogador:
    def __init__(self, nome: str):
        self.nome = nome

class Equipe:
    def __init__(self, nome: str): 
        self.nome = nome
        self.jogadores: List[Jogador] = [] #lista que agrega ojetos do tipo jogador

    def adicionando_jogador(self, jogador: Jogador):#aqui estamos falando que o parametro jogador é do tipo Jogador
        self.jogadores.append(jogador)

    def __str__(self):
        info = f'a equipe {self.nome} tem os seguintes jogadores:\n'
        for jogador in self.jogadores:
            info += f' - {jogador.nome}\n'
        return info


