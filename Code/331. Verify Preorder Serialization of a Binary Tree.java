class Solution {
    public boolean isValidSerialization(String preorder) {
        String[] nodes = preorder.split(",");
        Deque<Character> stack = new ArrayDeque();
        for (String s: nodes){
            Character c = s.charAt(0);
            stack.offerLast(c);
            if (stack.size() >= 3){
                cleanStack(stack);
            }
        }
        return stack.size() == 1 && stack.peekLast() == '#';
    }
    
    private void cleanStack(Deque<Character> stack){
        while (true){
            if (stack.size() < 3){
                return;
            }
            Character third = stack.pollLast();
            Character second = stack.pollLast();
            Character first = stack.pollLast();
            if (Character.isDigit(first) && !Character.isDigit(second) && !Character.isDigit(third)){
                stack.offerLast('#');
                continue;
            }
            stack.offerLast(first);
            stack.offerLast(second);
            stack.offerLast(third);
            break;
        }
    }
}