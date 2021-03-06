---
title: Task Scheduler
date: 2021-01-04
---
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].


#### Solutions

1. ##### greedy approach O(t)

- To make the most use of intervals between identical tasks, an intuitive approach is to firstly schedule the most frequent task and then schedule the second most frequent task between them.
- We schedule tasks in goups of size `(n + 1)` to make sure all tasks are delayed n tasks.


```cpp
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> count(26);
        for (auto c : tasks)
            count[c - 'A']++;
        
        int time = 0, lastt = 0;
        sort(count.rbegin(), count.rend());
        while (count.size() && count[0] > 0) {
            for (int i = 0; i <= n; i++) {
                if (i < count.size() && count[i] > 0) {
                    --count[i];
                    lastt = max(lastt, time + 1);
                }
                time++;
            }
            sort(count.rbegin(), count.rend());
            while (count.size() && count.back() <= 0)
                count.pop_back();
        }

        return lastt;
    }
};
```


2. ##### math

- Check the official answer.
- reference: https://leetcode-cn.com/problems/task-scheduler/solution/ren-wu-diao-du-qi-by-leetcode/

```cpp
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        n++;
        vector<int> count(26);
        for (auto c : tasks)
            ++count[c - 'A'];
        sort(count.rbegin(), count.rend());
        int maxc = count[0], idle_slots = (maxc - 1) * n;
        for (int i = 0; i < count.size() && count[i] > 0; i++) {
            idle_slots -= min(count[i], maxc - 1);
        }
        return idle_slots > 0 ? tasks.size() + idle_slots : tasks.size();
    }
};
```

since we only care about the most frequent task. we can reduce to `O(n)` time complexity.

```cpp
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        n++;
        vector<int> count(26);
        for (auto c : tasks)
            ++count[c - 'A'];

        int maxc = *max_element(count.begin(), count.end());
        int idle_slots = (maxc - 1) * n;
        for (int i = 0; i < count.size() && count[i] > 0; i++) {
            idle_slots -= min(count[i], maxc - 1);
        }
        return idle_slots > 0 ? tasks.size() + idle_slots : tasks.size();
    }
};
```