---
title: 1770. Maximum Score from Performing Multiplication Operations
date: 2021-02-21
---

# 1770. Maximum Score from Performing Multiplication Operations

You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.

 

Example 1:

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
Example 2:

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
 

Constraints:

n == nums.length
m == multipliers.length
1 <= m <= 103
m <= n <= 105
-1000 <= nums[i], multipliers[i] <= 1000


#### Solutions

1. ##### dynamic programming O(m2)

- `dp[n1][n2]` represents the maximum socre can be made when choosed the first `n1` numbers and the last `n2` numbers in array `nums`.

```c++
class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        int n = nums.size(), m = multipliers.size();
        vector<vector<int>> dp(m + 1, vector<int>(m + 1));
        int res = INT_MIN;
        for (int i = 0; i <= m; i++)
            for (int j = 0; j <= m; j++) {
                if (i == 0 && j == 0 || i + j > m)
                    continue;
                // check which number is the current number
                int s1 = i > 0 ? dp[i - 1][j] + nums[i - 1] * multipliers[i + j - 1] : INT_MIN;
                int s2 = j > 0 ? dp[i][j - 1] + nums[n - j] * multipliers[i + j - 1] : INT_MIN;
                dp[i][j] = max(s1, s2);
                if (i + j == m)
                    res = max(res, dp[i][j]);
            }
        
        return res;
    }
};
```