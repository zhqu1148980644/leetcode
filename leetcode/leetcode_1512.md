---
title: Number of Good Pairs
date: 2021-01-04
---
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100


#### Solutions

1. ##### sort O(nlog(n))

```cpp
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        if (nums.size() <= 1) return 0;
        vector<pair<int, int>> sorted;
        for (int i = 0; i < nums.size(); i++)
            sorted.push_back({nums[i], i});
        
        sort(sorted.begin(), sorted.end());
        
        int i = 0, res = 0;
        while (i < sorted.size()) {
            int j = i;
            while (j < sorted.size() && sorted[j].first == sorted[i].first)
                j++;
            while (i < j) {
                res += j - i - 1;
                i++;
            }
        }
        return res;
    }
};
```

2. ##### count sort O(n)

- reference: https://leetcode-cn.com/problems/number-of-good-pairs/solution/zhe-gu-ji-shi-wo-xie-zen-yao-duo-ti-yi-lai-zui-dua/

```cpp
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        vector<int> count(101);
        int res = 0;
        for (auto n : nums) {
            res += count[n]++;
        }
        return res;
    }
};
```

or a more straightforward version

```cpp
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        vector<int> count(101);
        for (auto n : nums)
            count[n]++;

        int res = 0;
        for (int n = 1; n <= 100; n++)
            if (count[n])
                res += count[n] * (count[n] - 1) / 2;
        
        return res;
    }
};
```