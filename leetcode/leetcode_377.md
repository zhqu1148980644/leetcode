---
title: Combination Sum IV
date: 2021-01-04
---
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.



#### Solutions.


1. ##### recursion

```cpp
class Solution {
public:
    vector<int> dp, nums;

    int solve(int cur) {
        if (cur < 0) return 0;
        if (dp[cur] != -1)
            return dp[cur];
        size_t res = 0;
        for (auto diff : nums)
            res += solve(cur - diff);
        return dp[cur] = res;
    }
    int combinationSum4(vector<int>& nums, int target) {
        this->nums = move(nums);
        dp = vector<int>(target + 1, -1);
        dp[0] = 1;
        return solve(target);
    }
};
```


2. ##### dynamic programming O(target * n)

```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<size_t> dp(target + 1);
        dp[0] = 1;
        
        // numbers in nums can be used multiple times.
        for (int s = 1; s <= target; s++)
            for (auto n : nums) {
                if (s - n >= 0 && dp[s - n])
                    dp[s] += dp[s - n];
            }

        return dp[target];
    }
};
```