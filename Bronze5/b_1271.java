// https://www.acmicpc.net/problem/1271
import java.math.BigInteger;
import java.util.Scanner;

public class b_1271 {

    public static void main(String[] args){
        BigInteger n;
        BigInteger m;
        Scanner sc=new Scanner(System.in);
        n=sc.nextBigInteger();
        m=sc.nextBigInteger();
        System.out.println(n.divide(m));
        System.out.println(n.remainder(m));

        sc.close();
    }
}
