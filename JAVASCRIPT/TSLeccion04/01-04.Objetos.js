let x= 10;
console.log(x.length);
console.log('Tipos Primitivos');
//Objeto
let persona= {
    nombre:'Carlos',
    apellido:'Gil',
    email:'cgil@gmail.com',
    edad:30,
    nombreComleto: function(){ //metodo
        return this.nombre+' '+this.apellido;
    }
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


//Tatiana Tamara, Giménez Ríos.
//Ticket Nº176
//Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreComleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+'' +this.apellido+'' +telefono;
    }
}
let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'   
}

console.log(persona4.nombreComleto2('Lic.', '549261848485'));
console.log(persona4.nombreComleto2.call(persona5, 'Ing.', '5492618585856'));
