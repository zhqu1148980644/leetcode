---
title: House Robber III
date: 2021-01-04
---
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.


#### Solutions

1. ##### dynamic programming with postorder traversal

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    pair<int, int> dp(TreeNode * root) {
        if (!root) return {0, 0};
        auto [y1, n1] = dp(root->left);
        auto [y2, n2] = dp(root->right);
        return {
            n1 + n2 + root->val,
            max(y1, n1) + max(y2, n2)
        };
    }
    int rob(TreeNode* root) {
        // y represents the maximum score when robbing the current node
        // n represents the                    not robbing
        auto [y, n] = dp(root);
        return max(y, n);        
    }
};
```