---
title: 1737. Change Minimum Characters to Satisfy One of Three Conditions
date: 2021-01-24
---

# 1737. Change Minimum Characters to Satisfy One of Three Conditions

You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.

Your goal is to satisfy one of the following three conditions:

Every letter in a is strictly less than every letter in b in the alphabet.
Every letter in b is strictly less than every letter in a in the alphabet.
Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.

 

Example 1:

Input: a = "aba", b = "caa"
Output: 2
Explanation: Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).
Example 2:

Input: a = "dabadd", b = "cda"
Output: 3
Explanation: The best way is to make condition 1 true by changing b to "eee".
 

Constraints:

1 <= a.length, b.length <= 105
a and b consist only of lowercase letters.


#### Solutions

1. ##### prefix sum


- Check for all 26 characters. Calculate the required number of operations to satisfy the first two conditions by treating a certain character as the boundary character between two strings.

```c++
class Solution {
public:
    int minCharacters(string a, string b) {
        vector<int> m1(26), m2(26);
        for (auto c : a)
            m1[c - 'a']++;
        for (auto c : b)
            m2[c - 'a']++;
        // prefix sum
        vector<int> s1(27), s2(27);
        for (int i = 0; i < 26; i++) {
            s1[i + 1] += s1[i] + m1[i];
            s2[i + 1] += s2[i] + m2[i];
        }
        
        int res1 = INT_MAX, res2 = INT_MAX, res3 = INT_MAX;
        for (int i = 0; i < 26; i++) {
            // the first two conditions
            res1 = min(res1, s2[i + 1] + s1.back() - s1[i + 1]);
            res2 = min(res2, s1[i] + s2.back() - s2[i]);
            // the third condition
            res3 = min((size_t)res3, a.size() - m1[i] + b.size() - m2[i]);
        }

        return min(res1, min(res2, res3));
    }
};

```