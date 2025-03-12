package polimorfismo;
public class FiguraGeometrica {
    
    double area(double radio) {
        return Math.PI * radio * radio;
    }
    
    double area(int base, int altura) {
        return base * altura;
    }
    
    double area(double base, double altura, boolean esTriangulo) {
        if (esTriangulo) {
            return (base * altura) / 2;
        }
        return base * altura; // Si no es triángulo, calcula rectángulo
    }
    
    double area(double baseMayor, double baseMenor, double altura) {
        return ((baseMayor + baseMenor) * altura) / 2;
    }

    double area(int lado) {
        double apotema = lado / (2 * Math.tan(Math.PI / 5));
        return (5 * lado * apotema) / 2;
    }

    public static void main(String[] args) {
        FiguraGeometrica f1 = new FiguraGeometrica();
        FiguraGeometrica f2 = new FiguraGeometrica();
        FiguraGeometrica f3 = new FiguraGeometrica();
        FiguraGeometrica f4 = new FiguraGeometrica();
        FiguraGeometrica f5 = new FiguraGeometrica();
    
        System.out.println("Área del Círculo: " + f1.area(1.0)); // Radio = 1
        System.out.println("Área del Rectángulo: " + f2.area(2, 3)); // Base = 2, Altura = 3 
        System.out.println("Área del Triángulo Rectángulo: " + f3.area(3, 4, true)); // Base = 3, Altura = 4 
        System.out.println("Área del Trapecio: " + f4.area(5, 7, 4)); // Base Mayor = 5, Base Menor = 7, Altura = 4
        System.out.println("Área del Pentágono: " + f5.area(6)); // Lado = 6
    }
}
