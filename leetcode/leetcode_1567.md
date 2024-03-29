---
title: 1567. Maximum Length of Subarray With Positive Product
date: 2021-01-04
---
# 1567. Maximum Length of Subarray With Positive Product
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

 

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
Example 4:

Input: nums = [-1,2]
Output: 1
Example 5:

Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

#### Solutions

1. ##### greedy strategy

- For a largest possible region without zero, if the product is `slower` than 0, try to remove the `first` or the `last` negative number to make the product positive.

```cpp
class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        nums.push_back(0);
        int n = nums.size(), res = 0, INF = 0x3f3f3f3f;
        int neg = 0, fneg = INF, lneg = -INF;
        for (int i = -1, j = 0; j < n; j++) {
            if (nums[j] == 0) {
                // meet a zero, try to remove the first negative or the last negative number.
                int len = j - i - 1;
                if (neg & 1) {
                    res = max(res, len - (fneg - i));
                    res = max(res, len - (j - lneg));
                }
                else
                    res = max(res, len);
                i = j; neg = 0;
                fneg = INF; lneg = -INF;
            }
            else if (nums[j] < 0) {
                    neg++; 
                    fneg = min(fneg, j);
                    lneg = max(lneg, j);
                }                    
            }
        return res;
    }
};

```