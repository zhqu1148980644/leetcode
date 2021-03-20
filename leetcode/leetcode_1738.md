---
title: 1738. Find Kth Largest XOR Coordinate Value
date: 2021-01-24
---

# 1738. Find Kth Largest XOR Coordinate Value

You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the kth largest value (1-indexed) of all the coordinates of matrix.

 

Example 1:

Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
Example 2:

Input: matrix = [[5,2],[1,6]], k = 2
Output: 5
Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
Example 3:

Input: matrix = [[5,2],[1,6]], k = 3
Output: 4
Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.
Example 4:

Input: matrix = [[5,2],[1,6]], k = 4
Output: 0
Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which is the 4th largest value.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 106
1 <= k <= m * n


#### Solutions

1. ##### dynamic programming O(n2)

- Similar to calculate the range sum in 2d-matrix.


```c++
class Solution {
public:
    int kthLargestValue(vector<vector<int>>& matrix, int k) {
        int m = matrix.size(), n = matrix[0].size();
        
        // O(m * n)
        vector<int> nums;
        vector<vector<int>> res(m + 1, vector<int>(n + 1));
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                res[i + 1][j + 1] = matrix[i][j] ^ res[i][j + 1] ^ res[i + 1][j] ^ res[i][j];
                nums.push_back(res[i + 1][j + 1]);
            }
        
        // O(m * n)
        k = nums.size() - k;
        nth_element(nums.begin(), nums.begin() + k, nums.end());

        return nums[k];
    }
};

```
