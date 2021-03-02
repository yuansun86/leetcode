# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.searchNode(root, p, q)
    
    def searchNode(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.searchNode(root.left, p, q)
        right = self.searchNode(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right