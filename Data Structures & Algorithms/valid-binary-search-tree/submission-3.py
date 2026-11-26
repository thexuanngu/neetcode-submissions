# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # problem guarantees at least one node exists
        # immediately check
        
        # dfs -> stack (LIFO)
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


            # if node.left:
            #     if node.left.val >= lowerBound:
            #         return False
            #     else:
            #         if node.left not in seen:
            #             seen.add(node.left)
            #             q.append((node.left, lowerBound, node.left.val))
            # if node.right:
            #     if node.right.val <= node.val:
            #         return False
            #     else:
            #         if node.right not in seen:
            #             seen.add(node.right)
            #             q.append((node.right, lowerBound, node.right))
        return True
            
        