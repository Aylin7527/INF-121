import random
class Juego:
    def __init__(self, numeroDeVidas, record=0):
        self.numeroDeVidas = numeroDeVidas
        self.record = record
    
    def reiniciaPartida(self):
        self.numeroDeVidas = 3
    
    def actualizaRecord(self):
        self.record += 1
    
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = random.randint(0, 10)
    
    def validaNumero(self, numero):
        return 0 <= numero <= 10
    
    def juega(self):
        self.reiniciaPartida()
        print("Adivina un número entre 0 y 10")
        while self.numeroDeVidas > 0:
            try:
                numeroIngresado = int(input("Ingresa un número: "))
                if not self.validaNumero(numeroIngresado):
                    print("Número fuera de rango. Inténtalo de nuevo.")
                    continue
                
                if numeroIngresado == self.numeroAAdivinar:
                    print("¡Acertaste!")
                    self.actualizaRecord()
                    return
                else:
                    self.quitaVida()
                    if self.numeroDeVidas > 0:
                        pista = "mayor" if numeroIngresado < self.numeroAAdivinar else "menor"
                        print(f"Incorrecto. El número es {pista}. Intentos restantes: {self.numeroDeVidas}")
            except ValueError:
                print("Entrada inválida. Ingresa un número entero.")
        print("Se acabaron los intentos. El número era:", self.numeroAAdivinar)

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def juega(self):
        while True:
            self.numeroAAdivinar = random.randint(0, 10)
            if self.numeroAAdivinar % 2 == 0:
                break  
        super().juega()

    def validaNumero(self, numero):
        if numero % 2 == 0 and 0 <= numero <= 10:
            return True
        print("Error: Debes ingresar un número par entre 0 y 10.")
        return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def juega(self):
        while True:
            self.numeroAAdivinar = random.randint(0, 10)
            if self.numeroAAdivinar % 2 != 0:
                break  
        super().juega()

    def validaNumero(self, numero):
        if numero % 2 != 0 and 0 <= numero <= 10:
            return True
        print("Error: Debes ingresar un número impar entre 0 y 10.")
        return False

class Aplicacion:
    @staticmethod
    def main():
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)
        
        print("\n--- Juego Adivina Número ---")
        juego1.juega()
        print("\n--- Juego Adivina Número Par ---")
        juego2.juega()
        print("\n--- Juego Adivina Número Impar ---")
        juego3.juega()

if __name__ == "__main__":
    Aplicacion.main()