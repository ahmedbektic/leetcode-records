/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode* next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode* next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == nullptr) return list2;
        if (list2 == nullptr) return list1;

        if (list1->val <= list2->val) {
            list1->next = mergeTwoLists(list1->next, list2);
            return list1;
        }
        else {
            int temp = list1->val;
            list1->val = list2->val;
            list2->val = temp;

            ListNode* dummy1 = list2;
            ListNode* dummy2 = list2->next;
            while (dummy2 != nullptr && dummy1->val > dummy2->val) {
                int temp2 = dummy1->val;
                dummy1->val = dummy2->val;
                dummy2->val = temp2;

                dummy1 = dummy2;
                dummy2 = dummy2->next;
            }
            mergeTwoLists(list1, list2);
            return list1;
        }
    }
};
