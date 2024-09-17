'''
Classe ContaBancaria: Implemente uma classe ContaBancaria com atributos titular, saldo e limite. Crie métodos para depositar, 
sacar e verificar o saldo. Adicione a regra de que o saque não pode exceder o limite permitido.
'''
from common import ContaBancaria 

def menuDeEntrada():
    titular =  input('Digite o seu nome: ')
    saldo = float(input('Digite o seu saldo bancario: '))
    limite = float(input('Digite o limite de saque da sua conta: '))
    return ContaBancaria(titular, saldo, limite)

def acao():
    print('Você deseja:')
    print('1- Depositar')
    print('2- Sacar')
    print('3- Verificar Saldo')
    print('4 - sair')
    op_acao = int(input())
    return op_acao
    
if __name__ == '__main__':

    while True:
        print('Bem vindo(a) a sua conta bancaria!\n1-Entrar na conta | 2-Ops, não sei o que estou fazendo aqui!\n')
        op = int(input())
        try:
            if op == 1:
                dados = menuDeEntrada()
                print(f'entrou na conta! Seja Bem-vindo(a) {dados.titular}\n')
                break
            elif op == 2:
                break
            else:
                print('[ERRO] Só há duas opções [1,2]')
        except ValueError:
            print('[ERRO] Algarismo errado! só pode entra [1,2]')

    if dados: #se 'dados' contiver uma string não vazia, execute:
        while True:
            acao_titular = acao()
            try:
                if acao_titular == 1:
                    valor = float(input('Quanto você quer depositar?\n'))
                    print(dados.depositar(valor))
                elif acao_titular == 2:
                    saque = float(input('Quanto voce gostaria de sacar?\n'))
                    print(dados.sacar(saque))   
                elif acao_titular == 3:
                    print(dados.verificandoSaldo())
                elif acao_titular == 4:
                    print(dados)
                else:
                    print('[ERRO] Só há duas opções [1,2]')
            except ValueError:
                print('[ERRO] Algarismo errado! só pode entra [1,2]')


                
    

                

