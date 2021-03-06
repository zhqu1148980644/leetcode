---
title: Decode Ways
date: 2021-01-04
---
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


#### Solutions

1. ##### dynamic programming

- Be cautious about conner cases.

```cpp
class Solution {
public:
    int numDecodings(string s) {
        if (s.size() == 0) return 0;
        int pprev = 1, prev = s[0] != '0', cur;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == '0') {
                if ('0' < s[i - 1] && s[i - 1] <= '2') cur = pprev;
                else return 0;
            }
            else {
                cur = prev;
                // 0 < s[i-1:i] < 27
                if ('0' < s[i - 1] && s[i - 1] <= ('2' - (s[i] > '6')))
                    cur += pprev;
            }
            pprev = prev; prev = cur;
        }
        return prev;
    }
};
```