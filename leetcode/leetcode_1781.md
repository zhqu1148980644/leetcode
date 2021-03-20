---
title: 1781. Sum of Beauty of All Substrings
date: 2021-03-06
---

# 1781. Sum of Beauty of All Substrings

The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

 

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.


#### Solutions

1. ##### tree map

```c++
class Solution {
public:
    int beautySum(string s) {
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            vector<int> count(26); count[s[i] - 'a']++;
            // <freq, num_char>
            map<int, int> m; m[1]++;
            for (int j = i + 1; j < s.size(); j++) {
                auto c = s[j] - 'a';
                count[c]++;
                m[count[c]]++;
                if (count[c] != 1 && --m[count[c] - 1] == 0)
                    m.erase(count[c] - 1);
                if (m.size()) {
                    auto first = begin(m)->first;
                    auto last = rbegin(m)->first;
                    res += last - first;
                }
            }
        }
        return res;
    }
};
```