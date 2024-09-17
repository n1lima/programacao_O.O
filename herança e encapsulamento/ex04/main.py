"""
Sistema de Funcionários

- Crie uma classe base chamada Funcionario com atributos protegidos nome, salario e cargo. Adicione métodos para definir e obter esses atributos.
- Crie subclasses Gerente e Desenvolvedor que herdam de Funcionario. Adicione atributos específicos, como numero_de_subordinados para Gerente e linguagens_de_programacao 
para Desenvolvedor.
- Implemente métodos para calcular o bônus salarial de cada tipo de funcionário com base em seus atributos.
"""
from common import *

funcionario = Funcionario('aline', 12.000, 'dentista')
print(funcionario)

funcionario_gerente = Gerente('bruna', 12.300, 'gestora de sistemas', 58)
print(funcionario_gerente)

funcionario_desenvolvedor = Desenvolvedor('nicoly', 20.000, 'analista de dados', 'js python R SQL C#')
print(funcionario_desenvolvedor)