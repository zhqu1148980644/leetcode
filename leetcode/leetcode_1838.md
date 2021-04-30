---
title: 1838. Frequency of the Most Frequent Element
date: 2021-04-25
---

# 1838. Frequency of the Most Frequent Element


The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

 

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 105

#### Solutions

1. ##### sort, binary search

```c++
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        // sort in ascending order to make binary search being possible
        sort(nums.begin(), nums.end());
        vector<long> sums(nums.size() + 1);

        int res = 1;
        for (int j = 0; j < nums.size(); j++) {
            sums[j + 1] += sums[j] + nums[j];
            if (j == 0) continue;
            // binary search for the first number to be increased to be the same as nums[j]
            // nums[i:j] are all same to nums[j] after increment within k steps
            int lo = 0, hi = j;
            while (lo < hi) {
                int mid = lo + ((hi - lo) >> 1);
                long need = (long)nums[j] * (j - mid) - (sums[j] - sums[mid]);
                if (need > k)
                    lo = mid + 1;
                else
                    hi = mid;
            }
            res = max(res, j - lo + 1);
        }

        return res;
    }
};
```

2. ##### sort, sliding window

```c++
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<long> sums(nums.size() + 1);
        sums[1] = nums[0];

        long res = 1, need = 0;
        for (int i = 0, j = 1; j < nums.size(); j++) {
            sums[j + 1] += sums[j] + nums[j];
            need = (long)nums[j] * (j - i) - (sums[j] - sums[i]);
            while (need > k) {
                i++;
                need = (long)nums[j] * (j - i) - (sums[j] - sums[i]);
            }
            res = max((int)res, j - i + 1);
        }

        return res;
    }
};
```