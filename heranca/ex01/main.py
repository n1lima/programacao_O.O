"""
Sistema de Animais

Crie uma classe base chamada Animal com atributos protegidos como nome, idade e especie. Adicione métodos para definir e obter esses atributos.
Crie subclasses Mamifero e Ave que herdam de Animal. Adicione atributos e métodos específicos para cada uma das subclasses, como tipo_de_pelo para Mamifero e tipo_de_ninho para Ave.
Implemente métodos para exibir informações detalhadas sobre cada animal, garantindo que a encapsulação seja mantida.
"""
from common import *

def menu():
    nome = input('digite o nome do seu bichinho: ')
    idade = int(input('digite a idade do seu bichinho: '))
    especie = input('digite a especie do seu bichinho: ')
    return nome, idade, especie

def tipoDeAnimal():
    try:
        op = int(input('Qual é o tipo de aimal que você quer entrar 1- Mamifero | 2- Ave'))
        return op
    except ValueError:
        print('Digite número inteiro entra [1,2]')
        return None
    
if __name__ == '__main__':
  
    while True:
        try:
            inseir = input('Você quer inseir um bichinho? [SIM/NAO]').strip().upper()
            if inseir == 'SIM':
                nome, idade, especie = menu()

                op = tipoDeAnimal()
                
                if op == 1:
                    tipoDePelo = input('Digite o tipo de pelo: ')
                    informacoesDoAnimal = Mamifero(nome, idade, especie, tipoDePelo)
                elif op == 2:
                    tipoDeNinho = input('Digite o tipo de ninho: ')
                    informacoesDoAnimal = Ave(nome, idade, especie, tipoDeNinho)
                else:
                    print('Digite apenas 1 e 2')
                    continue

                print(informacoesDoAnimal)
                continue

            elif inseir == 'NAO':
                print('saindo...')
            break
        except ValueError:
            print('Digite apenas SIM ou NAO')

    