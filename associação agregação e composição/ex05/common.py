from typing import List

class Pessoa: 
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade
    
    def __str__(self):
        info = (f'\nNome: {self.__nome}'
                f'\nIdade: {self.__idade}\n')
        return info
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, nivel: str):
        super().__init__( nome, idade)
        self.__nivel = nivel

    def __str__(self):
        info = super().__str__()
        info += (f'Nivel: {self.__nivel}\n')
        return info

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade: str):
        super().__init__(nome, idade)
        self.__especialidade = especialidade

    def __str__(self):
        info = super().__str__()
        info += (f'Especialidade: {self.__especialidade}\n')
        return info

class Instrumento:
    def __init__(self, instrumento: str, num_instrumento: int):
        self.instrumento = instrumento
        self.num_instrumento = num_instrumento
        self.professor: List[Professor] = []

    def add_professor(self, prof: Professor):
        self.professor.append(prof)

    def __str__(self):
        info = (f'Nome do Instrumento: {self.instrumento}\n'
                f'Numero de Instrumentos: {self.num_instrumento}\n')
        if self.professor:
            info += (f'\nProfessor(es) associado a esse instrumento: \n')
            for prof in self.professor:
                info += (f'\nProfessor desse Instrumento: {prof}\n')
        else:
            info += (f'\nNenhum professor associado a esse instrumento\n')
        return info

class Curso:
    def __init__(self, curso: str, alunos: List[Aluno], professores: List[Professor] ):
        self.curso = curso
        self.aluno = alunos
        self.prof = professores

    def __str__(self):
        info = (f'Curso: {self.curso}\n')
        for aluno in self.aluno:
            info += (f'\nAlunos: {aluno}\n')
        for prof in self.prof:
            info += (f'\nProfessor: {prof}\n')
        return info