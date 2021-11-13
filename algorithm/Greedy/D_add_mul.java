import java.util.Scanner;

public class D_addmul {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        long result = 0;
        for (int i = 0; i < str.length(); i++) {
            int num = str.charAt(i) - '0';
            if (num <= 1 || result <= 1) {
                result += num;
            } else {
                result *= num;
            }
        }

        System.out.println(result);
        sc.close();
    }
}
