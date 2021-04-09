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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        Map<Integer, Integer> index = new HashMap();
        for (int i = 0; i < inorder.length; i++){
            index.put(inorder[i], i);
        }
        return helper(inorder, postorder, 0, inorder.length - 1, 0, postorder.length - 1, index);
        
    }
    
    private TreeNode helper(int[] inorder, int[] postorder, int in_start, int in_end, int post_start, int post_end, Map<Integer, Integer> map){
        if (in_start > in_end || post_start > post_end){
            return null;
        }
        
        TreeNode root = new TreeNode(postorder[post_end]);
        int root_index = map.get(root.val);
        int gap = in_end - root_index;
        root.left = helper(inorder, postorder, in_start, root_index - 1, post_start, post_end - gap - 1, map);
        root.right = helper(inorder, postorder, root_index + 1, in_end, post_end - gap, post_end - 1, map);
        return root;
        
    }
}