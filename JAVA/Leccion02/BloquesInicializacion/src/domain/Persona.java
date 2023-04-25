package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static{//Bloque de Inicialización estático
        System.out.println("Ejecución del bloque estatico");
        ++Persona.contadorPersonas;
        //idPersona = 10; No es estatico un atributo, por esto tenemos un error
    }
    
    {//Bloque de inicialización No estático(contexto dinámico)
        System.out.println("Ejecución del bloque no estático");
        this.idPersona = Persona.contadorPersonas++;//Incrementamos el atributo
    }
    
    //Los bloques de inicialización se ejecutan antes del contructor
    public Persona(){
        System.out.println("Ejecución del contructor");
    }
    
    public int getIdPersona(){
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
    
}
