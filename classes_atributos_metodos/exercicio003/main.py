'''
Classe Carro: Crie uma classe Carro com atributos marca, modelo, ano e velocidade_atual. Adicione métodos para acelerar, 
frear e exibir a velocidade atual. Teste a classe acelerando e freando o carro.
'''
from common import Carro

def inserir_carro():
    marca = input('Qual marca eh o seu carro? ')
    modelo = input('Qual eh o modelo do seu carro? ')
    ano = int(input('Qual ano o seu carro é? '))
    velocidade_atual = float(input('Por último qual velocidade é o seu carro? '))
    return Carro(marca, modelo, ano, velocidade_atual)

def menu():
    print('escolha as opcoes: ')
    print('1- acelerar')
    print('2- frear')
    print('3- Exibir velocidade atual')
    print('4- sair')
    opcao = int(input('Escolha uma opcao'))
    return opcao
    

if __name__ == '__main__':

    carro = None

    while True:
        try:
            print('Olá! Escolha entre: 1- Cadastre o seu carro | 2-Saia do Cadastro')
            op = int(input())

            if op == 1:
                carro = inserir_carro()
                print(f'Carro cadastrado: {carro.marca}, {carro.modelo} e {carro.ano}')
                break
            elif op == 2:
                print('Encerrando o programa...')
                break
            else: 
                print('Só há duas opções [1 e 2], digite uma das duas!')
        except ValueError:
            print('[ERRO] Algarismo errado! apenas números e de [1,2]')
    
    if carro:
        while True:
            acao_carro =  menu()
            try:
                if acao_carro == 1:
                    incremento = float(input('o quanto voce quer acelerar?'))
                    carro.acelerar(incremento)
                elif acao_carro == 2:
                    descremento = float(input('o quanto voce quer frear?'))
                    carro.frear(descremento)
                elif acao_carro == 3:
                    print(f'A velocidade atual eh de {carro.velocidade_atual:.2f}km')
                elif acao_carro == 4:
                    print('voltando ao menu pricipal...')
                    break
                else: 
                    print('Só há duas opções [1 e 2], digite uma das duas!')
            except ValueError:
                print('[ERRO] Algarismo errado! apenas números e de [1,2]')


        