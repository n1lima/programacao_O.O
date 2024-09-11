class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularArea (self):
        return self.largura * self.altura

    def calcularPerimetro (self):
       return 2*(self.altura + self.largura)

    def __str__ (self):
        return f'A area desse retangulo sera {self.calcularArea()} e seu parametro eh {self.calcularPerimetro()}'