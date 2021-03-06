---
title:  Redundant Connection
date: 2021-01-04
---
#### In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

```
Example 1:

Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3

Example 2:

Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
```

#### Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.


#### Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused. 

#### Solutions

1. ##### Union Find O(n)

- Return the first edge whose nodes can be merged. ie: they are already connected.

```cpp
class UnionFind {
private:
    int * nodes;
    int * sizes;
public:
    UnionFind(int size) {
        nodes = new int[size];
        sizes = new int[size];
        for (int i = 0; i < size; i++) {
            nodes[i] = i;
            sizes[i] = 1;
        }
    }
    ~UnionFind() {
        delete [] nodes; delete [] sizes;
    }
    int find(int node) {
        while (nodes[node] != node)
            node = nodes[node] = nodes[nodes[node]];
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
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        // the maxinum i will be edges.size(), plus 1, otherwise will cause out of bounds
        UnionFind uf(edges.size() + 1);
        for (auto & e : edges)
            if (!uf.merge(e[0], e[1]))
                return e;
        return {0, 0};
    }
};
```


Or a python version

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            return find(tree[node]) if node in tree else node

        tree = {}
        for i, edge in enumerate(edges):
            f1, f2 = map(find, edge)
            if f1 == f2:
                return edge
            else:
                tree[f1] = f2

```



2. ##### dfs O(n2)

- Use dfs to check if there is a cycle between two nodes after added a new edges into the graph.
- We can also use bfs traversal with queue.

```cpp
class Solution {
public:
    bool hascycle(int src, int target, int pre, vector<vector<int>> & adj) {
        if (src == target)
            return true;
        for (auto & outnode : adj[src]) {
            if (outnode == pre) continue;
            if (hascycle(outnode, target, src, adj))
                return true;
        }
        return false;
    }
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> adj(n, vector<int>());

        for (auto & e : edges) {
            if (hascycle(e[0], e[1], 0, adj))
                return e;
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }

        return {0, 0};
    }
};
```


3. ##### Topological sort

- Reference: https://leetcode-cn.com/problems/redundant-connection/comments/179407
- The idea is to itratively remove nodes with `1` degree, then start checking from the last edge(nodes pair), find the first pair with degree larger than 1.(degrees of both nodes are greater than 1).

```cpp
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> adj(n, vector<int>());
        vector<int> degree(n);

        for (auto & e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
            degree[e[0]]++; degree[e[1]]++;
        }

        queue<int> q;
        vector<bool> visited(n);
        for (int i = 1; i < n; i++)
            if (degree[i] == 1) {
                q.push(i);
                visited[i] = true;
            }

        while (!q.empty()) {
            auto cur = q.front(); q.pop();
            for (auto outnode : adj[cur]) {
                if (visited[outnode]) continue;
                degree[cur]--;
                if (--degree[outnode] == 1) {
                    q.push(outnode);
                    visited[cur] = true;
                }
            }
        }
        // check from the back, find the first nodes pair with degree(minimum of two nodes) greater 1.
        for (int i = edges.size() - 1; i >= 0; i--) {
            auto & e = edges[i];
            if (min(degree[e[0]], degree[e[1]]) > 1)
                return e;
        }

        return {0, 0};
    }
};
```