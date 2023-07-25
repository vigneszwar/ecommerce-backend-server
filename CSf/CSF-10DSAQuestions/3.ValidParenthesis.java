import java.util.Scanner;
import java.util.Stack;

class ValidParenthesis {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        System.out.println(validparenthesis(str));
    }

    public static boolean validparenthesis(String str){
        Stack<Character> stack = new Stack<>();
        for(char ch :  str.toCharArray()){
            if( ch == '(')
                stack.push(')');
            else if(ch == '{')
                stack.push('}');
            else if(ch == '[')
               stack.push(']');
            else if(stack.isEmpty() || ch != stack.pop())
              return false;
        }
        return stack.isEmpty();
    }
}
