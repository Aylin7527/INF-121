import math
class Vector3D:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def __str__(self):
        return f"({self.a1:.2f}, {self.a2:.2f}, {self.a3:.2f})"

    def __add__(self, other):
        return Vector3D(self.a1 + other.a1, self.a2 + other.a2, self.a3 + other.a3)

    def __mul__(self, scalar):
        return Vector3D(self.a1 * scalar, self.a2 * scalar, self.a3 * scalar)

    def norma(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)

    def normal(self):
        norma = self.norma()
        return Vector3D(self.a1 / norma, self.a2 / norma, self.a3 / norma)

    def producto_escalar(self, other):
        return self.a1 * other.a1 + self.a2 * other.a2 + self.a3 * other.a3

    def producto_vectorial(self, other):
        c1 = self.a2 * other.a3 - self.a3 * other.a2
        c2 = self.a3 * other.a1 - self.a1 * other.a3
        c3 = self.a1 * other.a2 - self.a2 * other.a1
        return Vector3D(c1, c2, c3)

    def proyeccion_a_sobre_b(self):
        b_norm_sq = sum(i**2 for i in self.b)
        if b_norm_sq == 0:
            return "No se puede proyectar sobre un vector nulo"
        factor = self.producto_punto() / b_norm_sq
        return [factor * i for i in self.b]
    
    def es_perpendicular(self, other):
        return self.producto_escalar(other) == 0

a_v = list(map(float, input("Ingrese los valores del vector A separados por espacios: ").split()))
b_v = list(map(float, input("Ingrese los valores del vector A separados por espacios: ").split()))
a1 = Vector3D(*a_v)
b1 = Vector3D(*b_v)

print("Vector A:", a1)
print("Vector B:", b1)

suma = a1 + b1
print("Suma de A y B:", suma)

escalar = 3
producto_escalar = a1 * escalar
print(f"Producto de A por {escalar}:", producto_escalar)

longitud_a = a1.norma()
print(f"Longitud de A: {longitud_a:.2f}")

normal_a = a1.normal()
print("Normalización de A:", normal_a)

escalar_producto = a1.producto_escalar(b1)
print("Producto escalar A · B:", escalar_producto)

producto_vectorial = a1.producto_vectorial(b1)
print("Producto vectorial A × B:", producto_vectorial)
proyeccion_a_sobre_b = a1.proyeccion_a_sobre_b(b1)
print(f"Proyección de A sobre B: {[f'{valor:.2f}' for valor in proyeccion_a_sobre_b()]}")

es_ortogonal = a1.es_perpendicular(b1)
print("¿Son A y B ortogonales?", es_ortogonal)
