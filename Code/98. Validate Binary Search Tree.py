class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            # make inorder array of DFS. Remember, DFS has preorder, inorder, and postorder.
            # Preorder means visiting root first, then left-subtree, then right-subtree
            # Inorder means visiting left-subtree, then root, then right-subtree
            # Postorder means visiting left_subtree, then right-subtree, and then root
            if not root:
                return []
            else:
                return inorder(root.left) + [root.val] + inorder(root.right)
        
        inorder_list = inorder(root)
        for i in range(len(inorder_list)-1):
            if inorder_list[i] >= inorder_list[i+1]:
                # a binary search tree should in ascending order for its inorder traverse result
                return False
        return True