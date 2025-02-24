import javax.swing.*;  
import java.awt.*;  

public class Circulo extends JPanel {  
    public Punto centro;  
    public float radio;  

    public Circulo(Punto centro, float radio) {  
        this.centro = centro;  
        this.radio = radio;  
        setPreferredSize(new Dimension(400, 400));  
    }  

    @Override  
    public String toString() {  
        return "Círculo con centro en " + centro + " y radio " + radio;  
    }  

    public void dibujaCirculo() {  
        JFrame frame = new JFrame("Dibujar Círculo");  
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  
        frame.add(this);  
        frame.pack();  
        frame.setVisible(true);  
    }  

    protected void paintComponent(Graphics g) {  
        super.paintComponent(g);  
        g.setColor(Color.RED);  
        g.drawOval((int) (centro.x - radio) * 10, (int) (centro.y - radio) * 10, (int) (2 * radio * 10), (int) (2 * radio * 10));  
    }  
}
