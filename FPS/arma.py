from FPS import *

class Arma:
    def __init__(self, destruicao: float):
        self.destruicao =  destruicao

    def agredir(seld, j):
        j.energia -= 5

    def __str__(self):
        info = (f'Destruição: {self.destruicao}')
        return info
    
class Faca(Arma):
    def __init__(self, lamina: int):
        super().__init__(15)
        self.lamina = 10

    def agredir(self, j):
        self.lamina -= 1
        if self.lamina > 0: 
            j.energia -= self.destruicao 


