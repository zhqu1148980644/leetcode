---
title: Maximum Depth of N ary Tree
date: 2021-01-04
---
#### Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

```
Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
```

 

#### Constraints:

-    The depth of the n-ary tree is less than or equal to 1000.
-    The total number of nodes is between [0, 10^4].


#### Solutions

1. ##### recursion

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    int maxDepth(Node* root) {
        if (!root) return 0;
        int maxh = 0;
        for (auto child : root->children)
            maxh = max(maxh, maxDepth(child));
        return maxh + 1;
    }
};
```


2. ##### iteration with bfs

```cpp
class Solution {
public:
    int maxDepth(Node* root) {
        queue<Node *> q;
        if(root) q.push(root);
        int maxh = 0;
        while (!q.empty()) {
            int size = q.size();
            maxh++;
            while (size--) {
                root = q.front(); q.pop();
                for (auto & child : root->children)
                    if (child) q.push(child);
            }
        }

        return maxh;
    }
};
```