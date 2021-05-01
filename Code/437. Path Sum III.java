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
    
    public int pathSum(TreeNode root, int targetSum) {
        dfs(root, targetSum, new ArrayList<Integer>());
        return result;
    }
    
    private void dfs(TreeNode node, int targetSum, List<Integer> pathSum){
        if (node == null){
            return;
        }
        

        for (int i = 0; i < pathSum.size(); i++){
            if (pathSum.get(i) + node.val == targetSum){
                result++;
            }
            pathSum.set(i, pathSum.get(i) + node.val);
        }
        
        if (node.val == targetSum){
            result++;
        }
        pathSum.add(node.val);
        dfs(node.left, targetSum, pathSum);
        dfs(node.right, targetSum, pathSum);
        pathSum.remove(pathSum.size() - 1);
        
        for (int i = 0; i < pathSum.size(); i++){
            pathSum.set(i, pathSum.get(i) - node.val);
        }
        
    }
}