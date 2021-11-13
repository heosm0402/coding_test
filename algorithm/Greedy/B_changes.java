public class B_changes {
    public static void main(String[] args) {
        int money = 1260;
        int countCoin = 0;
        int[] coinTypes = {500, 100, 50, 10};

        for (int i = 0; i < 4; i++) {
            countCoin += money / coinTypes[i];
            money %= coinTypes[i];
        }

        System.out.println(countCoin);
    }
}