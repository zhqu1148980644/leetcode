---
title: Longest Increasing Path in a Matrix
date: 2021-01-04
---
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


#### Solutions

1. ##### recursion with memoization O(n2) S(n2)

- Note that the searching path will never be acrossed with nodes visited before, thus the ensureing the correctness in each dp step(implemented by recursion).

```cpp
class Solution {
public:
    int m, n;
    vector<vector<int>> dp, matrix;
    int search(int i, int j, int prev) {
        if (i < 0 || j < 0 || i >= m || j >= n || prev >= matrix[i][j])
            return 0;
        if (dp[i][j]) return dp[i][j];
        int cur = matrix[i][j];
        return dp[i][j] = 1 + max({
            search(i + 1, j, cur),
            search(i, j + 1, cur),
            search(i - 1, j, cur),
            search(i, j - 1, cur)
        });
    }

    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size(); if (!m) return 0;
        n = matrix[0].size();

        int res = 1;
        this->matrix = move(matrix);
        dp = vector<vector<int>>(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                res = max(res, search(i, j, INT_MIN));

        return res;
    }
};
```


2. ##### dynamic programming

- Sort then traverse all pixels in descending order to ensure dependent states are always been calculated before.

```cpp
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix.size(); if (!m) return 0;
        int n = matrix[0].size();

        vector<tuple<int, int, int>> pixels;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                pixels.emplace_back(matrix[i][j], i, j);
        sort(pixels.rbegin(), pixels.rend());

        int res = 0;
        vector<vector<int>> dp(m, vector<int>(n));
        int dirs[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        // solve dp(val) in descending order
        for (auto [val, x, y] : pixels) {
            int inc = 0;
            for (auto & d : dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx < 0 || ny < 0 || nx >= m || ny >= n 
                    || matrix[nx][ny] <= val)
                    continue;
                inc = max(inc, dp[nx][ny]);
            }
            res = max(res, dp[x][y] = inc + 1);
        }

        return res;
    }
};
```