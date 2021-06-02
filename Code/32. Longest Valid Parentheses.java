class Solution {
    public int longestValidParentheses(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.offerLast(-1);
        int res = 0;
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '('){
                stack.offerLast(i);
            }else{
                stack.pollLast();
                if (stack.isEmpty()){
                    stack.offerLast(i);
                }else{
                    res = Math.max(res, i - stack.peekLast());
                }
            }
        }
        return res;
    }
}