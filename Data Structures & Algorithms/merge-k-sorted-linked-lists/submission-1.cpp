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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* head = NULL;
        ListNode* temp = NULL;
        for(ListNode* i: lists){
            temp = head;
            while(temp && i){
                if(temp->val <= i->val){
                    if(temp->next == NULL){
                        temp->next = i;
                        i = NULL;
                    }
                    else if(temp->next->val > i->val){
                        ListNode* current = i;
                        i = i->next;
                        current->next = temp->next;
                        temp->next = current;
                        temp = current;
                    }
                    else{
                        temp = temp->next;
                    }
                }
                else{
                    if(temp == head){
                        ListNode* current = i;
                        i = i->next;
                        current->next = temp;
                        head = current;
                        temp = current;
                    }
                }
            }
            if(head == NULL){
                head = i;
            }
        } 
        return head;
    }
};
