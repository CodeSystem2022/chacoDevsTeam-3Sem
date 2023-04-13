package ar.com.system2023.mundopc;

public class Monitor {
    private static int contadorMonitor;
    private final int idMonitor;
    private String marca;
    private String tamaño;

    private Monitor() {
        this.idMonitor = ++Monitor.contadorMonitor;
    }

    public Monitor(String marca, String tamaño) {
        this();
        this.marca = marca;
        this.tamaño = tamaño;
    }

    public String getMarca() {
        return this.marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getTamaño() {
        return this.tamaño;
    }

    public void setTamaño(String tamaño) {
        this.tamaño = tamaño;
    }

    public int getIdMonitor() {
        return this.getIdMonitor();
    }

    @Override

    public String toString() {
        return "Monitor{" + "contadorMonitor=" + contadorMonitor + ", idMonitor=" + idMonitor + ", marca=" + marca + ", tama\u00f1o=" + tamaño + '}';
    }
}