import java.util.Scanner;

class ClimingStairs {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int  n = sc.nextInt();
        System.out.println(climingStairs(n));
    }

    public static int climingStairs(int n){
            int dp[] =new int[n+1];
            dp[0] = 1;
            dp[1] = 1 ;
            for(int i = 2 ; i< dp.length ; i++){
                 dp[i] = dp[i-1]+ dp[i-2];
            }
            return dp[n];
    }
}
