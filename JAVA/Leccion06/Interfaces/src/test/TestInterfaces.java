package test;

import accesodatos.IAccesoDatos;
import accesodatos.ImplementacionMySql;
import accesodatos.ImplementacionOracle;

//video 5
public class TestInterfaces {
    public static void main(String[] args) {
    IAccesoDatos datos = new ImplementacionMySql();
    //datos.listar();
    //clase 6
    //imprimir(datos);
    datos = new ImplementacionOracle();
    //datos.listar();
    imprimir(datos);
    }
    //clase 6
    public static void imprimir(IAccesoDatos datos){
        datos.listar();
    }
}