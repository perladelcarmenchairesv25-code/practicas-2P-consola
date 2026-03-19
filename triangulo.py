class triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
       return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        return self.base + self.altura + self. altura