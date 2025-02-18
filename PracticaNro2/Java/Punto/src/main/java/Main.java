public class Main {
    public static void main(String[] args) {
        Punto p1 = new Punto(0, 3);
        Punto p2 = new Punto(4, 5);

        // Prueba Punto
        System.out.println("Punto p1: " + p1);
        float a[] = p1.coord_cartesianas();
        System.out.println("Cartesianas: " + a[0] + " " + a[1]);
        float b[] = p1.coord_polares();
        System.out.println("Polares: " + b[0] + " " + b[1]);

        // Prueba Linea
        Linea linea = new Linea(p1, p2);
        System.out.println(linea);

        // Prueba Circulo
        Circulo circulo = new Circulo(p1, 3);
        System.out.println(circulo);
    } 
}