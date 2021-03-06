---
title:  Count Negative Numbers in a Sorted Matrix
date: 2021-01-04
---
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

```
Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3

Example 4:

Input: grid = [[-1]]
Output: 1
```

 

#### Constraints:

-    m == grid.length
-    n == grid[i].length
-    1 <= m, n <= 100
-    -100 <= grid[i][j] <= 100


#### Solutions

1. ##### straight forward  O(n)


```cpp
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int res = 0;
        // for each row
        for (int i = 0, j = n - 1; i < m && j >= 0; i++) {
            while (j >= 0 && grid[i][j] < 0)
                j--;
            res += n - j - 1;
            if (j < 0)
                res += (m - i - 1) * n;
        }

        return res;
    }
};
```

2. ##### binary search


```cpp
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), res = 0;

        for (int i = 0, j = n; i < m && j > 0; i++) {
            auto begin = grid[i].begin();
            auto find = lower_bound(begin, begin + j, -1, greater<int>());
            if (find != begin + n) {
                j = find - begin;
                res += n - j;
            }
            if (find == begin)
                res += (m - i - 1) * n;
        }

        return res;
    }
};
```