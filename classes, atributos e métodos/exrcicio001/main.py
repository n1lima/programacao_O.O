'''''
Ler os Dados (NOME, VALOR POR HORA, HORAS) de dois funcionarios e mostrar o valor 
total pago aos funcionarios
'''''
class Employee:
    nome = str
    valorPorHora = float
    horas = int
     
    def __init__(self, nome, valorPorHora, horas):
        self.nome = nome
        self.valorPorHora = valorPorHora
        self.horas = horas

    def salario (self):
        return self.valorPorHora * self.horas
        
nome1 = input('digite o nome do 1º funcionario: ')
salario1 = float(input('digite o salario do 1º funcionario: '))
horas1 = int(input('digite o horas do 1º funcionario: '))
funcionario1 = Employee(nome1, salario1, horas1)

nome2 = input("Digite o nome do segundo funcionário: ")
valor_por_hora2 = float(input("Digite o valor por hora do segundo funcionário: "))
horas2 = int(input("Digite as horas trabalhadas do segundo funcionário: "))
funcionario2 = Employee(nome2, valor_por_hora2, horas2)
#funcionario2 = Employee('Wagner', 80.0, 10)

total = (funcionario1.salario()) + (funcionario2.salario())

print(f'Total = {total}')