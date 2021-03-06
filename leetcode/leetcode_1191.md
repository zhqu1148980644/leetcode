---
title: K Concatenation Maximum Su
date: 2021-01-04
---
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0
 

Constraints:

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4


#### Solutions

1. ##### math

- There are three cases in total
    - the maximum sum of subarray in the original array.
    - the sum of the maximum `suffixsum` and the maximum `prefixsum`.
    - the sum of the second case plus sum of `k - 2` arrays in the middle.

```cpp
class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        if (arr.size() <= 0) return 0;
        long long presum = 0, minsum = 0, maxmid = 0, maxl = 0, maxr = 0;
        for (auto n : arr) {
            maxl = max(maxl, presum += n);
            maxmid = max(maxmid, presum - minsum);
            minsum = min(minsum, presum);
        }
        maxr = presum - minsum;
        // three cases
        long long res = k < 2 ? maxmid : max(
            max(maxl + maxr, maxmid), 
            (k - 2) * presum + maxl + maxr
        );
        return res % 1000000007;
    }
};
```

2. ##### dynamic programming

- https://leetcode-cn.com/problems/k-concatenation-maximum-sum/solution/java-kadanesuan-fa-yu-jie-ti-si-lu-by-zdxiq125/