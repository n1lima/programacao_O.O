"""
Desafio: Combinação dos Conceitos
Crie um sistema que modele uma Biblioteca, que agrega Livros e tem uma associação com Leitores. Além disso, crie a relação de composição entre Livro e Capítulos.

Regras:
- A Biblioteca agrega uma lista de Livros.
- O Leitor pode se associar a qualquer Livro.
- Cada Livro é composto por uma lista de Capítulos.
"""
from common import *

capitulo = Capitulo(10, 'array')
livro1 = Livro("Python para Iniciantes")
leitor1 = Leitor("João")
livro1.add_capitulos(capitulo)
print(livro1)

biblioteca = Biblioteca("Central")
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_leitor(leitor1)
print(biblioteca)
