package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        System.out.println("Continente No.4: " + Continentes.AMERICA);
        System.out.println("Numero de paises en el 4to. continente: "
                + Continentes.AMERICA.getPaises());
        System.out.println("Numero de habitantes en el 4to. continente: "
                + Continentes.AMERICA.getHabitantes());

        System.out.println("Continente No.1: " + Continentes.AFRICA);
        System.out.println("Numero de paises en el 1er. continente: "
                + Continentes.AFRICA.getPaises());
        System.out.println("Numero de habitantes en el 1er. continente: "
                + Continentes.AFRICA.getHabitantes());

        System.out.println("Continente No.5: " + Continentes.OCEANIA);
        System.out.println("Numero de paises en el 5to. continente: "
                + Continentes.OCEANIA.getPaises());
        System.out.println("Numero de habitantes en el 5to. continente: "
                + Continentes.OCEANIA.getHabitantes());

        System.out.println("Continente No.3: " + Continentes.ASIA);
        System.out.println("Numero de paises en el 3ro. continente: "
                + Continentes.ASIA.getPaises());
        System.out.println("Numero de habitantes en el 3ro. continente: "
                + Continentes.ASIA.getHabitantes());

        System.out.println("Continente No.2: " + Continentes.EUROPA);
        System.out.println("Numero de paises en el 2do. continente: "
                + Continentes.EUROPA.getPaises());
        System.out.println("Numero de habitantes en el 2do. continente: "
                + Continentes.EUROPA.getHabitantes());
    }


       // System.out.println("Dia:"+Dias.LUNES);
    }

