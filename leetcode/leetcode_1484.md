---
title: Clone Binary Tree With Random Pointer
date: 2021-01-04
---
A binary tree is given such that each node contains an additional random pointer which could point to any node in the tree or null.

Return a deep copy of the tree.

The tree is represented in the same input/output way as normal binary trees where each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (in the input) where the random pointer points to, or null if it does not point to any node.
You will be given the tree in class Node and you should return the cloned tree in class NodeCopy.

 

Example 1:


Input: root = [[1,null],null,[4,3],[7,0]]
Output: [[1,null],null,[4,3],[7,0]]
Explanation: The original binary tree is [1,null,4,7].
The random pointer of node one is null, so it is represented as [1, null].
The random pointer of node 4 is node 7, so it is represented as [4, 3] where 3 is the index of node 7 in the tree array.
The random pointer of node 7 is node 1, so it is represented as [7, 0] where 0 is the index of node 1 in the tree array
Example 2:


Input: root = [[1,4],null,[1,0],null,[1,5],[1,5]]
Output: [[1,4],null,[1,0],null,[1,5],[1,5]]
Explanation: The random pointer of a node can be the node itself.
Example 3:


Input: root = [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]
Output: [[1,6],[2,5],[3,4],[4,3],[5,2],[6,1],[7,0]]
Example 4:

Input: root = []
Output: []
Example 5:

Input: root = [[1,null],null,[2,null],null,[1,null]]
Output: [[1,null],null,[2,null],null,[1,null]]
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
Each node's value is between [1, 10^6].

#### Solutions

- Similar to `problem 138 copy list with random pointer`.

1. ##### recursion with hashmap

```cpp
/**
 * Definition for a binary tree node.
 * struct Node {
 *     int val;
 *     Node *left;
 *     Node *right;
 *     Node *random;
 *     Node() : val(0), left(nullptr), right(nullptr), random(nullptr) {}
 *     Node(int x) : val(x), left(nullptr), right(nullptr), random(nullptr) {}
 *     Node(int x, Node *left, Node *right, Node *random) : val(x), left(left), right(right), random(random) {}
 * };
 */
class Solution {
public:
    unordered_map<Node *, NodeCopy *> m = {{nullptr, nullptr}};
    NodeCopy * copy(Node * root) {
        if (m.count(root))
            return m[root];
        NodeCopy * newroot = new NodeCopy(root->val);
        m[root] = newroot;
        newroot->left = copy(root->left);
        newroot->right = copy(root->right);
        newroot->random = copy(root->random);
        return newroot;
    } 
    NodeCopy* copyRandomBinaryTree(Node* root) {
        return copy(root);
    }
};
```