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
    void reorderList(ListNode* head) {
        vector<ListNode*> nodes;
        ListNode* temp = head;
        while(temp){
            nodes.push_back(temp);
            temp = temp->next;
        }
        temp = head;
        int n = nodes.size();
        for(int i = 0; i < n/2; i++){
            nodes[i]->next = nodes[n-i-1];
            nodes[n-i-1]->next = nodes[i+1];
        }
        nodes[n/2]->next = NULL;
    }
};
