class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while (list1 is not None or list2 is not None):
            if (list1 is None):
                curr.next = list2
                break
            elif (list2 is None):
                curr.next = list1
                break
            else:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
        return dummy.next