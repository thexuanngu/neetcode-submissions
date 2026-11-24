# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""We create a dummy node to handle modifications to the head of the linked list, pointing its next pointer to the current head. We then iterate k nodes, storing the address of the next group's head and tracking the tail of the previous group. After reversing the current group, we reconnect it by linking the previous group's tail to the new head and the current group's tail to the next group's head. This process is repeated for all groups, and we return the new head of the linked list. """

class Solution:
    def checkKElementsInvalid(self, head, k):
        """Check there are at least K elements ahead (for reversal)"""
        curr = head
        for _ in range(k):
            if curr is None:
                return True
            curr = curr.next
        return False

    def reverseKElements(self, head, k):
        """Reverse k elements, and return the new head and tail (/ old head)"""
        prev, groupNext = None, head
        for _ in range(k):
            temp = groupNext.next
            groupNext.next = prev
            prev = groupNext
            groupNext = temp
        return prev, head, groupNext

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroupTail, curr = dummy, head
        while curr:
            if self.checkKElementsInvalid(curr, k):
                break
            newHead, newTail, groupNext = self.reverseKElements(curr, k)
            # loop them back in
            prevGroupTail.next = newHead
            newTail.next = groupNext

            # advance pointers
            prevGroupTail = newTail
            curr = groupNext
        return dummy.next
            
        