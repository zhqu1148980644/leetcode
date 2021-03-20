---
title: 1717. Maximum Score From Removing Substrings
data:
---

# 1717. Maximum Score From Removing Substrings

You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.


#### Solutions

1. ##### greedy approach

- In the first step, iteratively remove the substring(ab or ba) with the highest score by using a stack. Then remove the other one in the second step.
- Need to be proven.

```c++
class Solution {
public:
    int maximumGain(string s, int x, int y) {
        if (x > y) {
            for (auto & c : s)
                if (c == 'b') c = 'a';
                else if (c == 'a') c = 'b';
            swap(y, x);
        }
        int res = 0;
        string st = " ";
        for (auto c : s) {
            if (c == 'a' && st.back() == 'b') {
                st.pop_back(); res += y;
            }
            else
                st += c;
        }
        s = st; st = " ";
        for (auto c : s)
            if (c == 'b' && st.back() == 'a') {
                st.pop_back(); res += x;
            }
            else
                st += c;
        
        return res;
    }
    
};

```