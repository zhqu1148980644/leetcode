---
title: Split Two Strings to Make Palindrome
date: 2021-01-04
---
You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.

 

Example 1:

Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
Example 2:

Input: a = "abdef", b = "fecab"
Output: true
Example 3:

Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.
Example 4:

Input: a = "xbdef", b = "xecab"
Output: false
 

Constraints:

1 <= a.length, b.length <= 105
a.length == b.length
a and b consist of lowercase English letters


#### Solutions

1. ##### greedy approach

- For `s1[:i] + s2[j:]` to be palindrome, we can firstly find a prefix in s1 equals to suffix of s2, then check if the remaining part(in s1 or s2) is a palinedrome. We denote these kind of prefix as valid prefix.
- Since prefix of a valid prefix is also a valid prefix, it looks like we need to check for all possible prefix. However, we can prove that we only need(greedy) to check for the longest valid prefix.

```
aaa axxxxxx xxx
xxx xxxxxxa aaa
```

- For example above:
    - the longest valid prefix is `aaaa`
    - suppose we choose to check the prefix `aaa` in s1, then we need to check if the remaining part in s2 is a palindrome. ie: `xxxxxxa`
    - if `xxxxxxa` is a palindrome, we return true as the result. If we try to choose the longest prefix `aaaa` which will leads to the remaining part to be `xxxxx`(with 1 charactor in both ends removed), since `xxxxxxa` is a palindrome, `xxxxx` is also a palindrome and the result remains the same.
    - if `xxxxxxa` is not a palindrome, the only choice is to check a longer one.
    - In either case, we can always get the result by checking the longest valid prefix.

```cpp
class Solution {
public:
    bool check1(const string & s1, const string & s2) {
        auto check2 = [](auto & s, int i, int j) {
            while (i < j && s[i] == s[j]) {
                i++; j--;
            }
            return i >= j;
        };
        int i = 0, j = s1.size() - 1;
        while (i < j && s1[i] == s2[j]) {
            i++; j--;
        }
        return check2(s2, i, j) || check2(s1, i, j);
    }
    bool checkPalindromeFormation(string a, string b) {
        return check1(a, b) || check1(b, a);
    }
};
```