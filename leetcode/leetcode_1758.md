---
title: 1758. Minimum Changes To Make Alternating Binary String
date: 2021-02-14
---

# 1758. Minimum Changes To Make Alternating Binary String

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

 

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
 

Constraints:

1 <= s.length <= 104
s[i] is either '0' or '1'.

#### Solutions

1. ##### straight forward

```c++
class Solution {
public:
    int solve(string s) {
        int res = 0;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i - 1]) {
                s[i] = s[i] == '1' ? '0' : '1';
                res++;
            }
        }
        return res;
    }
    int minOperations(string s) {
        int res1 = solve(s);
        s[0] = s[0] == '1' ? '0' : '1';
        int res2 = solve(s);
        return min(res1, 1 + res2);
    }
};
```

or

```c++
class Solution {
public:
    int solve(string s) {
        int res = 0;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i - 1]) {
                s[i] = s[i] == '1' ? '0' : '1';
                res++;
            }
        }
        return res;
    }
    int minOperations(string s) {
        int res = solve(s);
        return min(res, (int)s.size() - res);
    }
};
```