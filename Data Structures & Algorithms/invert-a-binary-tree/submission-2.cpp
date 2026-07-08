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
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) return nullptr;
        stack<TreeNode *> tree_stack;
        tree_stack.push(root);
        while (!tree_stack.empty()) {
            TreeNode * node = tree_stack.top();
            tree_stack.pop();
            swap(node->left, node->right);
            if (node->left) tree_stack.push(node->left);
            if (node->right) tree_stack.push(node->right);
        }
        return root;
    }
};
