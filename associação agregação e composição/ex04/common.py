from typing import List

class Leitor:
    def __init__(self, nome: str):
        self.nome = nome

class Livro:
    def __init__(self, titulo: str):
        self.titulo = titulo

class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.livros: List[Livro] = []
        self.leitores: List[Leitor] = []
    
    def adicionar_livro(self, livro: Livro) -> None:
        self.livros.append(livro)
    
    def adicionar_leitor(self, leitor: Leitor) -> None:
        self.leitores.append(leitor)

    def exibir_biblioteca(self) -> None:
        print(f"Biblioteca {self.nome} tem os seguintes livros:")
        for livro in self.livros:
            print(f"- Livro: {livro.titulo}")
        
        print("E os seguintes leitores:")
        for leitor in self.leitores:
            print(f"- Leitor: {leitor.nome}")
