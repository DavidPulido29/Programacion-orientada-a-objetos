
package ejer4.pkg1;

public class Cuenta {
    protected float saldo;
    protected int numeroConsignaciones = 0;
    protected int numeroRetiros = 0;
    protected float tasaAnual;
    protected float comisionMensual = 0;
    
    public Cuenta(float saldo, float tasaAnual){
        this.saldo = saldo;
        this.tasaAnual = tasaAnual;
    }
    
    public void consignar(float cantidad){
        saldo += cantidad;
        numeroConsignaciones += 1;
    }
    
    public void retirar(float cantidad){
        if (saldo - cantidad > 0) {
            saldo -= cantidad;
            numeroRetiros += 1;
        }
        else {
            System.out.println("El valor a retirar excede"
                    + " el saldo de la cuenta");
        }
    }
    
    public void calcularInteres(){
        float tasaMensual = tasaAnual / 12;
        float interesMensual = saldo * tasaMensual;
        saldo += interesMensual;
    }
    
    public void extractoMensual(){
        saldo -= comisionMensual; 
        calcularInteres();
    }
        
}