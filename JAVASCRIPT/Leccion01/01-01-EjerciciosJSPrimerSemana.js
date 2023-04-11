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

   