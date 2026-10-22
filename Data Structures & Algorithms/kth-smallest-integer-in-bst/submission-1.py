# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        s = []
        cur = root
        while s or cur:
            while cur:
                s.append(cur)
                cur = cur.left
            cur = s.pop()
            k-=1
            if k == 0:
                return cur.val
            cur = cur.right
            