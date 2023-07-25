import java.util.*;
class TwoSum{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int  n = sc.nextInt();
        int nums[] = new int[n];
        for(int i = 0 ; i< n ; i++){
            nums[i] = sc.nextInt();
        }
        int target=sc.nextInt();
        int arr[]=twosum(nums,target);
        System.out.println(arr[0]+" "+arr[1]);
    }

    public static int[] twosum(int[] nums ,int target ){
        HashMap<Integer,Integer> map=new HashMap<>();
        int i=0,j=0;
        for( i=0;i<nums.length;i++){
            int res=target-nums[i];
            if(map.containsKey(res)){
                j=map.get(res);
                break;
            }else{
                map.put(nums[i],i);
            }
        }
        return new int[]{i,j};

    }
}