package Inmuebles;

public class Prueba {

    public static void main(String[] args) {
        ApartamentoFamiliar apto1 = new ApartamentoFamiliar(103067, 120, 
                "Avenida Santander 45-45", 3, 2, 200000);
        System.out.println("Datos apartamento familiar");
        apto1.calcularPrecioVenta(apto1.valorArea);
        apto1.imprimir();
        
        Apartaestudio aptestudio1 = new Apartaestudio(12354, 50,
                "Avenida Caracas 30-15", 1, 1);
        System.out.println("Datos apartaestudio");
        aptestudio1.calcularPrecioVenta(aptestudio1.valorArea);
        aptestudio1.imprimir();
    }
}