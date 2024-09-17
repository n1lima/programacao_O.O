class Funcionario:
    __nome: str
    __salario: float
    __cargo: str

    def __init__(self, nome, salario, cargo):
        self.__nome = nome
        self.__salario = salario
        self.__cargo = cargo

    def get_nome(self):
        return self.__nome
    
    def get_salario(self):
        return self.__salario
    
    def get_cargo(self):
        return self.__cargo
    
    def __str__(self):
        info = (f'Nome:{self.get_nome()}\n'
                f'Salario: R${self.get_salario():.3f}\n'
                f'Cargo:{self.get_cargo()}\n')
        return info
    
class Gerente(Funcionario):
    __numero_de_subordinados: int

    def __init__(self, nome, salario, cargo, numero_de_subordinados):
        super().__init__(nome, salario, cargo)
        self.__numero_de_subordinados = numero_de_subordinados

    def bonus(self):
        salarioComBonus = self.get_salario()

        if self.__numero_de_subordinados > 60:
           salarioComBonus += self.get_salario() * 10/100
           return salarioComBonus
        elif self.__numero_de_subordinados >= 50:
            salarioComBonus += self.get_salario() * 20/100
            return salarioComBonus
        else:
            return 'Não teve bônus!'
        
    def get_numero_de_subordinados(self):
        return self.__numero_de_subordinados
    
    def __str__(self):
        info = super().__str__()
        info += (f'Numero de subordinados: {self.get_numero_de_subordinados()}\n'
                 f'Salario com bônus: R${self.bonus():.3f}\n')
        return info
    
class Desenvolvedor(Funcionario):
    __linguagens_de_programacao: str

    def __init__(self, nome, salario, cargo, linguagens_de_programacao):
        super().__init__(nome, salario, cargo)
        # Remover espaços em branco e vírgulas ao redor de cada linguagem
        self.__linguagens_de_programacao = [ling.strip() for ling in linguagens_de_programacao.split(',')]

    def bonus(self):
        salarioComBonus = self.get_salario()
        numeros_de_ling = len(self.__linguagens_de_programacao)

        if numeros_de_ling < 5:
           salarioComBonus += self.get_salario() * 10/100
        elif numeros_de_ling > 5:
            salarioComBonus += self.get_salario() * 20/100

        return salarioComBonus
        
    def get_linguagens_de_programacao(self):
        return self.__linguagens_de_programacao
    
    def __str__(self):
        info = super().__str__()
        info += (f'Desenvolve nessas linguagens: {self.get_linguagens_de_programacao()}\n'
                  f'Salario com bônus: R${self.bonus():.3f}\n')
        return info

    