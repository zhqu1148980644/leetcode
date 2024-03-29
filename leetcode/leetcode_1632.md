---
title: 1632. Rank Transform of a Matrix
date: 2021-01-04
---
# 1632. Rank Transform of a Matrix
Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

If an element is the smallest element in its row and column, then its rank is 1.
If two elements p and q are in the same row or column, then:
If p < q then rank(p) < rank(q)
If p == q then rank(p) == rank(q)
If p > q then rank(p) > rank(q)
The rank should be as small as possible.
It is guaranteed that answer is unique under the given rules.

 

Example 1:


Input: matrix = [[1,2],[3,4]]
Output: [[1,2],[2,3]]
Explanation:
The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.
Example 2:


Input: matrix = [[7,7],[7,7]]
Output: [[1,1],[1,1]]
Example 3:


Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
Example 4:


Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
Output: [[5,1,4],[1,2,3],[6,3,1]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 500
-109 <= matrix[row][col] <= 109


#### Solutions

1. ##### greedy approach with union find O(mnlog(mn))

- reference: https://leetcode-cn.com/problems/rank-transform-of-a-matrix/solution/xun-zhao-lian-tong-fen-liang-by-time-limit/
- To make the rank be as small as possible and ensuring `rank(p) > rank(q)` if `p > q`. We can fill the rank table from points with smaller values to points with larger values.
- However, the second requirement states that `rank(q) == rank(q)` if `p == q`, for a given value, there may be multiple points canbe grouped into several groups based on their connectivity, and ranks in the same group should be equal to each other.

```cpp
struct UnionFind {
    vector<int> nodes;
    UnionFind(int size) : nodes(size) {}
    int find(int node) {
        return nodes[node] == node ?
            node : (nodes[node] = find(nodes[node]));
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
    vector<vector<int>> matrixRankTransform(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        // group points with the same value
        unordered_map<int, vector<pair<int, int>>> valsm;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                valsm[matrix[i][j]].emplace_back(i, j);
        // sort in ascending order by value
        vector<int> vals;
        for (auto & [val, pos] : valsm)
            vals.push_back(val);
        sort(vals.begin(), vals.end());
        // rmaxrank represents the maximum rank has been settled in each row
        vector<vector<int>> res(m, vector<int>(n));
        vector<int> rmaxrank(m), cmaxrank(n);
        UnionFind uf(m + n);

        // setting ranks from the smallest value to the largest.
        for (auto val : vals) {
            // re-initialize UnionFind
            iota(uf.nodes.begin(), uf.nodes.end(), 0);
            // To cater for the second requirement: if p == q, then rank(p) == rank(q)
            // connect ponints into different groups/communities
            for (auto [r, c] : valsm[val])
                uf.merge(r, c + m);
            // collect points within the same group
            unordered_map<int, vector<pair<int, int>>> groups;
            for (auto [r, c] : valsm[val])
                groups[uf.find(r)].emplace_back(r, c);
            // points within the same group should have the same rank
            for (auto & [_, points] : groups) {
                int maxrank = 0;
                for (auto [x, y] : points)
                    maxrank = max(maxrank, max(rmaxrank[x], cmaxrank[y]));
                // ensure rank(q) > rank(p) if p > q
                for (auto [x, y] : points)
                    rmaxrank[x] = cmaxrank[y] = res[x][y] = maxrank + 1;
            }
        }

        return res;
    }
};
```