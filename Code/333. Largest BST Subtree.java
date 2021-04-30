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
    int result;
    
    class RType{
        boolean isBST;
        int upper;
        int lower;
        int count;
        
        RType(boolean isBST, int lower, int upper, int count){
            this.count = count;
            this.isBST = isBST;
            this.lower = lower;
            this.upper = upper;
        }
    }
    
    
    private RType helper(TreeNode node){        
        if (node == null){
            return new RType(true, 0, 0, 0);
        }
        
        RType left = helper(node.left);
        RType right = helper(node.right);
        
        if (left.count == 0 && right.count == 0){
            result = Math.max(result, 1);
            return new RType(true, node.val, node.val, 1);
        }else if (left.count == 0){
            if (right.isBST == false){
                return new RType(false, 0, 0, Integer.MAX_VALUE);
            }else{
                if (node.val < right.lower){
                    result = Math.max(result, right.count + 1);
                    return new RType(true, node.val, right.upper, right.count + 1);
                }else{
                    return new RType(false, 0, 0, Integer.MAX_VALUE);
                }
            }
        }else if (right.count == 0){
            if (left.isBST == false){
                return new RType(false, 0, 0, Integer.MAX_VALUE);
            }else{
                if (node.val > left.upper){
                    result = Math.max(result, left.count + 1);
                    return new RType(true, left.lower, node.val, left.count + 1);
                }else{
                    return new RType(false, 0, 0, Integer.MAX_VALUE);
                }
            }
        }else{
            if (left.isBST == true && right.isBST == true && left.upper < node.val && right.lower > node.val){
                result = Math.max(result, left.count + right.count + 1);
                return new RType(true, left.lower, right.upper, left.count + right.count + 1);
            }else{
                return new RType(false, 0, 0, Integer.MAX_VALUE);
            }
        }
        

    }
    
    
    public int largestBSTSubtree(TreeNode root) {
        helper(root);
        return this.result;
    }
}