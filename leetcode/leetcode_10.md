---
title:  Regular Expression Matching
date: 2021-01-04
---
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

#### Note:

-    s could be empty and contains only lowercase letters a-z.
-    p could be empty and contains only lowercase letters a-z, and characters like . or *.

```
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
```


#### Solutions


1. ##### recursion

- reference: the official answer

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        if (p.empty())
            return s.empty();
        bool firstmatch = s.size() && (s[0] == p[0] || p[0] == '.');
        if (p.size() >= 2 && p[1] == '*')
            // case 1: ignore `x*`  case2: match the first character
            return isMatch(s, p.substr(2))
                || (firstmatch && isMatch(s.substr(1), p));
        else
            // case 3: match the first character
            return firstmatch
                && isMatch(s.substr(1), p.substr(1));
    }
};
```

2. ##### dynamic programming with memoization

- reference: the official answer
- `dp[i][j] = true` represents `s[i:]` matches `pattern[j:]`.


```cpp
class Solution {
public:
    vector<vector<int>> memo;
    string s, p;

    int match(int i, int j) {
        if (memo[i][j] != -1)
            return memo[i][j];
        // base case, patten is empty whearas the target string is not.
        // case when i reaches end will end in else expression
        if (j == p.size())
            return memo[i][j] = i == s.size();
        bool firstmatch = false;
        if (i < s.size() && (s[i] == p[j] || p[j] ==  '.'))
            firstmatch = true;
        if (j + 1 < p.size() && p[j + 1] == '*')
            memo[i][j] = match(i, j + 2) || (firstmatch && match(i + 1, j));
        else
            memo[i][j] = firstmatch && match(i + 1, j + 1);

        
        return memo[i][j];
    }

    int isMatch(string s, string p) {
        this->s = s; this->p = p;
        memo = vector<vector<int>>(s.size() + 1, vector<int>(p.size() + 1, -1));
        return match(0, 0);
    }
};
```

3. ##### dynamic programming O(len(s) * len(p)) S(max(len(s), len(p)))

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<bool>> dp(s.size() + 1, vector<bool>(p.size() + 1, false));
        dp[s.size()][p.size()] = true;
        // starting from s.size() to consume trailing .* in pattern   
        for (int i = s.size(); i >= 0; i--)
            for (int j = p.size() - 1; j >= 0; j--) {
                bool firstmatch = false;
                if (i < s.size() && (s[i] == p[j] || p[j] == '.'))
                    firstmatch = true;
                if (j + 1 < p.size() && p[j + 1] == '*')
                    dp[i][j] = dp[i][j + 2] || (firstmatch && dp[i + 1][j]);
                else
                    dp[i][j] = firstmatch && dp[i + 1][j + 1];
            }

        return dp[0][0];
    }
};
```

4. ##### DFA