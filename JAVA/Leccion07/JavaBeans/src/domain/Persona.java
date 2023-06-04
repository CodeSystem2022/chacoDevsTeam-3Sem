
package domain;

import java.io.Serializable;

public class Persona implements Serializable{
    private String nombre;
    private String apellido;
    
    //Constructor vacío: esto es obligatorio
    public Persona(){
        
    }
    public Persona(String nombre , String apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", apellido=" + apellido + '}';
    }
    
}
