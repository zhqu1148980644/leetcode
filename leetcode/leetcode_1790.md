---
title: 1790. Check if One String Swap Can Make Strings Equal
date: 2021-03-14
---

# 1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
Example 4:

Input: s1 = "abcd", s2 = "dcba"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.

#### Solutions

```c++
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        vector<int> count(26);
        int diff = 0, i = 0, j = 0;
        while (i != s1.size() && diff <= 2) {
            count[s1[i] - 'a']++;
            count[s2[j] - 'a']--;
            if (s1[i++] != s2[j++])
                diff++;
        }
        for (auto n : count)
            if (n != 0)
                return false;
        return i == s1.size() && (diff == 0 || diff == 2);
    }
};
```