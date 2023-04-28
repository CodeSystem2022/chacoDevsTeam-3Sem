
package test;

import domain.Persona;

public class TestForEach {
    public static void main(String[] args) {
        int edades[] = {5, 6, 8, };//Sintaxis resumida
        for (int edad: edades){ //Sintaxis del ForEach
            System.out.println("edad = " + edad);
        }
        
        Persona personas[] = {new Persona("Ludmila"), new Persona("Kevin"), new Persona("Juani")};
        
        //ForEach
        for(Persona persona: personas){
            System.out.println("persona = " + persona);
        }
    }
}
