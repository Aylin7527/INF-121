from multimethod import multimethod
import math

class Geometria:
    
    # Área del Círculo
    @multimethod
    def area(self, radio: float):
        return math.pi * radio ** 2
    
    # Área del Rectángulo
    @multimethod
    def area(self, base: int, altura: int):
        return base * altura
    
    # Área del Triángulo Rectángulo
    @multimethod
    def area(self, base: float, altura: float):
        return (base * altura) / 2
    
    # Área del Trapecio
    @multimethod
    def area(self, base_mayor: float, base_menor: float, altura: float):
        return ((base_mayor + base_menor) * altura) / 2
    
    # Área del Pentágono
    @multimethod
    def area(self, lado: int):
        apotema = lado / (2 * math.tan(math.pi / 5))
        return (5 * lado * apotema) / 2

geo = Geometria()
print("Área del Círculo:", geo.area(1.0))
print("Área del Rectángulo:", geo.area(2, 3))
print("Área del Triángulo Rectángulo:", geo.area(3.0, 4.0))
print("Área del Trapecio:", geo.area(5.0, 7.0, 4.0))
print("Área del Pentágono:", geo.area(6))
