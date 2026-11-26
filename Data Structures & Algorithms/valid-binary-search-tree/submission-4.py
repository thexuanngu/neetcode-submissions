# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # problem guarantees at least one node exists
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        # dfs -> stack (LIFO) (no need for set because of BST structure)
        q = [(root, -float('inf'), float('inf'))]

        while q:
            node, lowerBound, upperBound = q.pop()

            # check
            if node.val <= lowerBound or node.val >= upperBound:
                return False

            # add
            if node.left:
                q.append((node.left, lowerBound, node.val))
                
            if node.right:
                q.append((node.right, node.val, upperBound))

        return True
            
        