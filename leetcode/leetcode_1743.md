---
title: 1743. Restore the Array From Adjacent Pairs
date: 2021-02-02
---

# 1743. Restore the Array From Adjacent Pairs

There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

 

Example 1:

Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
Example 2:

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
Example 3:

Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]
 

Constraints:

nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 105
-105 <= nums[i], ui, vi <= 105
There exists some nums that has adjacentPairs as its pairs.


#### Solutions

1. ##### hash map

```c++
class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        // build graph
        unordered_map<int, vector<int>> m;
        for (auto & e : adjacentPairs) {
            m[e[0]].push_back(e[1]);
            m[e[1]].push_back(e[0]);
        }
        // find the head/tail
        int st = -1;
        for (auto & [cur, adj] : m) {
            if (adj.size() == 1) {
                st = cur;
                break;
            }
        }
        // rebuild the chain from the head/tail
        vector<int> res = {st};
        int cur = m[st][0];
        while (true) {
            int back = cur;
            for (auto next : m[cur]) {
                if (next == res.back()) continue;
                cur = next;
            }
            res.push_back(back);
            // didn't extend, reach the other end
            if (cur == back) break;
        }
        return res;
    }
};
```