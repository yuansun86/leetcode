/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode recoverFromPreorder(String S) {
        Deque<Character> deque = new ArrayDeque();
        for (int i = S.length() - 1; i >= 0; i--){
            Character ch = S.charAt(i);
            deque.addLast(ch);
        }
        return consume(deque, 0);
        
    }
    
    private int getValue(Deque<Character> deque){
        int value = 0;
        while (!deque.isEmpty() && deque.peekLast() != '-'){
            int number = Character.getNumericValue(deque.pollLast());
            value = value * 10 + number;
        }
        return value;
    }
    
    private TreeNode consume(Deque<Character> deque, int pre_level){
        if (deque.isEmpty()){
            return null;
        }
        TreeNode root;
        if (pre_level == 0){
            int val = getValue(deque);
            root = new TreeNode(val);
        }else{
            int level = 0;
            while (!deque.isEmpty() && deque.peekLast() == '-'){
                deque.pollLast();
                level++;
            }
            
            if (level != pre_level){
                for (int i = 0; i < level; i++){
                    deque.add('-');
                }
                return null;
            }else{
                int val = getValue(deque);
                root = new TreeNode(val);
            }
        }
        
        root.left = consume(deque, pre_level + 1);
        root.right = consume(deque, pre_level + 1);
        return root;
    }
}