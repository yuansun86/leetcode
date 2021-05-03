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
    int result = 0;
    
    public int longestUnivaluePath(TreeNode root) {
        helper(root);
        return result;
    }
    
    private int helper(TreeNode node){
        // return the longest path of the same value where node resides at one side
        
        if (node == null) return 0;
        
        int left = helper(node.left);
        int right = helper(node.right);
        
        if (node.left != null && node.right != null && node.left.val == node.right.val && node.left.val == node.val){
            result = Math.max(result, left + right + 2);
        }
        
        int curmax = 0;
        if (node.left != null && node.left.val == node.val){
            curmax = Math.max(curmax, left + 1);
        }
        if (node.right != null && node.right.val == node.val){
            curmax = Math.max(curmax, right + 1);
        }
        
        result = Math.max(result, curmax);
        return curmax;
    }
}