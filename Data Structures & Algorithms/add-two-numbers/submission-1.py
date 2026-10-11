# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        carry = 0
        dummy = ListNode()
        cur = dummy
        while cur1 and cur2:
            curSum = cur1.val + cur2.val + carry
            
            if curSum > 9:
                carry = 1
                curSum %= 10
            else:
                carry = 0
            cur.next = ListNode(curSum)
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next

        while cur1:
            curSum = cur1.val + carry
            if curSum > 9:
                carry = 1
                curSum %= 10
            else:
                carry = 0
            cur.next = ListNode(curSum)
            cur = cur.next
            cur1 = cur1.next

        while cur2:
            curSum = cur2.val + carry
            if curSum > 9:
                carry = 1
                curSum %= 10
            else:
                carry = 0
            cur.next = ListNode(curSum)
            cur = cur.next
            cur2 = cur2.next
        if carry != 0:
            cur.next = ListNode(carry)
            cur = cur.next
        return dummy.next
            
