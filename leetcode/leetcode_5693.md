---
title: 5693. Second Largest Digit in a String
date: 2021-03-21
---

# 5693. Second Largest Digit in a String

Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.

#### Solutions

1. ##### hash map

```c++
class Solution {
public:
    int secondHighest(string s) {
        vector<int> count(10);
        for (auto c : s) {
            if (c >= '0' && c <= '9') {
                count[c - '0']++;
            }
        }
        for (int i = 9; i >= 0; i--) {
            if (count[i] > 0) {
                for (int j = i - 1; j >= 0; j--) {
                    if (count[j] > 0)
                        return j;
                }
                break;
            }
        }
        return -1;
    }
};
```