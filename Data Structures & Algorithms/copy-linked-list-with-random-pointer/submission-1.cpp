/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return NULL;
        
        unordered_map<Node*, Node*> mp;
        Node* temp = head;
        
        // Step 1: Create all new nodes and map old nodes to new nodes
        while (temp) {
            mp[temp] = new Node(temp->val);
            temp = temp->next;
        }
        
        // Step 2: Connect the next and random pointers for the new nodes
        temp = head;
        while (temp) {
            mp[temp]->next = mp[temp->next];
            mp[temp]->random = mp[temp->random];
            temp = temp->next;
        }
        
        return mp[head];
    }
};
