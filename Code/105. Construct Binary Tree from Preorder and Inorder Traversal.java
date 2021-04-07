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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return helper(preorder, inorder, 0, preorder.length - 1, 0, inorder.length - 1);
    }
    
    public TreeNode helper(int[] preorder, int[] inorder, int pre_start, int pre_end, int in_start, int in_end){
        if (pre_start > pre_end || in_start > in_end){
            return null;
        }
        
        TreeNode root = new TreeNode(preorder[pre_start]);
        int gap = 0;
        int i = in_start;
        while (inorder[i] != root.val){
            gap++;
            i++;
        }
        root.left = helper(preorder, inorder, pre_start + 1, pre_start + gap, in_start, in_start + gap - 1);
        root.right = helper(preorder, inorder, pre_start + gap + 1, pre_end, in_start + gap + 1, in_end);
        return root;
    }
}