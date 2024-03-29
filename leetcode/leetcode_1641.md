---
title: 1641. Count Sorted Vowel Strings
date: 2021-01-04
---
# 1641. Count Sorted Vowel Strings
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045
 

Constraints:

1 <= n <= 50 


#### Solutions

1. ##### dynamic programming O(25n)

```cpp
class Solution {
public:
    int countVowelStrings(int n) {
        vector<vector<int>> dp(n + 1, vector<int>(5));
        for (int i = 0; i < 5; i++)
            dp[1][i] = 1;
        
        for (int len = 2; len <= n; len++) {
            for (char c = 0; c < 5; c++) {
                for (char prevc = c; prevc >= 0; prevc--) {
                    dp[len][c] += dp[len - 1][prevc];
                }
            }
        }
        
        return accumulate(dp[n].begin(), dp[n].end(), 0);
    }
};
```

2. ##### math

- Need To Be Done.
- reference: https://leetcode-cn.com/problems/count-sorted-vowel-strings/solution/tong-ji-zi-dian-xu-yuan-yin-zi-fu-chuan-de-shu-mu-/