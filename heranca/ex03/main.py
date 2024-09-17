"""
Crie uma classe para representar um jogador de futebol, com os atributos nome, posição, data de nascimento, nacionalidade, altura e peso. Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos os dados do jogador. Crie um método para calcular a idade do jogador e outro método para mostrar quanto tempo falta para o jogador se aposentar. Para isso, considere que os jogadores da posição de defesa se aposentam em média aos 40 anos, os jogadores de meio-campo aos 38 e os atacantes aos 35.
"""
from common import *

jogador = Jogador('igor', 'atacante', '11/3/2003', 'brasileiro', 1.90, 90)
print(jogador)

jogador2 = Jogador('camila', 'defesa', '12/12/1997', 'japonesa', 1.88, 89)
print(jogador2)
