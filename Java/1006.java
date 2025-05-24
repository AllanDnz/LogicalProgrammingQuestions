import java.io.IOException;
import java.util.*;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        double grade1 = scanner.nextDouble();
        double grade2 = scanner.nextDouble();
        double grade3 = scanner.nextDouble();
        double avg =  ((grade1*2) + (grade2*3) + (grade3*5)) / 10;

        System.out.println(String.format("MEDIA = %.1f", avg));
    }
 
}