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
    def __init__(self, titulo, material, datos_artistas, anuncio):
        self.titulo = titulo
        self.material = material
        self.artistas = [Artista(nombre, ci, exp) for nombre, ci, exp in datos_artistas]
        self.anuncio = anuncio

class Pintura(Obra):
    def __init__(self, titulo, material, datos_artistas, genero, anuncio):
        super().__init__(titulo, material, datos_artistas, anuncio)
        self.genero = genero

anuncio1 = Anuncio(101, 3500)
anuncio2 = Anuncio(102, 4000)

datos1 = [("Luis", "123", 10), ("Maria", "456", 5)]
datos2 = [("Ana", "789", 12)]

pintura1 = Pintura("Amanecer", "Óleo", datos1, "Realismo", anuncio1)
pintura2 = Pintura("Atardecer", "Acrílico", datos2, "Impresionismo", anuncio2)

def promedio_experiencia(p1, p2):
    todos = p1.artistas + p2.artistas
    total_exp = sum(a.años_experiencia for a in todos)
    promedio = total_exp / len(todos)
    return promedio

print("Promedio años de experiencia:", int(promedio_experiencia(pintura1, pintura2)))

def incrementar_precio_por_artista(p1, p2, nombre_artista, incremento):
    for pintura in [p1, p2]:
        if any(art.nombre == nombre_artista for art in pintura.artistas):
            if pintura.anuncio:
                pintura.anuncio.precio += incremento
                return f"Precio incrementado en {incremento} para la pintura '{pintura.titulo}'"
    return "Artista no encontrado en ninguna pintura"

print(incrementar_precio_por_artista(pintura1, pintura2, "Luis", 500))
print("Precio nuevo pintura1:", pintura1.anuncio.precio)
