import java.util.Arrays;

public class Actividad_1 {

    public static void main(String[] args) {
        int n = 3; 
        int[] codigos = new int[n]; 
        String[] nombres = new String[n]; 
        double[][] notas = new double[n][4]; 

        String nombree = "Pepe";
        int notaBase = 5;
        int codigoBuscado = 2;

        
        for (int i = 0; i < n; i++) {
            codigos[i] = i; 
            nombres[i] = nombree + i; 

           
            for (int j = 0; j < 3; j++) {
                notas[i][j] = notaBase - i; 
            }

            
            notas[i][3] = (notas[i][0] * 0.3) + (notas[i][1] * 0.3) + (notas[i][2] * 0.4);
        }
        boolean encontrado = false;
        for (int i = 0; i < n; i++) {
            if (codigoBuscado == codigos[i]) {
                System.out.println("Estudiante encontrado:");
                System.out.println("Código: " + codigos[i]);
                System.out.println("Nombre: " + nombres[i]);
                System.out.println("Notas: Corte1=" + notas[i][0] + ", Corte2=" + notas[i][1] + ", Corte3=" + notas[i][2]);
                System.out.println("Nota definitiva: " + notas[i][3]);
                encontrado = true;
                break;
            }
        }

        if (!encontrado) {
            System.out.println("Estudiante con código " + codigoBuscado + " no encontrado.");
        }
    }
}
