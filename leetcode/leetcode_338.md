---
title: Counting Bits
date: 2021-01-04
---
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

##### Solutions

1. ##### straight forward O(32 * n)

```cpp
class Solution {
public:
    int pop_count(int n) {
        int res = 0;
        while (n) {
            // remove the rightmost 1 bit.
            n &= n - 1; res++;
        }
        return res;
    }

    vector<int> countBits(int num) {
        vector<int> res(num + 1);
        for (int i = 0; i <= num; i++)
            res[i] = pop_count(i);

        return res;
    }
};
```

2. ##### dynamic programming O(n)


```cpp
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> dp(num + 1);
        for (int n = 1; n <= num; n++) {
            dp[n] = (n & 1) + dp[n >> 1];
        }
        return dp;
    }
};
```

or similar to popcount.

```cpp
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> dp(num + 1);
        for (int n = 1; n <= num; n++) {
            dp[n] = dp[n & (n - 1)] + 1;
        }
        return dp;
    }
};
```