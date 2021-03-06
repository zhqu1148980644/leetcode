---
title: Reconstruct Itinerary
date: 2021-01-04
---
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.


#### Solutions

1. #### Hierholzer algorithm

- Check to official answer
- The priority_queue is soly used for finding the lexicographically smallest path.

```cpp
class Solution {
public:
    using Pq = priority_queue<string_view, vector<string_view>, greater<>>;
    unordered_map<string_view, Pq> g;
    vector<string> res;
    void dfs(const string_view s) {
        while (g.count(s) && g[s].size()) {
            auto out = g[s].top(); g[s].pop();
            dfs(out);
        }
        res.push_back(string(s));
    }
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for (auto & vs : tickets) {
            g[vs[0]].push(vs[1]);
        }
        dfs(g.find("JFK")->first);

        reverse(res.begin(), res.end());
        return res;
    }
};
```