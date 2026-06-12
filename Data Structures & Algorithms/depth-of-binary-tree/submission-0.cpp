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
    void depth_counter(TreeNode* node, int pres, int* res){
        if(node == NULL){
            *res = max(pres,*res);
            return;
        }
        depth_counter(node->left, pres+1, res);
        depth_counter(node->right, pres+1, res);
    }
    int maxDepth(TreeNode* root) {
        int res = 0;
        int pres = 0;
        depth_counter(root, pres, &res);
        return res;
    }
};
