# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # brute force -> visit every node, sort, then get the kthSmallest

        vals = []
        q = [root]

        while q:
            node = q.pop()

            vals.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        vals.sort()
        return vals[k-1]

        
