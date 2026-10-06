/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // first pass -> get length of list
        ListNode* current = head;
        int length = 1;
        while (current->next != nullptr) {
            current = current->next;
            length++;
        }


        ListNode* prev = nullptr;
        current = head;
        for (int i = 0; i < length; i++) {

            if (i == length - n) {
                if (i == 0) {
                    ListNode* duplicateNode = head;
                    head=head->next;
                    delete duplicateNode;
                    return head;
                }
                prev->next = current->next;
                delete current;
                return head;
            }
            prev = current;
            current = current->next;

            // // n = 1
            // if (n == 1) {
            //     ListNode* duplicateNode = head;
            //     head=head->next;
            //     delete duplicateNode;
            //     return head;
            // }
            // // if (n == 2) {
            // //     ListNode* duplicateNode = head->next;
            // //     head->next = head->next->next;
            // //     delete duplicateNode;
            // //     return head;

            // // }

            // if (i == n-1) {
            //     prev->next = (current->next != nullptr) ? current->next : nullptr;
            //     delete current;
            //     return head;
            // }

            // prev = current;
            // current = current->next;
            
            // 
        }
    }
};
