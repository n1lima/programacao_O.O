"""
Sistema de Veículos

Crie uma classe base chamada Veiculo com atributos marca, modelo, ano e o privado valor que você pagou no seu veiculo. Depois
faça classes filhas para calcular o seguro do carro ou da moto corretamente.
"""
from common import *

def inserirTipoVeiculo():
    try:
        print('Qual é o seu veiuculo?\n'
            '1- Carro\n'
            '2- Motocicleta\n')
        op2 = int(input())
        if op2 not in {1, 2}:
            print('Não é aceito outro algarismo')
        else:
            return op2
    except ValueError:
        print('[ERRO] Só é aceito algarismo e entre [1,2]!')


def inserirCarro():
    marca = input('Qual a marca do seu veiculo: ')
    modelo = input('Qual é modelo do seu veiculo: ')
    ano = int(input('Qual é o ano do seu veiculo: '))
    valor = float(input('Quanto você pagou no seu veiculo: '))
    return marca, modelo, ano, valor

def inserirMoto():
    marca = input('Qual a marca do seu veiculo: ')
    modelo = input('Qual é modelo do seu veiculo: ')
    ano = int(input('Qual é o ano do seu veiculo: '))
    valor = float(input('Quanto você pagou no seu veiculo: '))
    return marca, modelo, ano, valor

if __name__ == '__main__':

    op1 = input('Você gostaria de cadastrar o seu veiculo para calcular o seuguro? [SIM/NAO]').strip().upper()

    while True:
        try:
            if op1 not in {'SIM'}:
                print('saindo...')
                break
            if op1 == 'SIM':
                veiculo = inserirTipoVeiculo() 
                break
        except ValueError:
            print('[ERRO] Só é aceito os caracteres [SIM/NAO]')

if veiculo == 1:
    marca, modelo, ano, valor = inserirCarro()
    seguro_carro = Carro(marca, modelo, ano, valor)
    print(seguro_carro)
elif veiculo == 2:
    marca, modelo, ano, valor = inserirMoto()
    seguro_moto = Motocicleta(marca, modelo, ano, valor)
    print(seguro_moto)


