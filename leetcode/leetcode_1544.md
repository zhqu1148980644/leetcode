---
title: 1544. Make The String Great
date: 2021-01-04
---
# 1544. Make The String Great
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
Example 3:

Input: s = "s"
Output: "s"
 

Constraints:

1 <= s.length <= 100
s contains only lower and upper case English letters.

#### Solutions

1. ##### recursion

```cpp
class Solution {
public:
    string makeGood(string s) {
        if (s.size() < 2) return s;
        for (int i = 0; i <= s.size() - 2; i++) {
            char c1 = s[i], c2 = s[i + 1];
            if (tolower(c1) == tolower(c2) && (c1 > 'Z' != c2 > 'Z'))
                return makeGood(s.substr(0, i) + s.substr(i + 2));
        }
        return s;
    }
};
```

2. ##### stack

```cpp
class Solution {
public:
    string makeGood(string s) {
        string res;
        for (auto c2 : s) {
            if (res.size()) {
                char c1 = res.back();
                if (tolower(c1) == tolower(c2)  && c1 > 'Z' != c2 > 'Z') {
                    res.pop_back();
                    continue;
                }
            }
            res += c2;
        }

        return res;
    }
};
```