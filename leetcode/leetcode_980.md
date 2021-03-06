---
title: Unique Paths III
date: 2021-01-04
---
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20


#### Solutions

1. ##### backtrack


```cpp
class Solution {
public:
    int m, n, needvisit = 0, res = 0;
    void dfs(vector<vector<int>> & grid, int i, int j, int cnt) {
        if (i < 0 || j < 0 || i >= m || j >= n 
            || grid[i][j] == -1)
            return;
        cnt++;
        if (grid[i][j] == 2)
            res += cnt == needvisit;
        else {
            int back = grid[i][j];
            grid[i][j] = -1;
            dfs(grid, i + 1, j, cnt);        
            dfs(grid, i - 1, j, cnt);
            dfs(grid, i, j + 1, cnt);
            dfs(grid, i, j - 1, cnt);
            grid[i][j] = back;
        }
    }

    int uniquePathsIII(vector<vector<int>>& grid) {
        m = grid.size(); if (!m) return 0;
        n = grid[0].size();
        int x = 0, y = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != -1) needvisit++;
                if (grid[i][j] == 1) {
                    x = i; y = j;
                }
            }
        dfs(grid, x, y, 0);
        return res;
    }
};
```


2. ##### dynamic programming
