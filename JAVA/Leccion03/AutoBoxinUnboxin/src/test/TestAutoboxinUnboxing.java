package test;

public class TestAutoboxinUnboxing {
    public static void main(String[] args){
       //Clases envolventes o Wrapper
        /*
          Clases envolventes de tipos primitivos 
          1-int = la clase envolvente es Integer
          2-long = la clase envolvente es Long
          3-float = la clase envolvente es Float
          4-double = la clase envolvente es Double
          5-boolean = la clase envolvente es Boolean
          6-byte = la clase envolvente es Byte
          7-char = la clase envolvente es Character
          8-short = la clase envolvente Short
        */
        
        int enteroPrim = 10; //Tipo primitivo
        System.out.println("enteroPrim = " + enteroPrim);
        Integer entero = 10; //Tipo object con la clase interger 
        System.out.println("entero = " + entero.doubleValue()); //AutoBoxing
        
        int entero2 = entero; //Unboxing
        System.out.println("entero2 = " + entero2);
        
    }
    
}
