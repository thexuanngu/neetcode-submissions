# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge2List(list1, list2):
    dummy = ListNode()
    curr = dummy

    while list1 or list2:
        if not list1:
            curr.next = list2
            list2 = list2.next
            break;

        elif not list2:
            curr.next = list1
            list1 = list1.next
            break

        else:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
    return dummy.next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        while len(lists) > 1:
            mergedLists = []
            for i in range(len(lists) // 2):
                list1 = lists[2*i]
                list2 = lists[2*i + 1]
                mergedLists.append(merge2List(list1, list2))
            if len(lists) % 2 == 1:
                mergedLists.append(lists[-1])
            lists = mergedLists
        return lists[0]


        # for i in range(1, len(lists)):
        #     list1 = lists[i-1]
        #     list2 = lists[i]
        #     lists[i] = merge2List(list1, list2)
        # return lists[-1]