---
title: Largest BST Subtree
date: 2021-01-04
---
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?



#### Solutions

1. ##### dynamic programming with postorder traversal

- borrowed from the official answer
- Use postorder traversal to findout the lower bound, upper bound and size of a child node, when both two children's info are available, we can found out if the current tree is a bst by comparing the bound info in `O(1)` time.
    - when the bound info does not satisfy the requirements of bst, the size of the current tree is -1 and is returned to the father node as a mark of not being a bst tree.


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
    int res = 0;
    tuple<int, int, int> dfs(TreeNode * root) {
        // trick, by this way, later steps can be simplified
        if (!root) return {INT_MAX, INT_MIN, 0};
        auto [l1, r1, n1] = dfs(root->left);
        auto [l2, r2, n2] = dfs(root->right);
        // size = -1 represents the subtree is not a bst, thus the father tree is not either
        if (n1 == -1 || n2 == -1 
            || r1 >= root->val 
            || l2 <= root->val)
            return {0, 0, -1};

        res = max(res, n1 + n2 + 1);
        // min/max is used for handling null children
        return {min(root->val, l1), max(root->val, r2), n1 + n2 + 1};
    }

    int largestBSTSubtree(TreeNode* root) {
        auto [l, r, size] = dfs(root);
        return res;        
    }
};
```

or

```cpp
class Solution {
public:
    int res = 0;
    tuple<int, int, int> dfs(TreeNode * root) {
        if (!root) return {INT_MAX, INT_MIN, 0};
        auto [l1, r1, n1] = dfs(root->left);
        auto [l2, r2, n2] = dfs(root->right);
        if (r1 >= root->val || l2 <= root->val)
            return {INT_MIN, INT_MAX, 0};

        res = max(res, n1 + n2 + 1);
        return {min(root->val, l1), max(root->val, r2), n1 + n2 + 1};
    }

    int largestBSTSubtree(TreeNode* root) {
        auto [l, r, size] = dfs(root);
        return res;        
    }
};
```