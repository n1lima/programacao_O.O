class Veiculo:
    marca: str
    modelo: str
    ano: int
    __valor: float

    def __init__(self, marca, modelo, ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.__valor = valor

    def get_valor(self):
        return self.__valor

    def __str__(self):
        info = (f'Marca: {self.marca}\n'
                f'Modelo: {self.modelo}\n'
                f'Ano: {self.ano}\n')
        return info

class Carro(Veiculo):

    def __init__(self, marca, modelo, ano, valor):
        super().__init__(marca, modelo, ano, valor)
        self.__valor_seguro = 0

    def get_valor_seguro(self):
        return self.__valor_seguro

    def calcular_seguro(self):

        valor_veiculo =  self.get_valor()
        
        dano_total = valor_veiculo * 0.50
        dano_terceiro = valor_veiculo * 0.20
        dano_roubo = valor_veiculo * 0.25
        guincho =  200
        oficina =  150
        sinistro = valor_veiculo * 0.10
        
        self.__valor_seguro = (dano_total + dano_roubo + dano_terceiro + guincho + oficina + sinistro)
                               
        return self.__valor_seguro 

    def __str__(self):
       info = super().__str__()
       info += (f'O valor do seguro do seu carro eh {self.calcular_seguro():.2f}')
       return info
      
class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, ano, valor):
        super().__init__(marca, modelo, ano, valor)
        self.__valor_seguro = 0

    def get_valor_seguro(self):
        return self.__valor_seguro

    def calcular_seguro(self):

        valor_veiculo =  self.get_valor()

        dano_total = valor_veiculo * 0.50
        dano_terceiro = valor_veiculo * 0.30
        dano_roubo = valor_veiculo * 0.40
        guincho =  150
        oficina =  100
        sinistro = valor_veiculo * 0.08
        
        self.__valor_seguro = (dano_total + dano_roubo + dano_terceiro + guincho + oficina + sinistro)
                               
        return self.__valor_seguro 

    def __str__(self):
       info = super().__str__()
       info += (f'O valor do seguro do sua moto eh {self.calcular_seguro():.2f}')
       return info

