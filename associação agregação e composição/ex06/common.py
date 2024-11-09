from typing import List

class Veiculo:
    def __init__(self, placa: str, modelo: str, ano: int):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        info = '--- Informações dos Veículos ---\n'
        info += (f'Placa: {self.placa}\n'
                f'Modelo: {self.modelo}\n'
                f'Ano: {self.ano}\n')
        return info
    
class Carro(Veiculo):
    def __init__(self, placa: str, modelo: str, ano: int, tipo: str):
        super().__init__(placa, modelo, ano)
        self.tipo = tipo

    def __str__(self):
        info = super().__str__()
        info += (f'Tipo: {self.tipo}\n')
        return info 
    
class Moto(Veiculo):
    def __init__(self, placa: str, modelo: str, ano: int, cilindrada: int):
        super().__init__(placa, modelo, ano)
        self.cilindrada = cilindrada

    def __str__(self):
        info = super().__str__()
        info += (f'Cilindrada da Moto eh: {self.cilindrada}cm³\n')
        return info
    
class Estacionamento:
    def __init__(self, nome: str, vagas: int):
        self.nome = nome
        self.vagas = vagas
        self.veiculos: List[Veiculo] = []

    def add_veiculo(self, v: Veiculo):
        if len(self.veiculos) < self.vagas:
            self.veiculos.append(v)
        else:
            print('Não há vagas o Suficiente')

    def remover_veiculo(self, placa: str):
        try:
            for veiculo in self.veiculos:
                if veiculo.placa == placa:
                    self.veiculos.remove(veiculo)
                    print('Veiculo Removido\n')
                    return #Retorna ao metodo apos achar a placa no loop
            print('Placa não encontrada\n') #caso não ache ele mostra essa mensagem
        except ValueError:
            print('Erro ao tentar remover o veículo\n')
    
    def listar_veiculos(self):
        if self.veiculos:
            for e in self.veiculos:
                print(f'Veiculos Disponiveis:\n {e}')
        else:
            print('Nenhum veículo no estacionamento.')

    def vagas_disponiveis(self):
        if self.vagas:
            vagasLivres = self.vagas - len(self.veiculos)
            return f'Vagas disponiveis: {vagasLivres}'
        
      

        

