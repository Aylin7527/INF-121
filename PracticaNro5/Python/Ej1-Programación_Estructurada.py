import math
def getDiscriminante(a, b, c):
    return b ** 2 - 4 * a * c

def getRaiz1(a, b, c):
    return (-b + math.sqrt(getDiscriminante(a, b, c))) / (2 * a)

def getRaiz2(a, b, c):
    return (-b - math.sqrt(getDiscriminante(a, b, c))) / (2 * a)

print("\n--- Ecuaciónes cuadráticas con POO ---")
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

discriminante = getDiscriminante(a, b, c)

if discriminante > 0:
    print(f"La ecuación tiene dos raíces {getRaiz1(a, b, c):.6f} y {getRaiz2(a, b, c):.5f}")
elif discriminante == 0:
    print(f"La ecuación tiene una raíz {getRaiz1(a, b, c):.0f}")
else:
    print("La ecuación no tiene raíces reales")