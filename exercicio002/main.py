'''
Classe Produto: Crie uma classe Produto que tenha os atributos nome, preco e quantidade. Adicione um método calcular_valor_total
que retorne o valor total do produto (preço multiplicado pela quantidade).
Depois, crie alguns objetos dessa classe e calcule o valor total de cada produto.
'''
from common import Produto# Importando a classe Produto do arquivo common.py

def inserir_valores():
    nome = input('Qual produto você pegou? ')
    preco = float(input('Digite seu valor: '))
    quantidade = int(input('Digite a quantidade que você pegou: '))
    return Produto(nome, preco, quantidade)


if __name__ == '__main__':#Esta linha verifica se o arquivo está sendo executado diretamente (e não importado como módulo)
    while True:
        try:
            print('Qual opção você quer? 1 - Ver o valor total do produto | 2 - Sair')
            opcao = int(input())

            if opcao == 1:
                 produto = inserir_valores()
                 print(produto) # Aqui o método __str__ será chamado automaticamente
            elif opcao == 2:
                print('Tchau')
                break
            else:
               print('ERRO, digite 1 ou 2')
        except ValueError:#Se o usuário inserir algo que não pode ser convertido para número
            print('ERRO, digite 1 ou 2')
                
        