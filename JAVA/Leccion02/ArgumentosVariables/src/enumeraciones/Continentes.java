package enumeraciones;

public enum  Continentes {
    AFRICA(53,"1.2 billones"),
    EUROPA(46,"1.1 billones"),
    ASIA(44,"1.9 billones"),
    AMERICA(34,"150.2 billones"),
    OCEANTA(14,"1.2 billones");

    private final int paises;
    private String habitantes;

    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes=habitantes;
    }
    //metodo get,para recuperar valores encapsulados
    public int getPaises(){
        return this.paises;
    }
    public String getHabitantes(){
        return this.habitantes;
    }

    //Mostramos el continente

}
