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
    void checker(TreeNode* node, bool& var, int& prev){
        if (var == false || node == NULL){
            return;
        }
        if (node->right && node->val >= node->right->val){
            var = false;
            return;
        }
        if (node->left && node->val <= node->left->val){
            var = false;
            return;
        }
        checker(node->left, var, prev);
        if(prev == 9999){
            prev = node->val;
        }
        else if(prev >= node->val){
            var = false;
            return;
        }
        else{
            prev = node->val;
        }
        checker(node->right, var, prev);
    }
public:
    bool isValidBST(TreeNode* root) {
        bool res = true;
        int var = 9999;
        checker(root, res, var);
        return res;
    }
};
