class Artista:
    def __init__(self, nombre, ci, años_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.años_experiencia = años_experiencia

class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
class Obra:
    def __init__(self, titulo, material, datos_artistas, anuncio=None):
        self.titulo = titulo
        self.material = material
        self.artistas = [Artista(nombre, ci, exp) for nombre, ci, exp in datos_artistas]
        self.anuncio = anuncio

class Pintura(Obra):
    def __init__(self, titulo, material, datos_artistas, genero, anuncio=None):
        super().__init__(titulo, material, datos_artistas, anuncio)
        self.genero = genero

anuncio1 = Anuncio(101, 3500)

datos1 = [("Luis", "123", 10), ("Maria", "456", 5)]
datos2 = [("Ana", "789", 12)]

pintura1 = Pintura("Amanecer", "Óleo", datos1, "Realismo", anuncio1)

pintura2 = Pintura("Atardecer", "Acrílico", datos2, "Impresionismo")

def artista_mas_experto(p1, p2):
    todos = p1.artistas + p2.artistas
    experto = max(todos, key=lambda a: a.años_experiencia)
    return experto.nombre

print("Artista con más experiencia:", artista_mas_experto(pintura1, pintura2))

pintura2.anuncio = Anuncio(102, 4000)

def total_venta(p1, p2):
    total = 0
    if p1.anuncio:
        total += p1.anuncio.precio
    if p2.anuncio:
        total += p2.anuncio.precio
    return total

print("Monto total de venta:", total_venta(pintura1, pintura2))