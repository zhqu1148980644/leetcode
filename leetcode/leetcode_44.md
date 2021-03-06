---
title: Wildcard Matching
date: 2021-01-04
---
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false


#### Solutios

1. ##### dynamic programming


- From the official answer.

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int n1 = s.size(), n2 = p.size();
        vector<vector<bool>> dp(n1 + 1, vector<bool>(n2 + 1, false));
        dp[0][0] = true;
        // empty string matched with * prefix
        for (int i = 1; i <= n2; i++) {
            if (p[i - 1] != '*') break;
            dp[0][i] = true;
        }

        for (int i = 1; i <= n1; i++)
            for (int j = 1; j <= n2; j++) {
                // p[j - 1] not used || p[j - 1] used 
                if (p[j - 1] == '*')
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j];
                else if (s[i - 1] == p[j - 1] || p[j - 1] == '?')
                    dp[i][j] = dp[i - 1][j - 1];
            }

        return dp[n1][n2];
    }
};

```