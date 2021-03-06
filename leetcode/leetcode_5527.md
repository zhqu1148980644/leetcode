---
title: Number of Sets of K Non Overlapping Line Segments
date: 2021-01-04
---
Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.

 

Example 1:


Input: n = 4, k = 2
Output: 5
Explanation: 
The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.
Example 2:

Input: n = 3, k = 1
Output: 3
Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
Example 3:

Input: n = 30, k = 7
Output: 796297179
Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 109 + 7 gives us 796297179.
Example 4:

Input: n = 5, k = 3
Output: 7
Example 5:

Input: n = 3, k = 2
Output: 1
 

Constraints:

2 <= n <= 1000
1 <= k <= n-1


#### Solutions

1. ##### dynamic programming O(nk)

- `dp[n][k] = dp[n - 1][k] + (dp[n - 1][k - 1], dp[n - 2][k - 1] + dp[n - 3][k - 1] + ...)`
    - The first part represents no line segment in `pos[k]`.
    - The second part is the opposite, however, since the segment in the last position may extend into multiple length, i.e. `pos[x:k]`. When conbined with `dp[x - 1][k - 1]`, all these combinations are different and thus need to be summed together.
- This dp formula actually cost `O(n^2 * k)` time and would cause TLE.

```cpp
class Solution {
public:
    int numberOfSets(int n, int k) {
        n--;
        vector<vector<size_t>> dp(n + 1, vector<size_t>(k + 1));

        for (int i = 1; i <= n; i++) {
            dp[i][1] = (i + 1) * i / 2;
            for (int j = 2; j <= k; j++) {
                // pos[k] has no segment
                dp[i][j] += dp[i - 1][j];
                // post[k] has segment and may have multiple length
                for (int pi = i - 1; pi >= 1; pi--)
                    dp[i][j] += dp[pi][j - 1];
                dp[i][j] %= 1000000007;
            }
        }
        
        return dp[n][k];
    }
};

```


- Optimize time complexity to `O(nk)` with prefix sum.
- `sum[n][k]` represents sum of `dp[1][k], dp[2][k], ..., dp[n][k]`

```cpp
class Solution {
public:
    int numberOfSets(int n, int k) {
        n--;
        vector<vector<size_t>> dp(n + 1, vector<size_t>(k + 1));
        vector<vector<size_t>> sum(dp);

        for (int i = 1; i <= n; i++) {
            sum[i][1] = dp[i][1] = (i + 1) * i / 2;
            for (int j = 2; j <= k; j++) {
                dp[i][j] += dp[i - 1][j];
                dp[i][j] += sum[i - 1][j - 1];
                dp[i][j] %= 1000000007;
                sum[i][j - 1] = sum[i - 1][j - 1] + dp[i][j - 1];
            }
        }
        
        return dp[n][k];
    }
};

```


2. ##### Other Solutions

- Check discussions in the official lc website.

