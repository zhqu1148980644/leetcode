---
title: Unique Number of Occurrences
date: 2021-01-04
---
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

#### Solutions

1. ##### hash map

```cpp
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        vector<int> count(2001);
        for (auto n : arr) count[n + 1000]++;

        vector<int> m(1000);
        for (auto c : count)
            if (c && ++m[c] > 1)
                return false;
        return true;
    }
};
```