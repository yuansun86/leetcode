# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found_p, found_q, node =  self.find(root, p, q)
        if found_p and found_q:
            return node
        return None
    
    def find(self, root, p, q):
        if not root:
            return False, False, None
        
        left_p, left_q, left_res = self.find(root.left, p, q)
        right_p, right_q, right_res = self.find(root.right, p, q)
        found_p = left_p or right_p or root == p
        found_q = left_q or right_q or root == q
        if root == p or root == q:
            return found_p, found_q, root
        if left_res and right_res:
            return found_p, found_q, root
        if left_res:
            return found_p, found_q, left_res
        if right_res:
            return found_p, found_q, right_res
        return found_p, found_q, None
        