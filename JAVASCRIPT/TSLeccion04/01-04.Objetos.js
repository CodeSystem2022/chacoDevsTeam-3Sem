let x= 10;
console.log(x.length);

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

console.log(persona['apellido']);//Accedemos como si fuera un arreglo

//for in
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}