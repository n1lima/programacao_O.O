"""
Crie uma classe abstrata chamada Animal com métodos falar e mover, depois implemente duas subclasses, 
Cachorro e Gato, cada uma com sua própria versão desses métodos.
"""
from common import *

cachorro = Cachorro()
cachorro.falar()
cachorro.racao()

gato = Gato()
gato.falar()
gato.racao()