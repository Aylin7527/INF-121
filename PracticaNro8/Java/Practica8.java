package Practicas;

public class Practica8 {
    public static class A {
        int x, z;
        public A(int x, int z) {
            this.x = x; this.z = z;
        }
        public void incrementaXZ() { x++; z++; }
        public void incrementaZ() { z++; }
    }

    public static class B {
        int y, z;
        public B(int y, int z) {
            this.y = y; this.z = z;
        }
        public void incrementaYZ() { y++; z++; }
        public void incrementaZ() { z++; }
    }

    public static class D {
        A a;
        B b;

        public D(int x, int y, int z) {
            a = new A(x, z);
            b = new B(y, z);
        }

        public void incrementaXYZ() {
            a.x++; b.y++; a.z++; b.z++;
        }

        public void printEstado() {
            System.out.println("x = " + a.x + ", y = " + b.y + ", z_A = " + a.z + ", z_B = " + b.z);
        }
    }

    public static void main(String[] args) {
        D d = new D(1, 2, 3);
        System.out.println("Original:");
        d.printEstado();
        d.incrementaXYZ();
        System.out.println("Después de incrementaXYZ:");
        d.printEstado();
    }
}
