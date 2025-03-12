class Cola:
    def __init__(self, n):
        self.n = n
        self.arreglo = [0] * n
        self.inicio = 0
        self.fin = -1
        self.nroElementos = 0
        
    def insert(self,e):
        if not self.isFull():
            if self.fin == self.n - 1:
                self.fin = -1
            self.fin = self.fin + 1
            self.arreglo[self.fin] = e
            self.nroElementos = self.nroElementos + 1
        else: 
            print("Cola llena.");        
        
    def remove(self):
        e = -1
        if not self.isEmpty():
            e = self.arreglo[self.inicio]
            self.inicio = self.inicio + 1 
            if self.inicio == self.n:
                self.inicio = 0
            self.nroElementos = self.nroElementos - 1
        else:
            print("Cola vacía.")
      
        return e

    def peek(self):
        e = -1
        if not self.isEmpty():
            e = self.arreglo[self.inicio]
        else:
            print("Cola vacía.")

        return e
    
    def isEmpty(self):
        return self.nroElementos == 0

    def isFull(self):
        return self.nroElementos == self.n

    def size(self):
        return self.nroElementos

cola = Cola(5)

cola.insert(10)
cola.insert(20)
cola.insert(30)
cola.insert(40)
cola.insert(50)
cola.insert(60)  # Aquí debería mostrar "Cola llena."

print(f"Primer elemento: {cola.peek()}")

while not cola.isEmpty():
    print(f"Elemento removido: {cola.remove()}")

print(f"Elemento removido: {cola.remove()}")  # Aquí debería mostrar "Cola vacía."
