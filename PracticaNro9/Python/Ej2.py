from abc import ABC, abstractmethod
import random
import math

class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass

class Figura(ABC):
    def __init__(self, color="sin color"):
        self.color = color
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def __str__(self):
        return f"Color: {self.color}"
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="sin color"):
        super().__init__(color)
        self.lado = lado
    
    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return 4 * self.lado
    
    def comoColorear(self):
        return "Colorear los cuatro lados"
    
    def __str__(self):
        return f"Cuadrado - Lado: {self.lado}, {super().__str__()}"

class Circulo(Figura):
    def __init__(self, radio, color="sin color"):
        super().__init__(color)
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio * self.radio
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"Circulo - Radio: {self.radio}, {super().__str__()}"

figuras = []
for _ in range(5):
    tipo = random.randint(1, 2)
    color = random.choice(["rojo", "verde", "azul"])
    if tipo == 1:
        lado = random.randint(1, 10)
        figuras.append(Cuadrado(lado, color))
    else:
        radio = random.randint(1, 10)
        figuras.append(Circulo(radio, color))

for figura in figuras:
    print(figura)
    print(f"Área: {figura.area():.2f}")
    print(f"Perímetro: {figura.perimetro():.2f}")
    if isinstance(figura, Coloreado):
        print(f"Coloreado: {figura.comoColorear()}")
    print("-" * 40)