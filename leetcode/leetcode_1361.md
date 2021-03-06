---
title:  Validate Binary Tree Nodes
date: 2021-01-04
---
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

```
Example 1:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:

Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Example 4:

Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false
```

 

#### Constraints:

-    1 <= n <= 10^4
-    leftChild.length == rightChild.length == n
-    -1 <= leftChild[i], rightChild[i] <= n - 1

#### Solutions

1. ##### Union Find

- `numedges == n - 1`
- no cycle
- all nodes are connected(one community).

```cpp
struct UnionFind {
    vector<int> nodes;
    UnionFind(int n) : nodes(n) {
        iota(nodes.begin(), nodes.end(), 0);
    }
    int find(int node) {
        return nodes[node] == node ? node : (nodes[node] = find(nodes[node]));
    }
    bool merge(int node1, int node2) {
        int f1 = find(node1), f2 = find(node2);
        if (f1 == f2) return false;
        nodes[f1] = f2;
        return true;
    }
};
class Solution {
public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        vector<int> indegree(n);
        UnionFind uf(n);
        int com = n;
        for (int i = 0; i < n; i++) {
            if (leftChild[i] != -1) {
                indegree[leftChild[i]]++;
                if (uf.merge(i, leftChild[i]))
                    com--;
                else return false;
            }
            if (rightChild[i] != -1) {
                indegree[rightChild[i]]++;
                if (uf.merge(i, rightChild[i]))
                    com--;
                else return false;
            }
        }

        return com == 1;
    }
};
```

2. ##### another method

```cpp
class Solution {
public:
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) {
        int edge = 0;
        vector<int> indeg(n), outdeg(n);
        for (int i = 0; i < n; i++) {
            if (leftChild[i] != -1) {
                edge++; outdeg[i]++;
                indeg[leftChild[i]]++;
            }
            if (rightChild[i] != -1) {
                edge++; outdeg[i]++;
                indeg[rightChild[i]]++;
            }
        }
        // check ig edge == n - 1
        if (edge != n - 1) return false;
        int root = -1;
        for (int i = 0; i < n; i++) {
            // there are at most 1 root node
            if (indeg[i] == 0) {
                if (root != -1) return false;
                root = i;
            }
            // no nodes has more than 1 indgree
            else if (indeg[i] != 1)
                return false;
        }
        // must has one root, and outdegree of root node must >= 0;
        // except sinleone case
        return root != -1 && (n == 1 || outdeg[root]);
    }
};
```

