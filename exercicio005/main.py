'''
Classe Retangulo: Crie uma classe Retangulo que tenha os atributos largura e altura. 
Adicione métodos para calcular a área e o perímetro do retângulo. Crie uma instância da classe e exiba os valores da área e do perímetro.
'''
from common import Retangulo

def inserindoValores():
        print('Calcule a area e o parametro do Retangulo')
        area = int(input('Qual eh a area do seu retangulo?'))
        largura = int(input('Qual a largura do seu retangulo?'))
        return Retangulo(largura, area)

if __name__ == '__main__':
        retangulo = inserindoValores()
        print(retangulo)
        