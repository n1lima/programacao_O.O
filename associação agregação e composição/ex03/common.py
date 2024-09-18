class Motor:
    def __init__(self, potencia: float):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo: str, potencia_motor: float):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

    def __str__(self):
        info = (f'O modelo do carro eh {self.modelo}\n'
                f'com a potencia de {self.motor.potencia}')
        return info