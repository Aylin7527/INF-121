package teatroMunicipal;

import java.awt.*;
import javax.swing.*;
import javax.swing.border.*;

public class TeatroMunicipal extends JFrame {
    private JTextField txtNumero;
    private JTextField txtDias;
    private JLabel lblResultado;
    private JLabel lblDias;
    private JRadioButton rdbPalco, rdbPlatea, rdbGaleria;
    private ButtonGroup grupo;

    public TeatroMunicipal() {
        getContentPane().setBackground(new Color(255, 255, 255));
        setTitle("Teatro Municipal");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 510, 360);
        getContentPane().setLayout(null);

        JLabel lblTitulo = new JLabel("Teatro Municipal", SwingConstants.CENTER);
        lblTitulo.setBackground(new Color(255, 255, 255));
        lblTitulo.setForeground(new Color(0, 0, 160));
        lblTitulo.setFont(new Font("Tahoma", Font.BOLD, 20));
        lblTitulo.setBounds(53, 21, 350, 40);
        getContentPane().add(lblTitulo);

        ImageIcon originalIcon = null;
        try {
            originalIcon = new ImageIcon(getClass().getResource("/teatroMunicipal/TM.jpg"));
            Image imagenEscalada = originalIcon.getImage().getScaledInstance(92, 57, Image.SCALE_SMOOTH);
            originalIcon = new ImageIcon(imagenEscalada);
        } catch (Exception e) {
            System.out.println("Imagen no encontrada.");
        }

        JLabel lblImagen = new JLabel(originalIcon);
        lblImagen.setBounds(370, 10, 92, 57);
        getContentPane().add(lblImagen);

        TitledBorder borde = new TitledBorder(new EtchedBorder(), "Datos del Boleto");
        borde.setTitleColor(new Color(0, 0, 128));
        JPanel panelDatos = new JPanel();
        panelDatos.setBorder(borde);
        panelDatos.setBounds(10, 70, 470, 164);
        panelDatos.setLayout(null);
        getContentPane().add(panelDatos);

        rdbPalco = new JRadioButton("Palco");
        rdbPalco.setFont(new Font("Tahoma", Font.PLAIN, 11));
        rdbPalco.setBounds(42, 20, 70, 20);
        panelDatos.add(rdbPalco);

        rdbPlatea = new JRadioButton("Platea");
        rdbPlatea.setFont(new Font("Tahoma", Font.PLAIN, 11));
        rdbPlatea.setBounds(184, 20, 70, 20);
        panelDatos.add(rdbPlatea);

        rdbGaleria = new JRadioButton("Galeria");
        rdbGaleria.setFont(new Font("Tahoma", Font.PLAIN, 11));
        rdbGaleria.setBounds(325, 20, 80, 20);
        panelDatos.add(rdbGaleria);

        grupo = new ButtonGroup();
        grupo.add(rdbPalco);
        grupo.add(rdbPlatea);
        grupo.add(rdbGaleria);

        JLabel lblNumero = new JLabel("Número:");
        lblNumero.setForeground(new Color(0, 0, 128));
        lblNumero.setFont(new Font("Tahoma", Font.PLAIN, 11));
        lblNumero.setBounds(21, 51, 80, 20);
        panelDatos.add(lblNumero);

        txtNumero = new JTextField("");
        txtNumero.setBounds(180, 51, 90, 22);
        panelDatos.add(txtNumero);

        lblDias = new JLabel("Cant. Días para el Evento:");
        lblDias.setForeground(new Color(0, 0, 128));
        lblDias.setFont(new Font("Tahoma", Font.PLAIN, 11));
        lblDias.setBounds(20, 93, 180, 20);
        panelDatos.add(lblDias);

        txtDias = new JTextField();
        txtDias.setBounds(180, 93, 90, 22);
        panelDatos.add(txtDias);

        JButton btnVende = new JButton("Vende");
        btnVende.setBounds(99, 129, 90, 25);
        panelDatos.add(btnVende);

        JButton btnSalir = new JButton("Salir");
        btnSalir.setBounds(255, 129, 90, 25);
        panelDatos.add(btnSalir);

        TitledBorder bordeInfo = new TitledBorder(new EtchedBorder(), "Información");
        bordeInfo.setTitleColor(new Color(0, 0, 128));
        JPanel panelInfo = new JPanel();
        panelInfo.setBorder(bordeInfo);
        panelInfo.setBounds(10, 244, 470, 69);
        panelInfo.setLayout(null);
        getContentPane().add(panelInfo);

        lblResultado = new JLabel("Número: 1, Precio: 100.0");
        lblResultado.setForeground(new Color(0, 64, 128));
        lblResultado.setBackground(new Color(240, 240, 240));
        lblResultado.setFont(new Font("Segoe UI", Font.BOLD, 20));
        lblResultado.setBounds(99, 10, 327, 49);
        panelInfo.add(lblResultado);

        rdbPalco.addActionListener(e -> {
            txtDias.setText("");
            txtDias.setEnabled(false);
            lblDias.setEnabled(false);
        });

        rdbPlatea.addActionListener(e -> {
            txtDias.setEnabled(true);
            lblDias.setEnabled(true);
        });

        rdbGaleria.addActionListener(e -> {
            txtDias.setEnabled(true);
            lblDias.setEnabled(true);
        });

        btnSalir.addActionListener(e -> System.exit(0));

        btnVende.addActionListener(e -> {
            try {
                int numero = Integer.parseInt(txtNumero.getText());
                int dias = 0;
                Boleto boleto = null;

                if (rdbPalco.isSelected()) {
                    boleto = new Palco(numero);
                } else if (rdbPlatea.isSelected()) {
                    dias = Integer.parseInt(txtDias.getText());
                    boleto = new Platea(numero, dias);
                } else if (rdbGaleria.isSelected()) {
                    dias = Integer.parseInt(txtDias.getText());
                    boleto = new Galeria(numero, dias);
                } else {
                    lblResultado.setText("Numero: 1, Precio: 100.0");
                    return;
                }

                lblResultado.setText(boleto.toString());
            } catch (NumberFormatException ex) {
                lblResultado.setText("Error: Ingrese números válidos.");
            }
        });

        txtDias.setEnabled(false);
        lblDias.setEnabled(false);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new TeatroMunicipal().setVisible(true);
        });
    }
}


abstract class Boleto {
    private int numero;
    private double precio;

    public Boleto(int numero) {
        this.numero = numero;
    }

    protected void setPrecio(double precio) {
        this.precio = precio;
    }

    protected int getNumero() {
        return numero;
    }

    protected double getPrecio() {
        return precio;
    }

    @Override
    public String toString() {
        return "Número: " + numero + ", Precio: " + precio;
    }
}

class Palco extends Boleto {

    public Palco(int numero) {
        super(numero);
        setPrecio(100.0);
    }

    @Override
    public String toString() {
        return "Número: " + getNumero() + ", Precio: " + getPrecio();
    }
}

class Platea extends Boleto {

    public Platea(int numero, int diasAnticipacion) {
        super(numero);
        if (diasAnticipacion >= 10) {
            setPrecio(50.0);
        } else {
            setPrecio(60.0);
        }
    }

    @Override
    public String toString() {
        return "Número: " + getNumero() + ", Precio: " + getPrecio();
    }
}

class Galeria extends Platea {

    public Galeria(int numero, int diasAnticipacion) {
        super(numero, diasAnticipacion);
        if (diasAnticipacion >= 10) {
            setPrecio(25.0);
        } else {
            setPrecio(30.0);
        }
    }

    @Override
    public String toString() {
        return "Número: " + getNumero() + ", Precio: " + getPrecio();
    }
}

