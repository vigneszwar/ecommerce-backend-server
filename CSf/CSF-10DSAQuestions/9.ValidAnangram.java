import java.util.HashMap;
import java.util.Scanner;

class ValidAnangram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        String str1 = sc.next();
        System.out.println(validAnagram(str,str1));
    }

    public static boolean validAnagram(String s, String t){

        HashMap<Character , Integer> map = new HashMap<>();
        for(char ch : s.toCharArray()){
            map.put(ch, map.getOrDefault(ch,0)+1);
        }
        for(char ch : t.toCharArray()){
            if(map.containsKey(ch)){
               if(map.get(ch) == 1){
                 map.remove(ch);
               }
               else{
                  map.put(ch, map.get(ch)-1);
               }
            }
            else
              return false;
        }
        if(map.isEmpty())
          return true;
        return false;
    }
}
