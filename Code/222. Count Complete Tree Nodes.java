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
    public int countNodes(TreeNode root) {
        if (root == null){
            return 0;
        }
        int height = getHeight(root);
        if (height == 0){
            return 1;
        }
        
        int left = 0;
        int right = (int)Math.pow(2, height) - 1;
        int mid;
        while (left + 1 < right){
            mid = left + (right - left) / 2;
            if (exist(mid, height, root)){
                left = mid;
            }else{
                right = mid;
            }
        }
        
        if (exist(right, height, root)){
            return right + (int)Math.pow(2, height);
        }
        if (exist(left, height, root)){
            return left + (int)Math.pow(2, height);
        }
        
        return 1;
    }
    
    private int getHeight(TreeNode node){
        int height = -1;
        while (node != null){
            height++;
            node = node.left;
        }
        return height;
    }
    
    private boolean exist(int index, int height, TreeNode node){
        int left = 0;
        int right = (int)Math.pow(2, height) - 1;
        int mid;
        while (height > 0){
            mid = left + (right - left) / 2;
            if (index <= mid){
                node = node.left;
                right = mid;
            }else{
                node = node.right;
                left = mid;
            }
            height--;
        }
        return node != null;
    }
}