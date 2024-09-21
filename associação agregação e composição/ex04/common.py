from typing import List

class Leitor:
    def __init__(self, nome: str):
        self.__nome = nome

    def __str__(self):
        info = f'\nNome Do Leitor: {self.__nome}\n'
        return info
    
class Capitulo:
    def __init__(self, num_cap: int, titulo:str):
        self.num_cap = num_cap
        self.titulo = titulo

    def __str__(self):
        info = (f'\nNumero de Capitulos: {self.num_cap}\n'
                f'Titulo do Capitulo: {self.titulo}\n')
        return info

class Livro:
    def __init__(self, titulo: str):
        self.titulo = titulo
        self.capitulos: List[Capitulo] = []

    def add_capitulos(self, capitulos:Capitulo):
        self.capitulos.append(capitulos)

    def __str__(self):
        info = (f'\nTitulo do Livro: {self.titulo}\n')
        for capitulos in self.capitulos:
            info +=(f'Informacoes dos Capitulos: {capitulos}\n')
        return info
    
class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.livros: List[Livro] = []
        self.leitores: List[Leitor] = []
    
    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)
    
    def adicionar_leitor(self, leitor: Leitor):
        self.leitores.append(leitor)

    def __str__(self):
        info = (f'Nome da Biblioeta: {self.nome}\n')
        for livro in self.livros:
            info += f'Livro: {livro}\n'
        for leitor in self.leitores:
            info += f'Leitores: {leitor}\n'
        return info

