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
   