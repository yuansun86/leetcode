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
    List<Integer> res;
    int index;

    public List<Integer> flipMatchVoyage(TreeNode root, int[] voyage) {
        res = new ArrayList();
        index = 0;
        dfs(root, voyage);
        if (!res.isEmpty() && res.get(0) == -1){
            res.clear();
            res.add(-1);
        }
        return res;
    }
    
    private void dfs(TreeNode node, int[] voyage){
        if (node == null){
            return;
        }
        
        if (node.val != voyage[index++]){
            res.clear();
            res.add(-1);
            return;
        }
        
        if (index < voyage.length && node.left != null && node.left.val != voyage[index]){
            res.add(node.val);
            dfs(node.right, voyage);
            dfs(node.left, voyage);
        }else{
            dfs(node.left, voyage);
            dfs(node.right, voyage);
        }
    }
}