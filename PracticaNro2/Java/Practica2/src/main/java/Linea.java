import javax.swing.*;  
import java.awt.*;  

public class Linea extends JPanel {  
    public Punto p1, p2;  

    public Linea(Punto p1, Punto p2) {  
        this.p1 = p1;  
        this.p2 = p2;  
        setPreferredSize(new Dimension(400, 400));  
    }  

    @Override  
    public String toString() {  
        return "Línea de " + p1 + " a " + p2;  
    }  

    public void dibujaLinea() {  
        JFrame frame = new JFrame("Dibujar Línea");  
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  
        frame.add(this);  
        frame.pack();  
        frame.setVisible(true);  
    }  

    protected void paintComponent(Graphics g) {  
        super.paintComponent(g);  
        g.setColor(Color.BLUE);  
        g.drawLine((int) p1.x * 10, (int) p1.y * 10, (int) p2.x * 10, (int) p2.y * 10);  
    }  
}
