import java.util.Scanner;

class MaximumSubarray {
    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
        int  n = sc.nextInt();
        int nums[] = new int[n];
        for(int i = 0 ; i< n ; i++){
            nums[i] = sc.nextInt();
        }
        System.out.println(maxSubarray(nums));
    }

    public static int maxSubarray(int[] nums){
        int currSum = 0; int max = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            currSum += nums[i];
            if(currSum > max)
              max = currSum;
            if(currSum <0)
              currSum = 0;
        }
        return max;
    }
}
