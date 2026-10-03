# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root,1)]
        depth = 1
        tempDepth = 1
        if not root:
            return 0
        while stack:
            node , tempDepth = stack.pop()
            if node.right:
                stack.append((node.right,tempDepth+1))
            if node.left:
                stack.append((node.left,tempDepth+1))
            depth = max(depth,tempDepth)
        return depth