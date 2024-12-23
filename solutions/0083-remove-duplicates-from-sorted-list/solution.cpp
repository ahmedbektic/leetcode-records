class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        for (ListNode* cur = head; cur && cur->next; ) 
            if (cur->val == cur->next->val) { ListNode* dup = cur->next; cur->next = dup->next; delete dup; } 
            else cur = cur->next;
        return head;
    }
};

