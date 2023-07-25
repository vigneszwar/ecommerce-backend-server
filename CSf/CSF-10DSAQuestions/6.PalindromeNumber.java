import java.util.Scanner;

class PalindromeNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int  n = sc.nextInt();
        System.out.println(palindromenumber(n));
    }

    public static boolean palindromenumber(int n){
        if(n < 0 || (n%10 == 0 && n !=0)){
            return false;
        }
        int revnum = 0;
        while(n > revnum){
            revnum=revnum*10 + n % 10 ;
            n /= 10;
        }

        return n == revnum || n == revnum/10;
    }
}
