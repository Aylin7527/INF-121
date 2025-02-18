public class Circulo {
    public Punto centro;
    public float radio;

    public Circulo(Punto centro, float radio) {
        this.centro = centro;
        this.radio = radio;
    }

    public double area() {
        return Math.PI * radio * radio;
    }

    public double perimetro() {
        return 2 * Math.PI * radio;
    }

    @Override
    public String toString() {
        return String.format("Circulo: Centro %s, Radio: %.2f, Area: %.2f, Perimetro: %.2f", 
                centro, radio, area(), perimetro());
    }
}