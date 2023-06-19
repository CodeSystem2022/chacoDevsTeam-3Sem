import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class ListadoPersonasApp {

    public static void main(String[] args) {
        System.out.println("Hello world!");
        Scanner entrada = new Scanner(System.in);
        //Definimos la lista fuera del ciclo while
        List<Persona> personas = new ArrayList<>();
        //Empezamos con el menu
        var salir = false;
        while (!salir) {
            mostrarMenu();
            try {
                salir = ejecutarOperacion(entrada, personas);
            } catch (Exception e) {
                System.out.println("Ocurrio un Error: " + e.getMessage());
            }
            System.out.println();
        }//Fin del ciclo while

    }//Fin metodod main

    private static void mostrarMenu() {
        //mostramos las opciones
        System.out.print("""
                         ******* Listado de Personas *******
                         1. Agregar 
                         2. Listar
                         3. Salir
                           """);
        System.out.print("Digite una de las opciones: ");
    }//Fin metodo mostrarMenu

    private static bollean ejecutarOperacion(Scanner entrada, List<Persona> personas) {
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        // revisamos la opcion digitada a travez de un Switch
        switch (opcion) {
            case 1 -> {//agregar una persona a la lista
                System.out.print("Digite el nombre: ");
                var nombre = entrada.nextLine();
                System.out.print("Digite el telefono: ");
                var tel = entrada.nextLine();
                System.out.print("Digite el Correo");
                var email = entrada.nextLine();
                // creammos el objeto persona
                var persona = new Persona(nombre, tel, email);
                //Agregamos la persona a la lista
                personas.add(persona);
                System.out.println("La Lista tiene : " + personas.size() + " elementos");
            }//Fin caso 1
            case 2 -> {//Listar a las personas
                System.out.println("Listado de personas: ");
                //mejoras con lambda y el metodo de referencia
                //personas.forEach((persona)-> System.out.println(persona));
                personas.forEach(System.out::println);
            }
        }
    }//fin del metodo ejecutarOperacion
}//Fin de la clase ListadoPersonasApp