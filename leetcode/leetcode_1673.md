---
title: 1673. Find the Most Competitive Subsequence
date: 2021-01-04
---
# 1673. Find the Most Competitive Subsequence
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

 

Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
Example 2:

Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= nums.length


#### Solutions

1. ##### mono stack O(n)

- The problem equals to find the minumum subsequence with length of k.
- Mataining a monotonically increasing sequence with sizes <= k.

```cpp
class Solution {
public:
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        stack<int> s;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            // if the current number is lower than the top(largest) element of the stack.
            // and also the remaining elements are sufficient, replace the top number with 
            // a smaller number could definitely makes up a smaller subsequence.
            while (s.size() && nums[i] < nums[s.top()] && s.size() + (n - i - 1) >= k)
                s.pop();
            // not larger than k
            if (s.size() < k)
                s.push(i);
        }
        vector<int> res;
        while (s.size()) {
            res.push_back(nums[s.top()]);
            s.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};

```