class Solution {
    public int scoreOfParentheses(String s) {
        Deque<String> stack = new ArrayDeque<>();
        char[] chs = s.toCharArray();
        for (char c: chs){
            if (c == '('){
                stack.offerLast(String.valueOf(c));
            }else {
                int sum;
                if (stack.peekLast().equals("(")){
                    stack.pollLast();
                    sum = 1;
                }else{
                    sum = 0;
                
                    while (!stack.isEmpty() && !stack.peekLast().equals("(")){
                        sum += Integer.parseInt(stack.pollLast());
                    }
                    if (!stack.isEmpty() && stack.peekLast().equals("(")){
                        sum *= 2;
                        stack.pollLast();
                    }
                }
                stack.offerLast(String.valueOf(sum));
            }
        }
        int res = 0;
        for (String str: stack){
            res += Integer.parseInt(str);
        }
        return res;
    } 
}