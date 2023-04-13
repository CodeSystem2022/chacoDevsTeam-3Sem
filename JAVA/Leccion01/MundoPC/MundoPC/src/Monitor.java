public class Monitor {
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
