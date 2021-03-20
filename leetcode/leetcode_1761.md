---
title: 1761. Minimum Degree of a Connected Trio in a Graph
date: 2021-02-14
---

# 1761. Minimum Degree of a Connected Trio in a Graph

You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges, where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.

A connected trio is a set of three nodes where there is an edge between every pair of them.

The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.

Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.

 

Example 1:


Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
Output: 3
Explanation: There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.
Example 2:


Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
Output: 0
Explanation: There are exactly three trios:
1) [1,4,3] with degree 0.
2) [2,5,6] with degree 2.
3) [5,6,7] with degree 2.
 

Constraints:

2 <= n <= 400
edges[i].length == 2
1 <= edges.length <= n * (n-1) / 2
1 <= ui, vi <= n
ui != vi
There are no repeated edges.



##### Solutions

1. ##### straight forward O(n3)

- iterate over all triples.

```c++
class Solution {
public:
    int minTrioDegree(int n, vector<vector<int>>& edges) {
        // build graph
        vector<vector<bool>> g(n + 1, vector<bool>(n + 1));
        vector<int> degree(n + 1);
        for (auto & e : edges) {
            int n1 = e[0], n2 = e[1];
            if (!g[n1][n2]) {
                degree[n1]++; degree[n2]++;
                g[n1][n2] = g[n2][n1] = true;
            }
        }
        // iterate over all triples
        int res = INT_MAX;
        for (int n1 = 1; n1 <= n; n1++)
            for (int n2 = 1; n2 <= n; n2++) {
                if (!g[n1][n2]) continue;
                for (int n3 = 1; n3 <= n; n3++) {
                    if (!(g[n1][n3] && g[n2][n3]))
                        continue;
                    res = min(res, degree[n1] + degree[n2] + degree[n3] - 6);
                }
            }

        return res == INT_MAX ? -1 : res;
    }
};
```