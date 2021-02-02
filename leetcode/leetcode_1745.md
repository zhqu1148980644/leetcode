---
title: 1745. Palindrome Partitioning IV
date: 2021-02-02
---

# 1745. Palindrome Partitioning IV

Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.

 

Example 1:

Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
Example 2:

Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.
 

Constraints:

3 <= s.length <= 2000
s​​​​​​ consists only of lowercase English letters.


#### Solutions

1. ##### dynamic programming O(n2)

```c++
class Solution {
public:
    bool checkPartitioning(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n));

        for (int j = 0; j < n; j++) {
            for (int i = j; i >= 0; i--) {
                if (s[i] == s[j] && (j - i < 2 || dp[i + 1][j - 1]))
                    dp[i][j] = true;
            }
        }

        for (int i = 0; i < n - 2; i++) {
            if (!dp[0][i]) continue;
            for (int j = i + 1; j < n - 1; j++) {
                if (dp[i + 1][j] && dp[j + 1][n - 1])
                    return true;
            }
        }

        return false;
    }
};
```