from common import *

estacionamento = Estacionamento('Estacione Aqui', 10)

carro = Carro('EZ3989', 'Agile', 2012, 'Popular')
print(carro)
moto = Moto('AV7890', 'Honda', 2010, 160)
print(moto)

estacionamento.add_veiculo(carro)
estacionamento.add_veiculo(moto)

estacionamento.listar_veiculos()

estacionamento.remover_veiculo('AV7890')
estacionamento.listar_veiculos()