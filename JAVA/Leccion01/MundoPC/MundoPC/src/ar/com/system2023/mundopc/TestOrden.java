package ar.com.system2023.mundopc;


public class TestOrden {
    public static void main(String[] args) {

Monitor monitor1 = new Monitor("LG","15 pulgadas");
Raton raton1 = new Raton("GENIUS","USBC");
Teclado teclado1= new Teclado("Genius","USBC");
Computadora computadora1= new Computadora("HP",monitor1,teclado1,raton1);
Orden orden1= new Orden();

Monitor monitor2 = new Monitor("HP Super","20 pulgadas");
Raton raton2 = new Raton("GENIUS Super","USBA");
Teclado teclado2= new Teclado("Genius Super","USBA");
Computadora computadora2= new Computadora("HP Super",monitor2,teclado2,raton2);

orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);


orden1.mostrarOrden();
    }
}