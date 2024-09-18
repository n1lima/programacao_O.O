"""
2. Agregação
Crie uma classe Equipe que agrega objetos da classe Jogador. Uma equipe pode ter vários jogadores, mas um jogador pode existir fora da equipe.
"""

from common import *

jogador1 = Jogador('igor')
jogador2 = Jogador('joao')

equipe = Equipe('flamento')
equipe.adicionando_jogador(jogador1)
equipe.adicionando_jogador(jogador2)

print(equipe)

