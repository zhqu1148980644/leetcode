---
title: Range Addition
date: 2021-01-04
---
Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Explanation:

Initial state:
[0,0,0,0,0]

After applying operation [1,3,2]:
[0,2,2,2,0]

After applying operation [2,4,3]:
[0,2,5,5,3]

After applying operation [0,2,-2]:
[-2,0,3,5,3]


#### Solutions

1. ##### discretization/ difference array O(n)

- This approach is used in many other problems.

```cpp
class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        vector<int> diff(length + 1);
        
        for (auto & uv : updates) {
            int st = uv[0], ed = min(uv[1] + 1, length), inc = uv[2];
            diff[st] += inc;
            diff[ed] -= inc;        
        }
        // prefix sum
        int sum = 0;
        for (auto & d : diff)
            d = sum += d;
        // equals to using stl algorithm
        // partial_sum(diff.begin(), diff.end(), diff.begin());
        
        diff.pop_back();
        return diff;
    }
};
```