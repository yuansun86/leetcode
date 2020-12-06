# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(root, low, high):
            if not root:
                return high - low
            left_min = inorder(root.left, low, root.val)
            right_min = inorder(root.right, root.val, high)
            return min(left_min, right_min)
        return inorder(root, float('-inf'), float('inf'))