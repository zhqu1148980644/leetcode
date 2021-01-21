---
title: 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
date: 2021-01-21
---

# 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

 

Example 1:



Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
Example 2:



Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
 

Constraints:

2 <= n <= 100
1 <= edges.length <= min(200, n * (n - 1) / 2)
edges[i].length == 3
0 <= ai < bi < n
1 <= weighti <= 1000
All pairs (ai, bi) are distinct.


#### Solutions

- Note that the MST is not unique, there may be many MSTs satisfy the definition of MST:
    - minimum sum edge weights.
    - no cycle(no redundant edge)
- After removing a certain `critical edge`, there are two cases:
    - The remaining graph is splitted into multiple non-connected graph.
    - The MST of the remaining graph has sum weights greater than the MST of the original graph.
- pseudo-critical edge:
    - is a part of some MST(since MST is not unique).
    - is non-critical edge(Still remain other MST when being removed).

1. ##### brute force O(n2)

- reference: the official answer
- The idea is to check for all edges.
- Use `kruskal` algorithm to build the MST.
    - build the graph starting with edges of small weights non-redundantly.

```c++
struct UnionFind {
    vector<int> nodes, sizes;
    UnionFind(int size) : nodes(size), sizes(size, 1) {
        iota(nodes.begin(), nodes.end(), 0);
    }
    int find(int n) {
        return nodes[n] == n ? n : (nodes[n] = find(nodes[nodes[n]]));
    }
    bool merge(int n1, int n2) {
        int f1 = find(n1), f2 = find(n2);
        if (f1 == f2) return false;
        nodes[f1] = f2;
        return true;
    }
};
class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        // store the original index as the fourth element in each edge
        for (int i = 0; i < edges.size(); i++)
            edges[i].push_back(i);

        // build the MST by kruskal algorithm
        sort(edges.begin(), edges.end(), [](auto & e1, auto & e2) {
            return e1[2] < e2[2];
        });
        UnionFind uf(n);
        int minval = 0;
        for (int i = 0; i < edges.size(); i++) {
            int n1 = edges[i][0], n2 = edges[i][1], w = edges[i][2];
            if (uf.merge(n1, n2))
                minval += w;
        }

        // iterate over all edges
        vector<vector<int>> res {{}, {}};
        for (int i = 0; i < edges.size(); i++) {
            // check if critical edge
            iota(uf.nodes.begin(), uf.nodes.end(), 0);
            int comsize = n, val = 0;
            for (int j = 0; j < edges.size(); j++) {
                int n1 = edges[j][0], n2 = edges[j][1], w = edges[j][2];
                if (i != j && uf.merge(n1, n2)) {
                    comsize--;
                    val += w;
                }
            }
            if (comsize != 1 || val > minval) {
                res[0].push_back(edges[i][3]);
                continue;
            }
            
            // check if pseudo-critical edge
            iota(uf.nodes.begin(), uf.nodes.end(), 0);
            // must use the current edge.
            uf.merge(edges[i][0], edges[i][1]);
            comsize = n - 1; val = edges[i][2];
            for (int j = 0; j < edges.size(); j++) {
                int n1 = edges[j][0], n2 = edges[j][1], w = edges[j][2];
                if (i != j && uf.merge(n1, n2)) {
                    comsize--;
                    val += w;
                }
            }
            // with the same weight as the MST of the original graph.
            if (comsize == 1 && val == minval)
                res[1].push_back(edges[i][3]);
            
        }

        return res;

    }
};
```

2. ##### Tarjan

- NEED TO BE DONE
- check the official answer.