from common import *

aluno1 = Aluno('nicoly', 19, 'basico')

professor = Professor('roberto', 34, 'teclado')

instrumento = Instrumento('piano', 10) 
instrumento.add_professor(professor)

curso = Curso('curso de piano', [aluno1], [professor])

print(curso)
print(instrumento)