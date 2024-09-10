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
    op_acao = int(input())
    return op_acao
    

if __name__ == '__main__':

    while True:
        print('Bem vindo(a) a sua conta bancaria!')
        print('1-Entrar na conta | 2-Ops, não sei o que estou fazendo aqui!')
        op = int(input())
        try:
            if op == 1:
                dados = menuDeEntrada()
                print(f'entrou na conta! Seja Bem-vindo(a) {dados.titular}')
            elif op == 2:
                break
        except ValueError:
            print('É para escolher entre 1 e 2')

    if dados:
        while True:
            acao_titular = acao()
            try:
                if acao_titular == 1:
                    deposito = float(input('Qaunto você quer depositar? '))
                    dados.depositar(deposito)
                elif acao_titular == 2:
                    saque = float(input('Quanto voce gostaria de sacar? '))
                    dados.sacar(saque)
            except ValueError:
                print('É para escolher entre [1,3]')


                
    

                

