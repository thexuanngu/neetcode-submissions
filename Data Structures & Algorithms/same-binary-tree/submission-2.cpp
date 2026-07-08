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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<pair<TreeNode*, TreeNode*>> tree_queue;
        tree_queue.push({p, q});
        while (!tree_queue.empty()) {
            TreeNode* node1 = tree_queue.front().first;
            TreeNode* node2 = tree_queue.front().second;
            tree_queue.pop();

            if (node1 == nullptr && node2 == nullptr) continue;
            if (node1 == nullptr || node2 == nullptr) return false;
            if (node1->val != node2->val) return false;
            tree_queue.push({node1->left, node2->left});
            tree_queue.push({node1->right, node2->right});
        }
        return true;
    }
};
