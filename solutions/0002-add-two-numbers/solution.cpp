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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* temp = new ListNode;
        ListNode* head = temp;
        bool carry = false;
        bool something = true;
        bool firstIteration = true;

        int val1, val2;

        while (something) {
            if (!firstIteration) {
                ListNode* next = new ListNode;
                temp->next = next;
                temp = temp->next;
                next = nullptr;
                delete next;
            }
            else firstIteration = false;

            if (l1 != nullptr) val1 = l1->val;
            else val1 = 0;
            if (l2 != nullptr) val2 = l2->val;
            else val2 = 0;

            int placeSum = val1 + val2 + carry;
            if (placeSum >= 10) {
                carry = true;
                placeSum = placeSum - 10;
            }
            else carry = false;

            temp->val = placeSum;

            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;

            if (l1 != nullptr || l2 != nullptr || carry) something = true;
            else something = false;
        }

        return head;
    }
};
