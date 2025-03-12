public class Cola {
	// atributos
	private long[] arreglo;
	private int inicio;
	private int fin;
	private int nroElementos;
	private int n;
	
	// métodos
	public Cola(int n) { // constructor
		this.n = n;
		arreglo = new long[n];
		inicio = 0;
		fin = -1;
		nroElementos = 0;
	}
	public void insert(long e) { // inserta un elemento al final de la Cola
		if (!isFull()) {
			if (fin == this.n - 1) // consulta para reiniciar
				fin = -1;
			fin++;            // incrementa fin
			arreglo[fin] = e; //  adiciona
			nroElementos++;   // un elemento mas
		} else 
			System.out.println("Cola llena.");
	}
	public long remove() { // elimina un elemento del principio de la Cola
		long e = Long.MIN_VALUE;
		if (!isEmpty()) {
			e = arreglo[inicio]; // obtiene el valor 
			inicio++;                // incrementa inicio
			if (inicio == this.n)    // consulta para reiniciar
				inicio = 0;
			nroElementos--;          // un elemento menos
		} else
			System.out.println("Cola vacía.");
		return e;
	}
	public long peek() { // obtiene el elemento del inicio de la Cola
		long e = Long.MIN_VALUE;
		if (!isEmpty())
			e = arreglo[inicio]; // obtiene el valor 
		else
			System.out.println("Cola vacía.");
		return e;
	}
	public boolean isEmpty() { // verdad si la Cola esta vacía
		return (nroElementos == 0);
	}
	public boolean isFull() { // verdad si la Cola esta llena
		return (nroElementos == this.n);
	}
	public int size() { // número de elementos de la Cola
		return nroElementos;
	}
}
