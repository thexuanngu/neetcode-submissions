# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = deque([root])

        while q:
            temp = []
            children = []
            for e in q:
                temp.append(e.val)
                if e.left:
                    children.append(e.left)
                if e.right:
                    children.append(e.right)
            res.append(temp)
            q = children
        return res



        