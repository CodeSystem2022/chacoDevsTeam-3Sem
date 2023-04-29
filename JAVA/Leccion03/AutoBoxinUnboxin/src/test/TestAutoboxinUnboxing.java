package test;

public class TestAutoboxinUnboxing {
    public static void main(String[] args){
        //Clases Envolventes o Wrapper
        /*
           Clases envolventes de tipos primitivos
            int = la clase envolvente es integer
        */
        
        int enteroPrim = 10; //Tipo primitivo
        System.out.println("enteroPrim = " + enteroPrim);
        Integer entero = 10; //Tipo object con la clase interger 
        System.out.println("entero = " + entero.doubleValue()); //AutoBoxing
        
        int entero2 = entero; //Unboxing
        System.out.println("entero2 = " + entero2);
        
    }
    
}
