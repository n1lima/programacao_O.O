class Livro:
    titulo: str
    autor: str
    ano_publicado: int

    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado

    def __str__(self):
        info = (f'O titulo do livro: {self.titulo}\n'
                f'O autor eh: {self.autor}\n'
                f'E seu ano de publicação eh: {self.ano_publicado}\n')
        return info

