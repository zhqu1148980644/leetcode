---
title: 1775. Equal Sum Arrays With Minimum Number of Operations
date: 2021-03-01
---

# 1775. Equal Sum Arrays With Minimum Number of Operations

You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

 

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
Example 2:

Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
Example 3:

Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6


#### Solutions

1. ##### greedy approach

- The idea is to change numbers with the maximum difference at each step.
- Suppose `nums1` has a lower summation and the difference is `sum2 - sum1 = diff`
- For each number `n` in `nums1`, change `n` to `6` will deduce the `diff` by `6 - n`.
- The same for numbers in `nums2`, ...                                     by `n - 6`.

```c++
class Solution {
public:
    int minOperations(vector<int>& nums1, vector<int>& nums2) {
        auto s1 = accumulate(nums1.begin(), nums1.end(), 0);
        auto s2 = accumulate(nums2.begin(), nums2.end(), 0);
        if (s1 > s2) return minOperations(nums2, nums1);

        vector<int> m1(7), m2(7);
        for (auto n : nums1)
            m1[n]++;
        for (auto n : nums2)
            m2[n]++;

        int res = 0, i = 1, j = 6, diff = s2 - s1;
        // two pointers
        // prefter to operate the number with maximum diff
        while (s1 != s2 && (i < 6 || j > 1)) {
            if (6 - i >=  j - 1) {
                int inc = min(diff, (6 - i) * m1[i]);
                res += (inc + (6 - i) - 1) / (6 - i);
                diff -= inc; i++;
            }
            else {
                int dec = min(diff, (j - 1) * m2[j]);
                res += (dec + (j - 1) - 1) / (j - 1);
                diff -= dec; j--;
            }
        }
    
        return diff == 0 ? res : -1;

    }
};
```

An optimized version that stores all difference in one array. reference: https://leetcode-cn.com/problems/equal-sum-arrays-with-minimum-number-of-operations/solution/tong-guo-zui-shao-cao-zuo-ci-shu-shi-shu-o8no/

```c++
class Solution {
public:
    int minOperations(vector<int>& nums1, vector<int>& nums2) {
        auto s1 = accumulate(nums1.begin(), nums1.end(), 0);
        auto s2 = accumulate(nums2.begin(), nums2.end(), 0);
        if (s1 > s2) return minOperations(nums2, nums1);
        vector<int> diffs(7);
        for (auto n : nums1)
            diffs[6 - n]++;
        for (auto n : nums2)
            diffs[n - 1]++;
        
        int diff = s2 - s1, res = 0;
        int d = 5;
        while (d > 0 && diff > 0) {
            int change = min(diff, d * diffs[d]);
            int op = (change + d - 1) / d;
            diff -= change;
            res += op;
            d--;
        }

        
        return diff == 0 ? res : -1;

    }
};
```