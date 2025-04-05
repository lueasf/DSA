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
    private:
        TreeNode* candidate;
        int max_dp;
    
        int dfs(TreeNode* node, int depth) {
            if (!node) return -1;
    
            if (!node->left && !node->right) {
                if (depth > max_dp) {
                    max_dp = depth;
                    candidate = node;
                }
                return depth;
            }
    
            int l_dp = dfs(node->left, depth + 1);
            int r_dp = dfs(node->right, depth + 1);
    
            if (l_dp == r_dp && l_dp == max_dp) {
                candidate = node;
            }
    
            return max(l_dp, r_dp);
        }
    
    public:
        TreeNode* lcaDeepestLeaves(TreeNode* root) {
            if (!root) return nullptr;
    
            candidate = nullptr;
            max_dp = -1;
    
            dfs(root, 0);
    
            return candidate;
        }
    };