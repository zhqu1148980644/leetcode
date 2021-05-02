---
title: 5748. Minimum Interval to Include Each Query
date: 2021-05-02
---

# 5748. Minimum Interval to Include Each Query

You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

 

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
 

Constraints:

1 <= intervals.length <= 105
1 <= queries.length <= 105
queries[i].length == 2
1 <= lefti <= righti <= 107
1 <= queries[j] <= 107

#### Solutions

1. ##### sort

```c++
class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        vector<int> indexes(queries.size());
        iota(indexes.begin(), indexes.end(), 0);
        sort(indexes.begin(), indexes.end(), [&](int i, int j) {
            return queries[i] < queries[j];
        });
        sort(intervals.begin(), intervals.end());

        multiset<int> ranges;
        multiset<pair<int, int>> invalidate;
        
        int i = 0;
        vector<int> res(queries.size());
        for (auto qi : indexes) {
            // record all intervals with start <= query
            while (i < intervals.size() && intervals[i][0] <= queries[qi]) {
                int st = intervals[i][0], ed = intervals[i][1];
                int range = ed - st + 1;
                ranges.insert(range);
                // record invalidate timing based on ed + 1
                invalidate.insert({ed + 1, range});
                i++;
            }
            // invalidate all range passed
            while (invalidate.size() && invalidate.begin()->first <= queries[qi]) {
                int range = invalidate.begin()->second;
                if (ranges.find(range) != ranges.end())
                    ranges.erase(ranges.find(range));
                invalidate.erase(invalidate.begin());
            }
            res[qi] = ranges.size() ? *ranges.begin() : -1;
        }

        return res;
    }
};
```