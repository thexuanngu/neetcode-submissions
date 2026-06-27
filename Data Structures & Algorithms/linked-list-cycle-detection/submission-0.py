# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()

        while (head != None):
            if head.next in visited_nodes:
                return True;
            else:
                visited_nodes.add(head)
                head = head.next
        return False 