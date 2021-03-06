---
title: Minimize Malware Sprea
date: 2021-01-04
---
In a network of nodes, each node i is directly connected to another node j if and only if graph[i][j] = 1.

Some nodes initial are initially infected by malware.  Whenever two nodes are directly connected and at least one of those two nodes is infected by malware, both nodes will be infected by malware.  This spread of malware will continue until no more nodes can be infected in this manner.

Suppose M(initial) is the final number of nodes infected with malware in the entire network, after the spread of malware stops.

We will remove one node from the initial list.  Return the node that if removed, would minimize M(initial).  If multiple nodes could be removed to minimize M(initial), return such a node with the smallest index.

Note that if a node was removed from the initial list of infected nodes, it may still be infected later as a result of the malware spread.



```
Example 1:

Input: graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
Output: 0

Example 2:

Input: graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
Output: 0

Example 3:

Input: graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
Output: 1
```



#### Note:

-    1 < graph.length = graph[0].length <= 300
-    0 <= graph[i][j] == graph[j][i] <= 1
-    graph[i][i] = 1
-    1 <= initial.length < graph.length
-    0 <= initial[i] < graph.length


#### Solutions

- According to the spreading rules, any communities containing at least one infected node will eventually become infected for the whole community.
- Since we can only erase one node, if a community contains more than two nodes which are infected initially, removing neither one of them will do nothing to help reduce the number of infected nodes at the end.
- Thus removing the node whose community contains only one infected node(itself) can minimize the final number of malware. To minimize M(initial) as much as possible, we choose the largest community satisfy the above requirements.

1. ##### dfs with recursion



2. ##### Union Find

```cpp
struct UnionFind {
    int * sizes;
    int * nodes;
    UnionFind(int size) {
        sizes = new int[size];
        nodes = new int[size];
        for (int i = 0; i < size; i++) {
            sizes[i] = 1;
            nodes[i] = i;
        }
    }
    int find(int node) {
        while (nodes[node] != node) {
            nodes[node] = nodes[nodes[node]];
            node = nodes[node];
        }
        return node;
    }
    bool merge(int node1, int node2) {
        int f1 = find(node1);
        int f2 = find(node2);
        if (f1 == f2)
            return false;
        else {
            if (sizes[f1] > sizes[f2])
                swap(f1, f2);
            nodes[f1] = f2;
            sizes[f2] += sizes[f1];
            return true;
        }
    }
};


class Solution {
public:
    int minMalwareSpread(vector<vector<int>>& graph, vector<int>& initial) {
        UnionFind uf(graph.size());
        
        int len = graph.size();
        for (int i = 0; i < len; i++)
            for (int j = i + 1; j < len; j++)
                if (graph[i][j] == 1)
                    uf.merge(i, j);
        // count the number of infected nodes in each community
        vector<int> count(len);
        for (auto & node : initial)
            count[uf.find(node)]++;

        // find the lagest community containing only one infected node.
        int maxsize = INT_MIN;
        int resnode = -1;
        int minnode = INT_MAX;
        for (auto & node : initial) {
            if (node < minnode)
                minnode = node;
            int com = uf.find(node);
            if (count[com] = 1) {
                if (uf.sizes[com] > maxsize 
                || (uf.sizes[com] == maxsize && node < resnode)) {
                    resnode = node;
                    maxsize = uf.sizes[com];
                }
            }
        }
        // No communities satisfy the rule, rethen the minimum node.
        return resnode == -1 ? minnode : resnode;
    }
};
```