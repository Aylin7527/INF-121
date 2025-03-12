public class Main {
    public static void main(String[] args) {
        Cola cola = new Cola(5); 

        cola.insert(10);
        cola.insert(20);
        cola.insert(30);
        cola.insert(40);
        cola.insert(50);        
        
        cola.insert(60);
        
        System.out.println("Primer elemento: " + cola.peek());

        
        System.out.println("Elemento removido: " + cola.remove());
        System.out.println("Elemento removido: " + cola.remove());

        
        cola.insert(60);
        cola.insert(70);

        
        while (!cola.isEmpty()) {
            System.out.println("Elemento removido: " + cola.remove());
        }   
        cola.remove();
        
        
        System.out.println("\n=== Prueba de la Pila ===");
        Pila pila = new Pila(5); 

        pila.push(100);
        pila.push(200);
        pila.push(300);
        pila.push(400);
        pila.push(500);
        pila.push(600); 

        System.out.println("Elemento en la cima: " + pila.peek());

        while (!pila.isEmpty()) {
            System.out.println("Elemento removido: " + pila.pop());
        }

        pila.pop(); 
    }
}
