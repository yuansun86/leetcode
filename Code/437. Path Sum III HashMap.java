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
        dfs(root, targetSum, 0, new HashMap<Integer, Integer>());
        return result;
    }
    
    private void dfs(TreeNode node, int targetSum, int curSum, Map<Integer, Integer> pathSum){
        if (node == null){
            return;
        }
        
        curSum += node.val;
        if (curSum == targetSum){
            result++;
        }
        
        result += pathSum.getOrDefault(curSum - targetSum, 0);
        pathSum.put(curSum, pathSum.getOrDefault(curSum, 0) + 1);
        dfs(node.left, targetSum, curSum, pathSum);
        dfs(node.right, targetSum, curSum, pathSum);
        pathSum.put(curSum, pathSum.get(curSum) - 1);
        
        
        
    }
}