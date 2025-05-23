import java.io.IOException;
import java.util.*;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        double raio = scanner.nextDouble();
        double area = 3.14159 * Math.pow(raio, 2);

        System.out.println(String.format("A=%.4f", area));
    }
 
}