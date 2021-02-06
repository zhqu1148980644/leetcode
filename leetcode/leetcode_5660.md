---
title: 5660. Maximum Number of Events That Can Be Attended II
date: 2021-02-06
---

# 5660. Maximum Number of Events That Can Be Attended II

You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

 

Example 1:



Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
Example 2:



Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
Example 3:



Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
Output: 9
Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
 

Constraints:

1 <= k <= events.length
1 <= k * events.length <= 106
1 <= startDayi <= endDayi <= 109
1 <= valuei <= 106


#### Solutions

1. ##### dynamic programming O(nlog(n))

- check problem `1235 Maximum Profit in Job Scheduling` for similar solution.

```c++
class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        int n = events.size();
        sort(events.begin(), events.end(), [&](auto & e1, auto & e2) {
            return e1[1] < e2[1];
        });

        vector<vector<int>> dp(n, vector<int>(k + 1));
        vector<int> target = {INT_MAX, 0, INT_MAX};
        int res = dp[0][k - 1] = events[0][2];

        for (int j = 1; j < n; j++) {
            target[1] = events[j][0];
            auto find = lower_bound(events.begin(), events.end(), target, 
                [](auto & v1, auto & v2) { return v1[1] < v2[1]; }
            );
            int prev = int(find - events.begin()) - 1;
            for (int i = k - 1; i >= 0; i--) {
                dp[j][i] = events[j][2] + (prev >= 0 ? dp[prev][i + 1] : 0);
                dp[j][i] = max(dp[j][i], dp[j - 1][i]);
                res = max(res, dp[j][i]);
            }
        }
        
        return res;
    }
};
```