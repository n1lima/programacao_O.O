'''
Classe Livro: Implemente uma classe Livro com atributos titulo, autor e ano_publicacao. 
Adicione um método que exiba as informações do livro formatadas.Crie alguns objetos dessa classe e exiba as informações dos livros.
'''
from common import *

def informacoesLivro():
    titulo = input('Qual o titulo do livro?')
    autor = input('Qual eh o autor?')
    while True:
        try:
            ano_publicado = int(input('Qual o ano de publicacao?'))
            if ano_publicado > 0:
                break
            else:
                print('Precisa ser número inteiro')
        except ValueError:
            print('[ERRO]Precisa ser um número')
                
    return Livro(titulo, autor, ano_publicado)

if __name__ == '__main__':
    while True:
        print('Você quer adicionar um livro? [SIM/NAO]')
        op = input().upper()

        if op not in {'SIM', 'NAO'}:
            print('[ERRO] é apenas SIM ou NAO')
        if op == 'SIM':
            informacoes = informacoesLivro()
            print('Informacoes registradas com sucesso!\n')
            print(informacoes)
        elif op == 'NAO':
            print('saindo...') 
            break

        

            