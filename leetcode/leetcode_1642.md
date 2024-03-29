---
title: 1642. Furthest Building You Can Reach
date: 2021-01-04
---
# 1642. Furthest Building You Can Reach
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

 

Example 1:


Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length


#### Solutions

1. ##### greedy approach with priority queue O(nlog(n))

- Use a priority queue to record the top-k cost we have been paid before while we moving forward using bricks.
- When the current bricks are not sufficient, we try to use ladders(effciently) to restore the cost/bricks.
- Move forward until no more bricks left even all ladders have been used.

```cpp
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();

        multiset<int> pq;
        for (int i = 1; i < n; i++) {
            int diff = max(0, heights[i] - heights[i - 1]);
            if (diff > 0) pq.insert(diff);
            // this step can be omitted if we can ensure no excess ladders are used.
            if (pq.size() > ladders) pq.erase(pq.begin());
            bricks -= diff;
            // Need more bricks, try to use ladders to replace maximum diffs we met before.
            while (bricks < 0 && pq.size()) {
                bricks += *prev(pq.end());
                pq.erase(prev(pq.end()));
                ladders--;
            }
            if (bricks < 0)
                return i - 1;
        }        
        
        return n - 1;
    }
};
``

or use priority_queue.


```cpp
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();

        priority_queue<int> pq;
        for (int i = 1; i < n; i++) {
            int cost = max(0, heights[i] - heights[i - 1]);
            if (cost > 0) pq.push(cost);
            bricks -= cost;
            while (bricks < 0 && ladders > 0 && pq.size()) {
                bricks += pq.top(); pq.pop();
                ladders--;
            }
            if (bricks < 0)
                return i - 1;
        }
        
        return n - 1;
    }
};
```

2. ##### binary search

- Binary searching for the result and using ladders for the top-k costs.