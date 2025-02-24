public class Main {
    public static void main(String[] args) { 
        Punto p1 = new Punto(0,3); 
        System.out.println("Punto: " + p1); 
        float a[] = p1.coord_cartesianas(); 
        System.out.println("Cartesianas: " + a[0] + " " + a[1]); 
        float b[] = p1.coord_polares(); 
        System.out.println("Polares: " + b[0] + " " + b[1]); 
    } 
}
