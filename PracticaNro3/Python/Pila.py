class Pila:
    def __init__(self):
        self.arreglo = []
        
    def push(self,e):
        self.arreglo.append(e)
        
    def pop(self):
        e = -1
        if not self.isEmpty():
            e = self.arreglo.pop()
        else:
            print("Pila vacía.")
      
        return e

    def peek(self):
        e = -1
        if not self.isEmpty():
            n = len(self.arreglo)
            e = self.arreglo[n-1]
        else:
            print("Pila vacía.")

        return e
    
    def isEmpty(self):
        return len(self.arreglo) == 0

pila = Pila()

# Insertar elementos en la pila
pila.push(100)
pila.push(200)
pila.push(300)
pila.push(400)
pila.push(500)

print("Elemento en la cima:", pila.peek())  # Debería imprimir 500

# Remover elementos de la pila
print("Elemento removido:", pila.pop())  # 500
print("Elemento removido:", pila.pop())  # 400
print("Elemento removido:", pila.pop())  # 300
print("Elemento removido:", pila.pop())  # 200
print("Elemento removido:", pila.pop())  # 100

# Intentar remover cuando la pila está vacía
print("Elemento removido:", pila.pop())  # Debería imprimir "Pila vacía." y retornar -1
