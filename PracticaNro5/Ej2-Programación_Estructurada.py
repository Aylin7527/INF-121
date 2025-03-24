import math
def promedio(valores):
    return sum(valores) / len(valores)

def desviacion(valores):
    m = promedio(valores)
    return math.sqrt(sum((x - m) ** 2 for x in valores) / (len(valores) - 1))

print("\n--- Estadísticas con POO ---")
numeros = [float(x) for x in input("Ingrese 10 números separados por espacio: ").split()]
print(f"El promedio es {promedio(numeros):.2f}")
print(f"La desviación estándar es {desviacion(numeros):.5f}")