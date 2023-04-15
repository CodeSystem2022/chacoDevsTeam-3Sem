//Ejercicio Espinola Renzo
console.log("Ejercicio for Espinola Renzo");
    let factorial = 1;
    let numero = 4;
    let x="";

    if(numero<0){
        console.log("Debe ingresar un numero mayor a 0 ");
        x = ("Debe ingresar un numero mayor a 0");
    }else{
        for(let i = 1; i <= numero ; i++ ){
            factorial *=  i;
        }
        if(numero!=null){
            x = ("Factorial de "+numero+" = "+factorial);
            console.log(x);
        }else{
            x = ("Debe ingresar un numero");
            console.log(x);
        }
    }
    console.log(x);

//Ejercicio Gimenez Rios Tatiana Tamara
console.log("Ejercicio While Giemenez Rios Tatiana Tamara");
let negativo=0;
let positivo=0;
let neutro=0;
let i=0;
let num= [0,2,3,-2,-8,-10,5,50,0,32];
while (i<num.length) { 
        if(num[i]>0){
            positivo+=1;
        }else if(num[i]<0){
            negativo+=1;
        }else{
            neutro+=1;
        }
        i+=1;
}
    console.log("Positivo: "+positivo);
    console.log("Negativo: "+negativo);
    console.log("Neutro: "+neutro);

    // EJERCICIO ALEJO GUTIERREZ 
console.log("Ejercicio Alejo Gutierrez");
  let numero1 =[10,25,35,50];  
  let contador = 0;
  do {
    if (numero1[contador] % 2 === 0) {
      console.log("Es multiplo" ) // Sumamos el número si es múltiplo de 2
    } else {
        console.log("No es multiplo")
    }
    contador++;
  } while (contador < numero1.length);
 
 
  // ejercicio N8 Ciclo while Gutierrez Agustin
  //Ejercicio 8: Pedir un número N, y mostrar todos los números del 1 al N.
console.log("Ejercicio Gutierrez Agustin");
let numero2 = 8 ;
let g = 1;
while (g <= numero2) {
    console.log(g);
    g++;
}

//Ejercicio N9 While Gutierrez Juana Natalia
console.log("Ejercicio Gutierrez Juana Natalia");
let conteo = 0;
while (conteo <= 7) {
  console.log("conteo= "+conteo );
  conteo++;
}
//Ejercicio N10 Ciclo for Balbuena Nicolas
console.log("Ejercicio Balbuena Nicolas");
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

//Ejercicio N11 While Ivan Matias
console.log("Ejercicio Ivan Matias");
let numeros = [5, 10, 15, 20];
let cuadrado;
let i1 = 0;

while(i1 < numeros.length){
    cuadrado = Math.pow(numeros[i1], 2);
    console.log(`El número ${numeros[i1]} elevado al cuadrado es: ${cuadrado}`);
    i1++;
}
console.log("El programa ha finalizado por haber recorrido todos los números del array");

//Ejercicio N12 Do While, Valdez Carlos Federico
let count = 0;
let limite = 7;
do{
    count++;
    console.log("el numero actual de la estructura de control es"+ count)
}while(limite < 7);


// Ejercicio N13 FOR, Juan Carlos Gutierrez

  // Solicitar las notas
  console.log("Ejercicio De Juan Carlos Gutierrez")
  let notaIntegrador = 2
  let notaExposicion = 5
  let notaParcial = 8

  // Calcular la nota final
  let notaFinal = (notaIntegrador * 0.35) + (notaExposicion * 0.25) + (notaParcial * 0.4);
if(notaFinal > 6){
    console.log("Aprobo con " + notaFinal)
}else{
    console.log("Reprobo con " + notaFinal)
}
