import math
class Estadisticas:
    def __init__(self, valores):
        self.valores = valores

    def promedio(self):
        return sum(self.valores) / len(self.valores)

    def desviacion(self):
        m = self.promedio()
        return math.sqrt(sum((x - m) ** 2 for x in self.valores) / (len(self.valores) - 1))

print("\n--- Estadísticas con POO ---")
numeros = [float(x) for x in input("Ingrese 10 números separados por espacio: ").split()]
est = Estadisticas(numeros)
print(f"El promedio es {est.promedio():.2f}")
print(f"La desviación estándar es {est.desviacion():.5f}")