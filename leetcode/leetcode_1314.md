---
title: Matrix Block Su
date: 2021-01-04
---
Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100


#### Solutions

1. ##### prefix sum O(n)

```cpp
class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int K) {
        int m = mat.size(); if (!m) return {};
        int n = mat[0].size();
        
        vector<vector<int>> sum(m + 1, vector<int>(n + 1));
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                sum[i + 1][j + 1] = mat[i][j] + sum[i][j + 1]  
                                  + sum[i + 1][j] - sum[i][j]; 
        
        vector<vector<int>> res(m, vector<int>(n));
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                int r1 = max(0, i - K);
                int r2 = min(m, i + K + 1);
                int c1 = max(0, j - K);
                int c2 = min(n, j + K + 1);
                res[i][j] = sum[r2][c2] - sum[r1][c2] - sum[r2][c1] + sum[r1][c1];
            }
        
        return res;
    }
};
```