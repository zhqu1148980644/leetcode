---
title: Parallel Courses
date: 2021-01-04
---
There are N courses, labelled from 1 to N.

We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return -1.

 

Example 1:



Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: 
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
Example 2:



Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: 
No course can be studied because they depend on each other.
 

Note:

1 <= N <= 5000
1 <= relations.length <= 5000
relations[i][0] != relations[i][1]
There are no repeated relations in the input.


#### Solutions

1. ##### topological sorting O(n)

```cpp
class Solution {
public:
    int minimumSemesters(int N, vector<vector<int>>& relations) {
        vector<int> deg(N + 1);
        vector<vector<int>> g(N + 1);
        // record indegree of each node
        for (auto & e : relations) {
            deg[e[1]]++;
            g[e[0]].push_back(e[1]);
        }
        // push nodes with no dependencies. i.e. 0 indegree
        queue<int> q;
        for (int c = 1; c <= N; c++)
            if (deg[c] == 0)
                q.push(c);
        
        int num_sem = 0, taken = 0;
        while (q.size()) {
            num_sem++;
            int size = q.size();
            while (size--) {
                auto cur = q.front();
                q.pop();
                taken++;
                for (auto out : g[cur]) {
                    if (--deg[out] == 0) {
                        q.push(out);
                    }
                }
            }
        }

        return taken == N ? num_sem : -1;
    }
};
```