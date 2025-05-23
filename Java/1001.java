import java.io.IOException;
import java.util.Scanner;
    
public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int number1 = scanner.nextInt();
        int number2 = scanner.nextInt();
        int x = number1 + number2;
        
        System.out.println("X = " + x);
    }
 
}