
class Jogador:
    def __init__(self, ernergia: float):
        self.energia = 150

    def __str__(self):
        info = f'\n Energia: {self.energia}'
        return info
