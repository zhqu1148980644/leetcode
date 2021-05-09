---
title: 5752. Maximum Subarray Min-Product
date: 2021-05-09
---

# 5752. Maximum Subarray Min-Product


The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
Example 2:

Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.
Example 3:

Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 107

#### Solutions

1. ##### mono stack O(n)

- The maxinum product of a certain array is constrained by the minimum number within it, we can iterate over all numbers in the array and find the maximum product when the checking number is the minimum vlaue.
- To calculate the maximum product for a minimum number, we need to find out the first two numbers not lower than in both sides. This can be done in `O(1)` time with a monotonically increasing stack.

```c++
class Solution {
public:
    int maxSumMinProduct(vector<int>& nums) {
        // guard at the end, to simplify check for edge cases
        nums.push_back(0);
        int n = nums.size();
        // can be done simultaneously in next for loop
        vector<size_t> sums(n + 1);
        for (int i = 0; i < n; i++)
            sums[i + 1] += sums[i] + nums[i];
        
        stack<pair<int, int>> s;
        // guard at the start, to simplify check for edge cases
        s.emplace(-INT_MAX, -1);
        size_t res = 0;

        for (int j = 0; j < n; j++) {
            int cur = nums[j];
            while (cur < s.top().first) {
                // cur is the first number < prev in the left
                auto [prev, i] = s.top(); s.pop();
                while (s.top().first == prev)
                    s.pop();
                // s.top().second if the first number < prev in the right
                size_t pro = prev * (sums[j] - sums[s.top().second + 1]);
                res = max(res, pro);
            }
            s.emplace(cur, j);
        }

        return res % 1000000007;
    }
};
```