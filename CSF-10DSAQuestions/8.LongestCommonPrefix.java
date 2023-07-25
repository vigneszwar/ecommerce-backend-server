import java.util.*;

class LongestCommonPrefix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int  n = sc.nextInt();
        String nums[] = new String[n];
        for(int i = 0 ; i< n ; i++){
            nums[i] = sc.next();
        }
        System.out.println(lcf(nums));
    }

    public static String lcf(String[] nums){
        if (nums == null || nums.length==0 )
           return "" ;
        Arrays.sort(nums);
        int i = 0;
        while(i < nums[0].length()){
            if(nums[0].charAt(i) != nums[nums.length-1].charAt(i))
                break;
            else
                i++;
        }

        return nums[0].substring(0,i);
    }
}
