class Produto:
    nome = str
    preco = float
    quantidade = int

    def __init__(self, nome, preco, quantidade):
        self.nome = nome # Atributos da instância
        self.preco = preco
        self.quantidade = quantidade 

    def  calcular_valor_total(self):
        return self.preco * self.quantidade  # Usando 'self' para acessar atributos da instância
    
    def __str__(self):
        return f'Produto {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade}. Seu valor total foi de R${self.calcular_valor_total():.2f}'