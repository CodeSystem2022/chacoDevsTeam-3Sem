//Video 5 Valladares Juan Ignacio
//let persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer: Persona is not defined

class Persona{
    constructor(nombre, apellido){
        this.persona = nombre;
        this.apellido = apellido;
    }


//Video 6 Valladares Juan Ignacio
    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }
}

let persona1 =new Persona('Martin', 'Perez');
console.log(persona1.apellido);
console.log(persona1);
let persona2 =new Persona('Martin', 'Perez');
console.log(persona2.apellido)
console.log(persona2);


//video 7
//Espinola Renzo Oscar Alejo
class Empleado extends Persona{//clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido)
        this._departamento = departamento;
    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }
}
//video 8
//Espinola Renzo Oscar Alejo
let empleado1 = new Empleado('Maria', 'Gimenez','Sistemas');
console.log(empleado1);
console.log(empleado1.nombre);