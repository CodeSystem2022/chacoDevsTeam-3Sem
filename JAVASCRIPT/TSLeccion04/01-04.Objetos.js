let x= 10;
console.log(x.length);
console.log('Tipos Primitivos');
//Objeto
let persona= {
    nombre:'Carlos',
    apellido:'Gil',
    email:'cgil@gmail.com',
    edad:28,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase(); //Convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreComleto: function(){ //metodo
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){ //Este es el metodo get 
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    },
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreComleto());
console.log('Ejecutando con un objeto');
console.log(persona['apellido']);//Accedemos como si fuera un arreglo

console.log('Creamos un nuevo objeto');

 let persona2 = new Object(); // Debe crear un nuevo objeto en memoria
 persona2.nombre = "Juan";
 persona2.direccion = "Salada 14";
 persona2.telefono = "5492618282821";
 console.log(persona2.telefono)


//for in
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}
console.log('cambiamos y eliminamos un error');
// ALEJO HERNAN GUTIERREZ
persona.apellida = 'Betancud';//Cambiamos dinamicamente un valor del objeto 
delete persona.apellida;
console.log(persona);

//Tatiana Tamara, Giménez Ríos.
//Distintas formas de imprimir un objeto.
//Número 1: la más sencilla: Concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un objeto: forma 1');
console.log(persona.nombre+','+persona.apellido);

//Número 2: A través del ciclo for in
console.log('Distintas formas de imprimir un objeto: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);  
}

//Número 3: La función Object.values()
console.log('Distintas formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Número 4: Utilizaremos el método JSON.stringify
console.log('Distintas formas de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);

function Persona3(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
}
let padre = new Persona3('Leo', 'Lopez', 'lopezl@gmail.com');
padre.nombre = 'Luis';
padre.telefono = '549261828221';
console.log(padre);
let madre = new Persona3('Laura', 'Contrera', 'contreral@gmail.com');
console.log(madre);
console.log(madre.telefono); //la propiedad no está definida

console.log('Comenzamos a utilizar el metodo get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

//Tatiana Tamara, Giménez Ríos.
//Ticket Nº176
//Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' ' +this.apellido+' ' +telefono;
        // return this.nombre+ ' ' + this.apellido;
    }
}
let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'   
}

console.log(persona4.nombreCompleto2('Lic.', '549261848485'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '5492618585856'));

//Metodo Apply
//Espinola Renzo Oscar Alejo
let arreglo = ['Ing.','5492618686865']
console.log(persona4.nombreCompleto2.apply(persona5,arreglo));


//Balbuena Fernando Nicolas
//Distintas formas de crear un objeto
//Caso objeto 1
let miObjeto = new Object(); //Esta es una opc formal
//Caso objeto 2
let miObjeto2 = {}; //Esta opción es breve y recomendada

//Caso String 1
let miCadena1 = new String('Hola'); //Sintaxis formal
//Caso String 2
let miCadena2 = 'Hola'; //Esta es la sintaxis simplificada y recomendada 

//Caso con números 1
 let miNumero = new Number(1); //Es formal no recomendable
 //Caso con numeros 2
 let miNumero2 = 1; //Sintaxís recomendada 

 //Caso boolean 1
 let miBoolean1 = new Boolean(false); //Formal
 //Caso boolean 2
 let miBoolean2 = false; //Sintaxis recomendada 

 //Caso Arreglos 1
 let miArreglo1 = new Array(); //FOrmal
 //Caso Arreglos 2
 let miArreglo2 = [];

 //Caso Fuction 1
 let miFuncion1 = new function(){}; //Todo despues de new es considerado objeto
 //Caso fuction 2
let miFuncion2 = function(){}; //notacion simplificada y recomendada

//Uso de Prototype
Persona3.prototype.telefono = '2618383832';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '5492618383832';
console.log(madre.telefono);