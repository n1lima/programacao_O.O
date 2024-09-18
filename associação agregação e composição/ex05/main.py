from common import *

produto1 = Produto('trakinas', 4)
produto2 = Bebida('todynho', 3, False)
produto3 = Lanche('Misto', 6)
item = Produto('tomate', 2)
produto3.add_item(item)

pedido = Pedido(1)
pedido.adicionando_produto(produto1)

print(pedido)
print(produto2)
print(produto3)
