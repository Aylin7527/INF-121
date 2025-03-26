import math
class EcuacionesCuadraticas:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b ** 2 - 4 * self.a * self.c

    def getRaiz1(self):
        d = self.getDiscriminante()
        return (-self.b + math.sqrt(d)) / (2 * self.a)

    def getRaiz2(self):
        d = self.getDiscriminante()
        return (-self.b - math.sqrt(d)) / (2 * self.a)

    def resolver(self):
        d = self.getDiscriminante()

        if d > 0:  # Dos raíces reales
            raiz1 = self.getRaiz1()
            raiz2 = self.getRaiz2()
            print(f"La ecuación tiene dos raíces {raiz1:.6f} y {raiz2:.5f}")
        elif d == 0:  # Una raíz real
            raiz = -self.b / (2 * self.a)
            print(f"La ecuación tiene una raíz {raiz:.0f}")
        else:  
            print("La ecuación no tiene raíces reales")

print("\n--- Ecuaciónes cuadráticas ---")
a, b, c = map(float, input("Ingrese a, b, c: ").split())

ecuacion = EcuacionesCuadraticas(a, b, c)
ecuacion.resolver()
