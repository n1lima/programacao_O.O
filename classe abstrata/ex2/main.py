from common import *

contratado = Empregado('nicoly')
estagiario = Estagiario('joao')
freela = Freelancer('matheus')

print(f'O trabalhor: {contratado.nome} recebe apenas {contratado.calcular_pagamento(160)}')
print(f'O trabalhor: {estagiario.nome} recebe apenas {estagiario.calcular_pagamento(160)}')
print(f'O trabalhor: {freela.nome} recebe apenas {freela.calcular_pagamento(160)}')