from typing import List

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.__idade = idade

    def get_idade(self):
        return self.__idade
    
    def __str__(self):
        info = (f'Nome: {self.nome}\n'
                f'Idade: {self.get_idade()}\n')
        return info
    
class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, matricula: str):
        super().__init__(nome, idade)
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula
    
    def __str__(self):
        info = super().__str__()
        info += (f'Matricula: {self.get_matricula()}\n')
        return info
    
class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, departamento: str):
        super().__init__(nome, idade)
        self.departamento = departamento

    def __str__(self):
        info = super().__str__()
        info += (f'Departamento: {self.departamento}\n')
        return info

class Livro:
    def __init__(self, titulo: str, autor: str, quantidade: int, ):
        self.titulo = titulo
        self.autor = autor
        self.quantidade = quantidade 
        self.emprestado_para = None

    def emprestado(self, pessoa:Pessoa):
        if self.quantidade > 0:
            self.emprestado_para = pessoa
            self.quantidade -= 1
        else:
            print("empréstimo não pode ser feito")

    def devolver(self):
        if self.emprestado_para != None:
            self.emprestado_para = None
            self.quantidade += 1
            print(f'Livro "{self.titulo}" foi devolvido.')
        else:
            print("não há livro para devolver")

    def __str__(self):
        info = (f'Titulo: {self.titulo}'
                f'Autor: {self.autor}\n'
                f'Quantidade: {self.quantidade}\n')
        if self.emprestado_para:
            info += (f'Livro "{self.titulo}" foi emprestado para {self.emprestado_para}\n')
        else:
            info += (f'Não há nenhum livro emprestado!\n')
        return info
    
# class Biblioteca:
#     def __init__(self, nome: str):
#         self.nome = nome
#         self.lista: List[Livro] = []

#     def adicionar_livro(self, livro: Livro):
#         self.lista += livro

#     def remover_livro(self, titulo: str):
#         self.lista -= titulo 

#     def listar_livros(self):
#         for livro in self.lista:
#             print(livro)

#     def emprestar_livro(self, titulo: str, pessoa: Pessoa):
#         self.lista -= titulo

        

