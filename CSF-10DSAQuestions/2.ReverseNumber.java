import java.util.Scanner;

class ReverseNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int  n = sc.nextInt();
        System.out.println(reversenumber(n));
    }
    public static int reversenumber(int n){
        boolean flag = false;
        if(n < 0){
            n= Math.abs(n);
            flag = true;
        }
        String rev = "";
        while(n >0){
            int rem = n%10;
            rev += ""+rem;
            n /= 10;
            }
        return flag ? (-1)*Integer.parseInt(rev) : Integer.parseInt(rev);
    }
}
