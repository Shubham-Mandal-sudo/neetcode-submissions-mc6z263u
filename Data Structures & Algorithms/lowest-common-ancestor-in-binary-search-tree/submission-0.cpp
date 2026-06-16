/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> pnode;
        vector<TreeNode*> qnode;
        int pnum = p->val;
        int qnum = q->val;
        TreeNode* temp = root;
        while(temp->val != pnum){
            pnode.push_back(temp);
            if(temp->val > pnum){
                temp = temp->left;
            }
            else{
                temp = temp->right;
            }
        }
        pnode.push_back(temp);
        
        temp = root;
        while(temp->val != qnum){
            qnode.push_back(temp);
            if(temp->val > qnum){
                temp = temp->left;
            }
            else{
                temp = temp->right;
            }
        }
        qnode.push_back(temp);

        temp = root;
        for(int i = 0; i < pnode.size() && i < qnode.size(); i++){
            if (pnode[i] == qnode[i]){
                temp = pnode[i];
            }
        }
        return temp;
    }
};
