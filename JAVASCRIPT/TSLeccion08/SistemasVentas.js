class Producto{
    static contadorProducto = 0;
    constructor(nombre,precio){
        this._idProducto = ++Producto.contadorProducto;
        this._nombre=nombre;
        this._precio=precio;
    }

    get idProducto() {
        return this._idProducto;
    }
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get precio(){
        return this._precio;
    }
    set precio(precio){
        this._precio = precio;
    }
    toString(){
        return `${this._idProducto} ${this._nombre} ${this._precio}`};
}//Fin de la clase Producto

class Orden{
    static contadorOrdenes = 0;
    static getMAX_PRODUCTOS(){
        return 5;
    }

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this._contadorProductosAgregados = 0;
    }

    get idOrden(){
        return this._idOrden;
    }

    agregarProducto(producto){
        if(this._productos.length < Orden.getMAX_PRODUCTOS()){
            this._productos.push(producto);//Tenemos 2 tipos de sintaxis: 1
            //this._productos[this._contadorProductosAgregados++] = producto; //segunda sintaxis
        }else{
            console.log('No se pueden agregar mas productos');
        }
    }//Fin del método agregarProducto
}//Fin de la clase Orden

let producto1 = new Producto('Pantalón', 200);
let producto2 = new Producto('Camisa', 150);
console.log(producto1.toString());
console.log(producto2.toString());

    producto1 = new Producto("TV",2500);
    producto2 = new Producto("SmarthPhone",26000);
    console.log(producto1.toString());
    console.log(producto2.toString());

    orden1 = new Orden();
    orden1.agregarProducto(producto1);
    orden1.agregarProducto(producto2);
    orden1.mostrarOrden();

    producto3 = new Producto("PC", 50000);
    producto4 = new Producto("Heladera",38000);
    producto5 = new Producto("Cocina",60000);
    producto6 = new Producto("Cocina2",52000);
    producto7 = new Producto("Cocina3",62000);
    producto8 = new Producto("Cocin5",61000);
    orden2 = new Orden();
    orden2.agregarProducto(producto3);
    orden2.agregarProducto(producto4);
    orden2.agregarProducto(producto5);
    orden2.agregarProducto(producto6);
    orden2.agregarProducto(producto7);
    orden2.agregarProducto(producto8);
    orden2.mostrarOrden();