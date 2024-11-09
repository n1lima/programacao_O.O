from common import *

carro = Carro('toyota', 'minivan', 2012, 'preto')
bicicleta = Bicicleta('caloi', 'speed', 'entrada', 'branco')

print(carro, carro.tipo_combustivel(), carro.velocidade_maxima())
print(bicicleta, bicicleta.tipo_combustivel(), bicicleta.velocidade_maxima())