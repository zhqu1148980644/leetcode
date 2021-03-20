---
title: 1782. Count Pairs Of Nodes
date: 2021-03-06
---

# 1782. Count Pairs Of Nodes

You are given an undirected graph represented by an integer n, which is the number of nodes, and edges, where edges[i] = [ui, vi] which indicates that there is an undirected edge between ui and vi. You are also given an integer array queries.

The answer to the jth query is the number of pairs of nodes (a, b) that satisfy the following conditions:

a < b
cnt is strictly greater than queries[j], where cnt is the number of edges incident to a or b.
Return an array answers such that answers.length == queries.length and answers[j] is the answer of the jth query.

Note that there can be repeated edges.

 

Example 1:


Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
Output: [6,5]
Explanation: The number of edges incident to at least one of each pair is shown above.
Example 2:

Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
Output: [10,10,9,8,6]
 

Constraints:

2 <= n <= 2 * 104
1 <= edges.length <= 105
1 <= ui, vi <= n
ui != vi
1 <= queries.length <= 20
0 <= queries[j] < edges.length

#### Solutions

- `a < b` means edge `(a, b)` and `(b, a)` should not be counted twice.
- `repeated edges` means there may be multiple undirected edges between two nodes, and should not be dropped.

1. ##### two pointers after sort

- Firstly use two pointers(based on sorted degree array) to count node pairs satisfying the requirements without considering inner edges.
    - `degree(a, b) = degree(a) + degree(b) - num_edges(a, b)`
- Then loop through all edges to count for the repeated counts due to inner edges.

```c++
class Solution {
public:
    vector<int> countPairs(int n, vector<vector<int>>& edges, vector<int>& queries) {
        unordered_map<int, int> m;
        vector<int> degree(n);

        for (auto & e : edges) {
            if (e[0] > e[1]) swap(e[0], e[1]);
            auto h = (e[0] - 1) * n + (e[1] - 1);
            m[h]++;
            degree[e[0] - 1]++;
            degree[e[1] - 1]++;
        }

        vector<int> sorted(degree);
        sort(sorted.begin(), sorted.end());
        vector<int> res;
        for (auto q : queries) {
            int cur = 0;
            for (int i = 0; i < n; i++) {
                // another option is to start bisearch from the start of the array,
                // in this case, node pairs are counted twice, and with plus one(self pair).
                int hi = upper_bound(sorted.begin() + i + 1, sorted.end(), q - sorted[i]) 
                    - sorted.begin();
                cur += max(0, n - hi);
            }
            for (auto [h, cnt] : m) {
                int n1 = h / n, n2 = h % n;
                if (degree[n1] + degree[n2] > q && degree[n1] + degree[n2] - cnt <= q) {
                    cur--;
                }
            }
            res.push_back(cur);
        }
        return res;
    }
};
```