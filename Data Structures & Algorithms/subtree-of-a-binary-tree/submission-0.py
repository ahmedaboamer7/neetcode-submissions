# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def sameTree(N1, N2):
            if N1 is None and N2 is None:
                return True
            if N1 and N2 and N1.val == N2.val:
                return sameTree(N1.right, N2.right) and sameTree(N1.left, N2.left)
            return False

        if not subRoot:
            return True
        if not root:
            return False
        
        if sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)  