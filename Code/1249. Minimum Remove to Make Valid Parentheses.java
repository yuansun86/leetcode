class Solution {
    public String minRemoveToMakeValid(String s) {
        Set<Integer> idxRemove = new HashSet();
        Deque<Integer> stack = new ArrayDeque();
        for (int i = 0; i < s.length(); i++){
            Character ch = s.charAt(i);
            if (Character.isAlphabetic(ch)) continue;
            if (ch == '('){
                stack.offerLast(i);
            }else{
                if (!stack.isEmpty() && s.charAt(stack.peekLast()) == '('){
                    stack.pollLast();
                }else{
                    idxRemove.add(i);
                }
            }
        }
        idxRemove.addAll(stack);
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++){
            if (idxRemove.contains(i)) continue;
            sb.append(s.charAt(i));
        }
        return sb.toString();
    }
}