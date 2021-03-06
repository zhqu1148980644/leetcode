---
title:  Construct Target Array With Multiple Sums
date: 2021-01-04
---
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

    let x be the sum of all elements currently in your array.
    choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
    You may repeat this procedure as many times as needed.

Return True if it is possible to construct the target array from A otherwise return False.

 

```
Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done

Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].

Example 3:

Input: target = [8,5]
Output: true
```

 

#### Constraints:

-    N == target.length
-    1 <= target.length <= 5 * 10^4
-    1 <= target[i] <= 10^9


#### Solutions

1. ##### backwards

- For example: `target = [9, 3, 5]`
    - Since 9 is the largest element, 9 must be calculated by adding the sum of the previous array.
    - ie: the previous array is `[9 - (3 + 5), 3, 5]` and `prev = curmax - (sum - curmax)`.
    - Following this rule, we can reconstruct the initial array `[1, 1, 1]` if we can construct target from `A`(composed of 1s).

```cpp
class Solution {
public:
    bool isPossible(vector<int>& target) {
        long sum = accumulate(target.begin(), target.end(), 0l);
        priority_queue<long> pq(target.begin(), target.end());

        int curmax = pq.top(), prev, size = target.size();
        while (sum > size && curmax - (sum - curmax) > 0) {
            pq.pop();
            if (sum - curmax == 0)
                return false;
            // in case the stepsize is 1, deduce to 1 instead of 0
            else if (sum - curmax > 1) 
                prev = curmax % (sum - curmax);
            else prev = 1;
            pq.push(prev);
            sum -= curmax - prev;
            curmax = pq.top();
        }
        // all are ones
        return sum == size && curmax == 1;
    }
};
```