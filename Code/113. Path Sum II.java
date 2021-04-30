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
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> results = new ArrayList<>();
        if (root == null){
            return results;
        }
        backtracking(root, targetSum, new ArrayList<Integer>(), results);
        return results;
    }
    
    private void backtracking(TreeNode node, int targetSum, List<Integer> path, List<List<Integer>> results){
        if (node.left == null && node.right == null){
            if (targetSum == node.val){
                path.add(node.val);
                results.add(new ArrayList(path));
                path.remove(path.size() - 1);
            }
            return;
        }
        
        if (node.left != null){
            path.add(node.val);
            backtracking(node.left, targetSum - node.val, path, results);
            path.remove(path.size() - 1);
        }
        
        if (node.right != null){
            path.add(node.val);
            backtracking(node.right, targetSum - node.val, path, results);
            path.remove(path.size() - 1);
        }
    }
}