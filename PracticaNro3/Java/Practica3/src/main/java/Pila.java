public class Pila {
	// atributos
	private int n; // tamaño de la pila
	private long[] arreglo;
	private int top; // cima o parte superior de la pila
	
	// métodos
	public Pila(int n) { // constructor
		this.n = n; // asigna el tamaño del arreglo
		arreglo = new long[n]; // crea arreglo
		top = -1; // todavia no tiene elementos
	}
	public void push(long e) { // inserta un elemento en la cima de la pila
		if (!isFull()) {
			top++;            // incrementa top
			arreglo[top] = e; // inserta elemento
		} else
			System.out.println("Pila llena.");
	}
	public long pop() { // elimina un elemento de la cima de la pila
		long e = Long.MIN_VALUE;
		if (!isEmpty()){
			e = arreglo[top]; // retorna el elemento
			top--;            // decrementa top
		} else
			System.out.println("Pila vacía.");
		return e;
	}
	public long peek() { // obtiene el elemento de la cima de la pila
		long e = Long.MIN_VALUE;
		if (!isEmpty()){
			e = arreglo[top]; // retorna el elemento
		} else
			System.out.println("Pila vacía.");
		return e;
	}
	public boolean isEmpty() { // verdad si la pila está vacía
		return (top == -1);
	}
	public boolean isFull() { // verdad si la pila está llena
		return (top == this.n - 1);
	}
}
