---
title: 1723. Find Minimum Time to Finish All Jobs
date:
---

# 1723. Find Minimum Time to Finish All Jobs

You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.

 

Example 1:

Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.
Example 2:

Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.
 

Constraints:

1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107


#### Solutions

- reference: https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/solution/zhuang-ya-dp-jing-dian-tao-lu-xin-shou-j-3w7r/

1. ##### dynamic programming

- `dp[k][s]` represents the minimum time for `k` workers to finish the job set `s`. `s` is a bit represention of the job set.
- `dp[k][s] = min(max(dp[k - 1][s - curs], sum[curs]), dp[k][s] for curs in s)`.
  - `curs` is the jobs set to be finished for the k'th worker.
  - `sum[curs]` is the sum time for job set `curs`.

```c++
class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k) {
        int n = jobs.size(), maxs = 1 << n;
        // sum times of all possible job combinations
        vector<int> sum(maxs);
        for (int s = 0; s < maxs; s++)
            for (int i = 0; i < n; i++)
                if (s & (1 << i))
                    sum[s] += jobs[i];
        

        vector<vector<int>> dp(k + 1, vector<int>(maxs, INT_MAX));
        dp[0][0] = 0;
        for (int ck = 1; ck <= k; ck++)
            for (int s = 1; s < maxs; s++)
                for (int cs = s; cs; cs = (cs - 1) & s)
                    dp[ck][s] = min(dp[ck][s], max(dp[ck - 1][s ^ cs], sum[cs]));
        

        return dp[k][maxs - 1];
    }
};
```


2. ##### binary search + dynamic programming

- `min_workers(limit)` represents the minimum number of workers to finish all jobs with the maximum sum time `<= limit`.
- We can use binary search to find the mininum `limit` because `min_workers(limit)` changes monotonically according to the value of `limit`. i.e. the higher the limit becomes, less workers are required.

```c++
class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k) {
        int n = jobs.size(), maxs = 1 << n;
        // sum times of all possible job combinations
        vector<int> sum(maxs);
        for (int s = 0; s < maxs; s++)
            for (int i = 0; i < n; i++)
                if (s & (1 << i))
                    sum[s] += jobs[i];
        
        // use dynamic programming to find the minimum number of workers required.
        auto min_workers = [&](int limit) {
            vector<int> dp(maxs, INT_MAX / 2);
            dp[0] = 0;
            for (int s = 1; s < maxs; s++)
                for (int cs = s; cs; cs = (cs - 1) & s)
                    if (sum[cs] <= limit)
                        dp[s] = min(dp[s], dp[s ^ cs] + 1);
            return dp[maxs - 1];
        };

        int lo = 1, hi = accumulate(jobs.begin(), jobs.end(), 0);
        while (lo < hi) {
            int mid = lo + ((hi - lo) >> 1);
            // if min_workers > k, the limit must be underestimated
            if (min_workers(mid) > k)
                lo = mid + 1;
            else
                hi = mid;
        }

        return lo;
    }
};
```