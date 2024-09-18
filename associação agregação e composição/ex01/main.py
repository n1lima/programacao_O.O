"""
1. Associação
Crie um programa que modele a relação de associação entre Aluno e Disciplina.
"""
from common import *

aluno = Aluno('Joao')
disciplina = Disciplina('matematica')

print(aluno.inscrever(disciplina))