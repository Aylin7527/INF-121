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

pila.push(100)
pila.push(200)
pila.push(300)
pila.push(400)
pila.push(500)

print("Elemento en la cima:", pila.peek()) 

print("Elemento removido:", pila.pop())  
print("Elemento removido:", pila.pop())  
print("Elemento removido:", pila.pop())  
print("Elemento removido:", pila.pop())  
print("Elemento removido:", pila.pop())  

print("Elemento removido:", pila.pop())  
