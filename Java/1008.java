import java.io.IOException;
import java.util.*;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        int hours_worked = scanner.nextInt();
        double salary = scanner.nextDouble();
        

        System.out.println(String.format("NUMBER = %d\nSALARY = U$ %.2f", number, (hours_worked*salary)));
       
    }
 
}