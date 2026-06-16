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
    vector<vector<int>> levelOrder(TreeNode* root) {
        bool flag = true;
        vector<TreeNode*> prev;
        prev.push_back(root);
        vector<vector<int>> res;
        if(root == NULL){
            return res;
        }
        while(flag){
            vector<TreeNode*> temp;
            vector<int> current;
            for(TreeNode* i: prev){
                current.push_back(i->val);
                if(i->left){
                    temp.push_back(i->left);
                }
                if(i->right){
                    temp.push_back(i->right);
                }
            }
            res.push_back(current);
            if(temp.size() == 0){
                flag = false;
            }
            else{
                prev = move(temp);
            }
        }
        return res;
    }
};
