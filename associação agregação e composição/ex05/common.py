from typing import List

class Produto:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.preco = preco

    def get_nome(self):
        return self.__nome

    def __str__(self):
        info = (f'O Nome do produto é {self.get_nome()}\n'
                f'E seu preço é R$ {self.preco:.2f}')
        return info

class Pedido:
    def __init__(self, numero: int):
        self.__numero = numero
        self.__produtos: List[Produto] = []

    def adicionando_produto(self, produto: Produto):
        self.__produtos.append(produto)

    def calculando_valor(self):
        preco_total = 0
        for produto in self.__produtos:
            preco_total += produto.preco
        return preco_total
    
    def __str__(self):
        info = f'O pedido número: {self.__numero}\n'
        info += 'Produtos:\n'
        for produto in self.__produtos:
           info += f'{produto}\n'  
        info += f'Valor total: R$ {self.calculando_valor():.2f}'
        return info

class Bebida(Produto):
    def __init__(self, nome: str, preco: float, alcoolica: bool):
        super().__init__(nome, preco)
        self.alcoolica = alcoolica

    def __str__(self):
        info = super().__str__()
        info += f', Alcoólica: {self.alcoolica}'
        return info

class Lanche(Produto):
    def __init__(self, nome: str, preco: float):
        super().__init__(nome, preco)
        self.itens: List[Produto] = []  # Lista de produtos no lanche

    def add_item(self, produto: Produto):
        if produto in self.itens:
            print("Produto já está no lanche")
        else:
         self.itens.append(produto)

    def __str__(self):
        info = super().__str__()
        info += '\nItens:\n'
        for item in self.itens:
            info += f'{item}\n'
        return info
