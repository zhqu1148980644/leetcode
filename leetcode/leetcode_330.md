---
title: Patching Array
date: 2021-01-04
---
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:

Input: nums = [1,3], n = 6
Output: 1 
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0


#### Solutions

1. ##### greedy/math O(n)

- reference: https://leetcode-cn.com/problems/patching-array/solution/tan-xin-by-maozz_17-izg9/
- `hi` represents the current number needs to be formed and all nunmbers in `[0:hi)` can be composed of by `nums[:i)` and some patched number before.
- If `nums[i] < hi`, then we can compose nummbers `[0:hi) + nums[i] === [hi: hi + nums[i])`, we quickly jump to `hi + nums[i]` as the next number should be formed.
- If `nums[i] > hi or no numbers left`, we choose `hi` as the patched number, then we can compose `[0:hi) + hi === [hi, hi + hi)`, we quickly jump to `hi + hi` as the next number.
  - This is the greedy step.


```cpp
class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        long long res = 0, hi = 1, i = 0;
        while (hi <= n) {
            // [0:hi) + nums[i] === [hi: hi + nums[i])
            if (i < nums.size() && nums[i] <= hi)
                hi += nums[i++];
            // [0:hi) + hi === [hi: hi + hi)
            else {
                hi *= 2;
                res++;
            }
        }

        return res;
    }
};
```

