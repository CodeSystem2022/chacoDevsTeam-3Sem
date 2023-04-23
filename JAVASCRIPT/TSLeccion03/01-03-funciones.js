// Balbuena Fernando-Creamos una nueva funcion
miFuncion(10,15);//Hosting
function miFuncion(a,b){
    console.log("Sumamos: "+ (a+b));
    return a+b;
    
}
//Llamando a la función
miFuncion(5,4);
let resultado=miFuncion(6,7);
console.log(resultado);

// Valladares Juan Ignacio
//Declaramos una función de tipo expresión o anonima
let x = function(a, b){ return a + b}; //necesita cierre con punto y coma
resultado = x(5, 6); //al llamarla se pone la variable y parentesis
console.log(resultado);

//Funciones de tipo self y invoking
(function(a, b){
    console.log('Ejecuntado la función:' + (a + b))
})(9, 6);

//Espinola Renzo
//Argumentos y parametros
//parametros se llaman a las variables(a,b)
//argumentos se llaman a los valores que le pasamos a la funcion(5,7,8)
//JS presenta flexibilidad al pasar los argumentos a la funcion
//no es necesario para pasar todos los args pueden ser mas o menos args
//Funcion de tipo expresion
let sumar = function(a = 4, b = 8){
    console.log(arguments[0]);//muetra el parametro de: a
    console.log(arguments[1]);//muetra el parametro de: b
    return a + b + arguments[2];
}
resultado = sumar(3,2,9);
console.log(resultado);

//Espinola Renzo
//sumar todos los argumentos
let respuesta = sumarTodo(5,4,13,10,9);
console.log(respuesta);
function sumarTodo(){
    let suma=0;
    for(let i = 0; i< arguments.length; i++){
        suma += arguments[i]; // arguments es para arreglos
    }
    return suma;
}


// Juan Carlos Gutierrez 
// Paso por referencia 
const persona ={
    nombre: 'Juan',
    apellido: 'Lepez'
}
console.log(persona);
function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
}

cambiarValorObjeto(persona);
console.log(persona);

// Juana Natalia Gutierrez
// Tipos de Datos en una Funcion

console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.length);
 }

 miFuncionDos(5, 7, 3, 6);

 //toString
 var miFuncionTexto = miFuncionDos.toString();//convierte la funcion a texto
 console.log(miFuncionTexto);  

  //Gutierrez Juana Natalia
 //Funcion Flecha
 const sumarFuncionFlecha = (a, b) =>a + b;
 resultado = sumarFuncionFlecha(3, 7);//Asignamos el valor a una variable
    console.log(resultado);
