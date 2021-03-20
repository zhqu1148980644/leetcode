---
title: 5695. Maximize Score After N Operations
date: 2021-03-21
---

# 5695. Maximize Score After N Operations

You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

 

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
 

Constraints:

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106


#### Solutions

1. ##### dynamic programming

```c++
class Solution {
public:
    int maxScore(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> g(n, vector<int>(n));
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                g[i][j] = gcd(nums[i], nums[j]);
        
        int final_state = 1 << n;
        vector<int> dp(final_state);
        for (int s = 0; s < final_state; s++) {
            int count = __builtin_popcount(s);
            if (count & 1) continue;
            for (int i = 0; i < n; i++)
                for (int j = i + 1; j < n; j++) {
                    if ((s & (1 << i)) || (s & (1 << j)))
                        continue;
                    int ns = s | (1 << i) | (1 << j);
                    dp[ns] = max(dp[ns], dp[s] + g[i][j] * ((count / 2) + 1));
                }
        }
        return dp.back();
    }
};
```