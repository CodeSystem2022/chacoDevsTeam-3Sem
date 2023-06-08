import java.util.Scanner;

public class CalculadoraUTN {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("******* Aplicacion Calculadora *******");
        System.out.print("Digite el valor para el operano1: ");
        var operando1 = Integer.parseInt(entrada.nextLine());
        System.out.print("Digite el valor para el operano2: ");
        var operando2 = Integer.parseInt(entrada.nextLine());
        var resutado = operando1 + operando2;
        System.out.println("resultado = " + resutado);
    }
}
