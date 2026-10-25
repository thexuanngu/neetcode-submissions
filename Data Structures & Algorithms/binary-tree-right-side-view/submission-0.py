# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        res = []
        q = [root]

        while q:
            children = []
            appended = False
            for e in q:
                if not appended:
                    res.append(e.val)
                    appended = True
                if e.right is not None:
                    children.append(e.right)
                if e.left is not None:
                    children.append(e.left)
            q = children
        return res
