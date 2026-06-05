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
        Node* temp = head;
        int n = 0;
        vector<Node*> nodes;
        vector<Node*> random;

        while(temp){
            nodes.push_back(temp);
            random.push_back(temp->random);
            n++;
            temp = temp->next;
        }
        vector<int> index(n,-1);
        int c = 0;
        for(Node* i : random){
            if(i){
                auto it = find(nodes.begin(), nodes.end(), i);
                index[c] = distance(nodes.begin(), it);
            }
            c++;
        }
        temp = NULL;
        Node* nhead = NULL;
        vector<Node*> nodes1;
        for(int i = 0; i < n; i++){
            if(temp == NULL){
                temp = new Node(nodes[i]->val);
                nhead = temp;
                nodes1.push_back(temp);
            }
            else{
                temp->next = new Node(nodes[i]->val);
                nodes1.push_back(temp->next);
                temp = temp->next;
                
            }
        }
        for(int i = 0; i < n; i++){
            if(random[i]){
                nodes1[i]->random = nodes1[index[i]];
            }
        }
        return nhead;
    }
};
