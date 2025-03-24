import math
class EcuacionesCuadraticas:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b ** 2 - 4 * self.a * self.c

    def getRaiz1(self):
        return (-self.b + math.sqrt(self.getDiscriminante())) / (2 * self.a)

    def getRaiz2(self):
        return (-self.b - math.sqrt(self.getDiscriminante())) / (2 * self.a)

    def resolver(self):
        d = self.getDiscriminante()
        if d > 0:
            print(f"La ecuación tiene dos raíces {self.getRaiz1():.6f} y {self.getRaiz2():.5f}")
        elif d == 0:
            print(f"La ecuación tiene una raíz {self.getRaiz1():.0f}")
        else:
            print("La ecuación no tiene raíces reales")

print("\n--- Ecuaciónes cuadráticas con POO ---")
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

ecuacion = EcuacionesCuadraticas(a, b, c)
ecuacion.resolver()