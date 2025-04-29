from multimethod import multimethod
import math

class AlgebraVectorial:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def norma(self, v):
        suma = sum(i**2 for i in v)
        return math.sqrt(suma)

    def producto_punto(self):
        return sum(self.a[i] * self.b[i] for i in range(len(self.a)))

    @multimethod
    def es_perpendicular(self, tipo: int):
        if tipo == 1:
            return self.norma([self.a[i] + self.b[i] for i in range(len(self.a))]) == \
                   self.norma([self.a[i] - self.b[i] for i in range(len(self.a))])
        elif tipo == 2:
            return self.norma([self.a[i] - self.b[i] for i in range(len(self.a))]) == \
                   self.norma([self.b[i] - self.a[i] for i in range(len(self.a))])
        elif tipo == 3:
            return self.producto_punto() == 0
        elif tipo == 4:
            return self.norma([self.a[i] + self.b[i] for i in range(len(self.a))])**2 == \
                   self.norma(self.a)**2 + self.norma(self.b)**2
        return False

    @multimethod
    def es_paralelo(self, tipo: int):
        if tipo == 1:
            r0 = None
            for i in range(len(self.a)):
                if self.b[i] != 0:
                    r = self.a[i] / self.b[i]
                    if r0 is None:
                        r0 = r
                    elif r != r0:
                        return False
            return True
        elif tipo == 2:
            return all(self.a[i] * self.b[i] == 0 for i in range(len(self.a)))
        return False

    def proyeccion_a_sobre_b(self):
        b_norm_sq = sum(i**2 for i in self.b)
        if b_norm_sq == 0:
            return "No se puede proyectar sobre un vector nulo"
        factor = self.producto_punto() / b_norm_sq
        return [factor * i for i in self.b]

    def componente_a_en_b(self):
        b_norm = self.norma(self.b)
        if b_norm == 0:
            return "No se puede calcular componente sobre un vector nulo"
        return self.producto_punto() / b_norm

a = list(map(float, input("Ingrese los valores del vector A separados por espacios: ").split()))
b = list(map(float, input("Ingrese los valores del vector B separados por espacios: ").split()))

algebra = AlgebraVectorial(a, b)

print("\n--- RESULTADOS ---")
print("Perpendicular (|a+b| = |a-b|):", algebra.es_perpendicular(1))
print("Perpendicular (|a-b| = |b-a|):", algebra.es_perpendicular(2))
print("Perpendicular (a · b = 0):", algebra.es_perpendicular(3))
print("Perpendicular (|a+b|² = |a|² + |b|²):", algebra.es_perpendicular(4))
print("Paralelo (a = r * b):", algebra.es_paralelo(1))
print("Paralelo (a × b = 0):", algebra.es_paralelo(2))
print(f"Proyección de A sobre B: {[f'{valor:.2f}' for valor in algebra.proyeccion_a_sobre_b()]}")
print(f"Componente de A en la dirección de B: {algebra.componente_a_en_b():.2f}")
