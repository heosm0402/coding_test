import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class E_adventurer {
    public static int n;
    public static ArrayList<Integer> arrayList = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            arrayList.add(sc.nextInt());
        }

        Collections.sort(arrayList);
        
        int result = 0;
        int member = 0;
        for (int i = 0; i < n; i++) {
            member += 1;
            if (member >= arrayList.get(i)) {
                result += 1;
                member = 0;
            }
        }
        System.out.println(result);
        sc.close();

    }    
}
