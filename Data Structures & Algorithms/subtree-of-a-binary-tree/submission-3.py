# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(node1, node2):
    if node1 == None and node2 == None: return True
    if node1 == None or node2 == None: return False
    if node1.val != node2.val: # and node2 is not None
        return False
    return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None: return True
        if not root and subRoot: return False
        q = [root]
        while q:
            node = q.pop()
            if isSameTree(node, subRoot):
                return True
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
        return False

            



