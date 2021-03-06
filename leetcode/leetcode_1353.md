---
title:  Maximum Number of Events That Can Be Attende
date: 2021-01-04
---
Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.

 

```
Example 1:

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Example 3:

Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4

Example 4:

Input: events = [[1,100000]]
Output: 1

Example 5:

Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7
```

 

#### Constraints:

-    1 <= events.length <= 10^5
-    events[i].length == 2
-    1 <= events[i][0] <= events[i][1] <= 10^5


#### Solutions

- Caution: We can attend an event at any single day within the schedule. ie: No need to start at the beginning of events and end at the end.

1. ##### greedy approach

- Sort by end time of events, then attend each event on a single day.
- TLE.
```cpp
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end(), [](auto & e1, auto & e2) {
            return e1[1] < e2[1];
        });

        int num = 0;
        unordered_set<int> used;
        for (auto & e : events) {
            for (int day = e[0]; day <= e[1]; day++) {
                if (used.count(day)) continue;
                used.insert(day);
                num++;
                break;
            }
        }

        return num;
    }
};
```

2. ##### greedy strategy with priority queue O(d * log(n)) S(n)


```cpp
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        unordered_map<int, vector<int>> evs;
        int mind = INT_MAX, maxd = INT_MIN;
        for (auto & e : events) {
            mind = min(mind, e[0]);
            maxd = max(maxd, e[1]);
            evs[e[0]].push_back(e[1]);
        }

        int num = 0;
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int d = mind; d <= maxd; d++) {
            if (evs.count(d))
                for (auto endday : evs[d])
                    pq.push(endday);
            while (pq.size() && pq.top() < d)
                pq.pop();
            if (pq.size()) {
                pq.pop();
                if (++num >= events.size())
                    break;
            }
        }

        return num;
    }
};
```

Or(TLE)

```cpp
class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        // heapfy by start day(minstack), O(n)
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (auto e : events)
            pq.push({e[0], e[1]});

        int cur = 0, num = 0;
        while (!pq.empty()) {
            int st = pq.top().first;
            int ed = pq.top().second;
            pq.pop();
            // this event is no longer valid
            if (ed < cur)
                continue;
            // attend one event
            else if (st >= cur) {
                cur = st + 1;
                num++;
            }
            // since days before the current day have been checked, postpone this event
            else if (st + 1 <= ed)
                pq.push({st + 1, ed});
        }

        return num;
    }
};
```