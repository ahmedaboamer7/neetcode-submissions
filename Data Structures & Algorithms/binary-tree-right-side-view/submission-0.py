# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level = []
            sz = len(q)
            for _ in range(sz):
                nood = q.popleft()
                level.append(nood.val)
                if nood.right: q.append(nood.right)
                if nood.left: q.append(nood.left) 
            res.append(level)
        ans = []
        for i in range(len(res)):
            ans.append(res[i][0])
        return ans
