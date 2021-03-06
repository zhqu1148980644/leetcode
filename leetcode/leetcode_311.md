---
title: Sparse Matrix Multiplication
date: 2021-01-04
---
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
 

Constraints:

1 <= A.length, B.length <= 100
1 <= A[i].length, B[i].length <= 100
-100 <= A[i][j], B[i][j] <= 100


#### Solutions

1. ##### straight forward O(n3)

```cpp
class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        int r1 = A.size(), c1 = A[0].size();
        int r2 = B.size(), c2 = B[0].size();

        vector<vector<int>> res(r1, vector<int>(c2));

        for (int i = 0; i < r1; i++)
            for (int j = 0; j < c1; j++) {
                if (!A[i][j]) continue;
                for (int k = 0; k < c2; k++) {
                    res[i][k] += A[i][j] * B[j][k];
                }
            }

        return res;
    }
};
```

2. ##### sparse multiplication

- `O(n2 + num1 * num2)` num is the number of nonzero elements in each matrix.
- Collect for all non-zero points, and add up the mul of each pair of numbers to their corresponding positions in the final matrix.

```cpp
class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<tuple<int, int, int>> sma1, sma2;
        for (int i = 0; i < A.size(); i++)
            for (int j = 0; j < A[0].size(); j++) {
                if (!A[i][j]) continue;
                sma1.emplace_back(i, j, A[i][j]);
            }
        for (int i = 0; i < B.size(); i++)
            for (int j = 0; j < B[0].size(); j++) {
                if (!B[i][j]) continue;
                sma2.emplace_back(i, j, B[i][j]);
            }
        

        vector<vector<int>> res(A.size(), vector<int>(B[0].size()));

        for (auto [i, m1, val1] : sma1)
            for (auto [m2, j, val2] : sma2) {
                if (m1 == m2)
                    res[i][j] += val1 * val2;
            }
        
        return res;
    }
};
```