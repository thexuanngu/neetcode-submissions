# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow = head
        fast = head.next
        while fast:
            fast = fast.next
            if not fast: break
            fast = fast.next
            slow = slow.next
            if fast == slow:
                return True
        return False