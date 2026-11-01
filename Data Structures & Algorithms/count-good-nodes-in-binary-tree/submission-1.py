# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        dq = deque([(root, root.val)])

        while dq:
            node, curMax = dq.popleft()
            if node.val >= curMax:
                counter += 1
            if node.left is not None:
                leftMax = max(curMax, node.left.val)
                dq.append((node.left, leftMax))
            if node.right is not None:
                rightMax = max(curMax, node.right.val)
                dq.append((node.right, rightMax))
        return counter
            
