---
title: Number of Valid Subarrays
date: 2021-01-04
---
Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the following condition:

The leftmost element of the subarray is not larger than other elements in the subarray.

 

Example 1:

Input: [1,4,2,5,3]
Output: 11
Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
Example 2:

Input: [3,2,1]
Output: 3
Explanation: The 3 valid subarrays are: [3],[2],[1].
Example 3:

Input: [2,2,2]
Output: 6
Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].
 

Note:

1 <= A.length <= 50000
0 <= A[i] <= 100000


#### Solutions

1. ##### mono stack O(n)

- For a given number in the array, the maximum length of subarray starts at this number satisfying the requirements is defined by the first number(after) slower than it.

```cpp
class Solution {
public:
    int validSubarrays(vector<int>& nums) {
        int n = nums.size();
        nums.push_back(INT_MIN);
        stack<int> s; s.push(n);
        
        int res = 0;
        for (int i = n - 1; i >= 0; i--) {
            while (s.size() && nums[i] <= nums[s.top()])
                s.pop();
            // the first number slower than self in the right.
            res += s.top() - i;
            s.push(i);
        }

        return res;
    }
};
```