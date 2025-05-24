import java.io.IOException;
import java.util.*;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        float grade1 = scanner.nextInt();
        float grade2 = scanner.nextInt();
        float avg =  ((grade1*3.5) + (grade2*7.5)) / 11;

        System.out.println("MEDIA = " + avg);
    }
 
}