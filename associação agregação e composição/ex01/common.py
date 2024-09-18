class Aluno:
    aluno: str
    def __init__(self, aluno):
        self.aluno = aluno

    def inscrever(self, disciplina):
        return f'O aluno {self.aluno} se inscreveu na disciplina {disciplina.disciplina}'
        # está acessando o atributo disciplina da instância da classe Disciplina
    
class Disciplina:
    disciplina: str
    def __init__(self, disciplina):
        self.disciplina = disciplina

    
