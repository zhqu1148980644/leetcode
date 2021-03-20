---
title: 1793. Maximum Score of a Good Subarray
date: 2021-03-14
---

# 1793. Maximum Score of a Good Subarray

You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

 

Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 
Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length


#### Solutions

1. ##### binary search O(nlog(n))

- Since the minvalue around the `k'th` number has monotonic values.
- For each `i`, we can use binary search to find the right most `j` with `minvalue >= mins[i]`.

```c++
class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        vector<int> mins(nums.size());
        mins[k] = nums[k];
        for (int j = k + 1; j < nums.size(); j++)
            mins[j] = min(mins[j - 1], nums[j]);
        for (int i = k - 1; i >= 0; i--)
            mins[i] = min(mins[i + 1], nums[i]);
        
        int res = 0;
        for (int i = 0; i <= k; i++) {
            int j = upper_bound(mins.begin() + k, mins.end(), mins[i], greater<>()) - mins.begin() - 1;
            res = max(res, mins[i] * (j - i + 1));
        }
        for (int j = k; j < nums.size(); j++) {
            int i = lower_bound(mins.begin(), mins.begin() + k + 1, mins[j]) - mins.begin();
            res = max(res, mins[j] * (j - i + 1));
        }

        return res;
    }
};
```