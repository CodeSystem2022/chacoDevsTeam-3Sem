package ar.com.system2023.mundopc;

public class ClaseMonitor {
    public class Contador {
        private int valor = 0;

        public synchronized void incrementar() {
            valor++;
        }

        public synchronized void decrementar() {
            valor--;
        }

        public synchronized int getValor() {
            return valor;
        }
    }
}

