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
        int carry = 0;
        int i,j;
        ListNode* head = NULL;
        ListNode* temp = NULL;
        while(l1 && l2){
            if(head == NULL){
                i = l1->val+l2->val+carry;
                j = i % 10;
                carry = i/10;
                temp = new ListNode(j);
                head = temp;
            }
            else{
                i = l1->val+l2->val+carry;
                j = i % 10;
                carry = i/10;
                temp->next = new ListNode(j);
                temp = temp->next;
            }
            l1 = l1->next;
            l2 = l2->next;
        }
        while(l1){
            i = l1->val+carry;
            j = i % 10;
            carry = i/10;
            temp->next = new ListNode(j);
            l1 = l1->next;
            temp = temp->next;
        }
        while(l2){
            i = l2->val+carry;
            j = i % 10;
            carry = i/10;
            temp->next = new ListNode(j);
            l2 = l2->next;
            temp = temp->next;
        }
        if(carry){
            temp->next = new ListNode(carry);
        }
        return head;
    }
};
