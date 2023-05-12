
package test;

import domain.*;


public class TestConversionObjetos {
    public static void main(String[] args) {
       //InstanceOf
        Empleado  empleado1 = new Empleado("Juan",10000);
        determinarTipo(empleado1);
        empleado1 = new Gerente("Jose",5000,"Sistemas");
        //determinarTipo(empleado1);
    }
   
    public static void determinarTipo(Empleado empleado){
       if(empleado instanceof Gerente){
            System.out.println("Es del tipo Gerente");
            Gerente gerente = (Gerente)empleado;
            System.out.println("Gerente: "+gerente.getDepartamento());
            //((Gerente) empleado).getDepartamento();
            //System.out.println("Gerente: "+empleado);
       }
       else if (empleado instanceof Empleado){
            System.out.println("Es del tipo Empleado");
            //provoca exception ya que no se puede castear de una clase padre
            //hacia una clase hija en tiempo de ejecucion
            //Gerente gerente = (Gerente)empleado;
            //System.out.println("Gerente: "+gerente.getDepartamento());
       }
       else if(empleado instanceof Object)
            System.out.println("Es de tipo Object");
        }
   
}
