public class Main {  
    public static void main(String[] args) {  
        Punto p1 = new Punto(5, 5);  
        Punto p2 = new Punto(10, 10);  
        Linea linea = new Linea(p1, p2);  
        System.out.println(linea);  
        linea.dibujaLinea();  

        Punto centro = new Punto(8, 8);  
        float radio = 3;  
        Circulo circulo = new Circulo(centro, radio);  
        System.out.println(circulo);  
        circulo.dibujaCirculo();  
    }  
}
