//Video 5 Valladares Juan Ignacio
//let persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer: Persona is not defined

class Persona{

    static contadorPersona = 0;// atributo estatico
    //email= "valor default email"; // atributo no estatico

//Video 7 Balbuena Fernando Nicolas
    static get MAX_OBJ(){  //Este metodo simula una constante
        return 5;
    }

    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
        //Balbuena Fernando Nicolas
        if(Persona.contadorPersona < Persona.MAX_OBJ){
            this.idPersona =  ++Persona.contadorPersona; 
        }
        else{
            console.log('Se ha superado el maximo de objetos permitidos ')
        }
        
        //console.log('Se incrementa el contador: '+Persona.contadorObjetosPersona);
    }

//Tatiana Tamara, Giménez Ríos
get nombre(){
    return this._nombre;
}

set nombre(nombre){
    this._nombre = nombre;
}

//Video 6 Valladares Juan Ignacio
    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }
    nombreCompleto(){
        return this.idPersona+' '+this._nombre+' '+this._apellido;
    }
    //Sobrescribiendo el metodo de la clase padre (Object)
    toString(){ //Regresa un String
       //Se aplica polimorfismo que significa  = multiples formas en tiempo de ejecucion
       //El metodo que se ejecuta depende si es una refe rencia de tipo padre o hija
        return this.nombreCompleto();
     }

//Video 1
//Tatiana Tamara, Giménez Rios
     static saludar(){
        console.log('Saludos desde este método static');   
    }

    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido);
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
    //Fernando Nicolas Balbuena
    //Sobreescritura
nombreCompleto(){
    return super.nombreCompleto()+', '+this._departamento;
}

}
//video 8
//Espinola Renzo Oscar Alejo
let empleado1 = new Empleado('Maria', 'Gimenez','Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

//VIDEO 3 y 4
// JUAN CARLOS GUTIERREZ
function Persona3(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre + " " + this.apellido;
}
}
let padre =new Persona3('Leo', 'Lopes','lopezl@gmail.com');
padre.nombre ='Luis'; //MODIFICAMOS EL NOMBRE
console.log(padre);
console.log(padre.nombreCompleto()); //UTILIZAMOS LA FUNCION
let madre = new Persona3('Laura','contrera','contrera@gmail.com');
console.log(madre);
console.log(madre.nombreCompleto());

//Video 3
//Tatiana Tamara, Giménez Ríos.
//Object. prototype.toString Esta es la manera de acceder a atributos y métodos de manera dinámica
console.log(empleado1.toString());
//Espinola, Renzo Oscar
console.log(persona1.toString());

//persona1.saludar(); no se utiliza desde el objeto
Persona.saludar();
Persona.saludar2(persona1);

//Video 2
//Tatiana Tamara, Giménez Ríos.
Empleado.saludar();
Empleado.saludar2(empleado1);

//console.log(persona1.contadorObjetosPersona)
console.log(Persona.contadorPersona);
console.log(Empleado.contadorPersona);

console.log(persona1.email);
console.log(empleado1.email);
//console.log(Persona.email); No se puede acceder desde la clase
//Espinola Renzo
console.log(persona1.toString())
console.log(persona2.toString())
console.log(empleado1.toString())
console.log(Persona.contadorPersona);
let persona3 = new Persona('Carla','Pertosi');
console.log(persona3.toString())
console.log(Persona.contadorPersona);

//Video 7 Balbuena Fernando Nicolas
console.log(Persona.MAX_OBJ);
Persona.MAX_OBJ = 10;
console.log(Persona.MAX_OBJ); //No se puede modificar

let persona4= new Persona('Franco','Diaz');
console.log(persona4.toString())
let persona5= new Persona('Liliana','Paz');
console.log(persona5.toString())
