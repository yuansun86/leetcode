/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    Map<TreeNode, List<TreeNode>> graph;
    
    
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        graph = new HashMap();
        List<Integer> res = new ArrayList<>();
        generateGraph(root, null);
        
        Deque<TreeNode> queue = new LinkedList();
        Set<TreeNode> visited = new HashSet();
        queue.add(target);
        visited.add(target);
        int dist = 0;
        while (!queue.isEmpty()){
            int loops = queue.size();
            if (dist == K)break;
            for (int i = 0; i < loops; i++){
                TreeNode node = queue.pollFirst();
                for (TreeNode neighbor: graph.get(node)){
                    if (visited.contains(neighbor)){
                        continue;
                    }
                    queue.add(neighbor);
                    visited.add(neighbor);
                }
            }
            dist++;
        }
        
        for (TreeNode node: queue){
            res.add(node.val);
        }
        return res;
    }
    
    private void generateGraph(TreeNode node, TreeNode parent){
        if (node == null) return;
        
        List<TreeNode> entry;
        if (!graph.containsKey(node)){
            entry = new ArrayList<>();
        }else{
            entry = graph.get(node);
        }
        
        if (node.left != null){
            entry.add(node.left);
        }
        if (node.right != null){
            entry.add(node.right);
        }
        if (parent != null){
            entry.add(parent);
        }
        graph.put(node, entry);
        
        generateGraph(node.left, node);
        generateGraph(node.right, node);       
    }
}