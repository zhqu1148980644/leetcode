---
title: 399. Evaluate Division
date: 2021-01-04
---


# 399. Evaluate Division

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.

#### Solutions

1. ##### UnionFind

- `A / C` can be derived from `A / B` and `B / C`, and this chain can be stored in an directed graph.
- Use `UnionFind` data structure to check connectivity between two variables in `O(1)` time.
- Use recursion to find a valid path between them and calculate the chaining result at the same time.


```c++
struct UnionFind {
    vector<int> nodes;
    UnionFind(int size) : nodes(size) {
        iota(nodes.begin(), nodes.end(), 0);
    }
    int find(int node) {
        return nodes[node] == node 
        ? node 
        : (nodes[node] = find(nodes[nodes[node]]));
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
    template <typename G>
    double search(G & g, int src, int tgt, int prev) {
        if (src == tgt) return 1;
        if (g[src].count(tgt))
            return g[src][tgt];
        for (auto [ch, cur] : g[src]) {
            if (ch == prev) continue;
            double left = search(g, ch, tgt, src);
            if (left != -1)
                return cur * left;
        }
        return -1;
    }

    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        int id = 1;
        // used for check conectivity in near O(1) time
        UnionFind uf(41);
        unordered_map<string, int> vars;
        // directed graph
        unordered_map<int, unordered_map<int, double>> g;

        for (int i = 0; i < equations.size(); i++) {
            auto & eq = equations[i];
            auto & a = eq[0], & b = eq[1];
            if (!vars.count(a))
                vars[a] = id++;
            if (!vars.count(b))
                vars[b] = id++;
            int n1 = vars[a], n2 = vars[b];
            uf.merge(n1, n2);
            auto val = values[i];
            g[n1][n2] = val;
            g[n2][n1] = 1.0 / val;
        }

        vector<double> res;
        for (auto & q : queries) {
            int n1 = vars[q[0]], n2 = vars[q[1]];
            if (n1 == 0 || n2 == 0 || uf.find(n1) != uf.find(n2))
                res.push_back(-1);
            else
                res.push_back(search(g, n1, n2, -1));
        }

        return res;
    }
};
```

##### 3. Floyd



##### 2. UnionFind with edge merge


