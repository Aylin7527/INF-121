import random
class Juego:
    def __init__(self, numeroDeVidas, record): 
        self.numeroDeVidas = numeroDeVidas
        self.record = record

    def reiniciaPartida(self):
        self.numeroDeVidas = 3 
        print("La partida se ha reiniciado.")

    def actualizaRecord(self, intentos):
        if intentos < self.record or self.record == 0:
            self.record = intentos
            print(f"¡Nuevo récord! Número de intentos: {self.record}")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f"Te quedan {self.numeroDeVidas} vidas.")
            return True
        else:
            print("¡Te has quedado sin vidas! Fin del juego.")
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas=3, record=0):
        super().__init__(numeroDeVidas, record)
        self.numeroAAdivinar = random.randint(0, 10) 

    def juega(self):
        self.reiniciaPartida()
        intentos = 0

        while self.numeroDeVidas > 0:
            try:
                numero_usuario = int(input("Adivina un número entre 0 y 10: "))
                intentos += 1

                if numero_usuario == self.numeroAAdivinar:
                    print("¡Acertaste!")
                    self.actualizaRecord(intentos)
                    break
                else:
                    print("Número incorrecto.")
                    if self.quitaVida():
                        if numero_usuario < self.numeroAAdivinar:
                            print("El número a adivinar es mayor.")
                        else:
                            print("El número a adivinar es menor.")
                    else:
                        print(f"El número correcto era: {self.numeroAAdivinar}")
            except ValueError:
                print("Por favor, ingresa un número válido.")

class Aplicacion:
    def main(self):
        juego = JuegoAdivinaNumero()
        print("\n--- Juego Adivina Número ---")
        juego.juega()

if __name__ == "__main__":
    app = Aplicacion()
    app.main()
