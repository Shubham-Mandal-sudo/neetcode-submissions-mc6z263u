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
    void preorder(TreeNode* node, vector<int>& store){
        if(node == NULL){
            store.push_back(1000);
            return;
        }
        
        store.push_back(node->val);
        preorder(node->left, store);
        preorder(node->right, store);
    }

    void postorder(TreeNode* node, vector<int>& store){
        if(node == NULL){
            return;
        }
        
        postorder(node->left, store);
        postorder(node->right, store);
        store.push_back(node->val);
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        vector<int> prp;
        vector<int> prq;
        vector<int> pop;
        vector<int> poq;
        preorder(p,prp);
        preorder(q,prq);
        postorder(p,pop);
        postorder(q,poq);
        if(prp == prq && pop==poq){
            return true;
        }
        else{
            return false;
        }
    }
};
