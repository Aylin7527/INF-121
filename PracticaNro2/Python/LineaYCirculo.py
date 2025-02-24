import math
import pygame
import multiprocessing

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        radio = math.sqrt(self.x ** 2 + self.y ** 2)
        angulo = math.degrees(math.atan2(self.y, self.x))
        return radio, angulo

    def __str__(self):
        return "({:.2f}, {:.2f})".format(self.x, self.y)

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def longitud(self):
        return math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    def __str__(self):
        return "{} -> {}, Longitud: {:.2f}".format(self.p1, self.p2, self.longitud())

    def dibujaLinea(self, screen):
        pygame.draw.line(screen, (255, 0, 0), (int(self.p1.x), int(self.p1.y)), (int(self.p2.x), int(self.p2.y)), 2)

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return "Centro {}, Radio: {:.2f}, Área: {:.2f}, Perímetro: {:.2f}".format(self.centro, self.radio, self.area(), self.perimetro())

    def dibujaCirculo(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.centro.x), int(self.centro.y)), int(self.radio), 2)

def ventana_linea():
    pygame.init()
    WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ventana - Línea")

    p1 = Punto(100, 300)
    p2 = Punto(400, 200)
    linea = Linea(p1, p2)

    running = True
    while running:
        screen.fill((255, 255, 255))
        linea.dibujaLinea(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

def ventana_circulo():
    pygame.init()
    WIDTH, HEIGHT = 500, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ventana - Círculo")

    circulo = Circulo(Punto(250, 250), 100)

    running = True
    while running:
        screen.fill((255, 255, 255))
        circulo.dibujaCirculo(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":

    proceso_linea = multiprocessing.Process(target=ventana_linea)
    proceso_circulo = multiprocessing.Process(target=ventana_circulo)

    proceso_linea.start()
    proceso_circulo.start()

    proceso_linea.join()
    proceso_circulo.join()
