---
title: 5740. Longest Substring Of All Vowels in Order
date: 2021-04-25
---

# 5740. Longest Substring Of All Vowels in Order

A string is considered beautiful if it satisfies the following conditions:

Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
Example 2:

Input: word = "aeeeiiiioooauuuaeiou"
Output: 5
Explanation: The longest beautiful substring in word is "aeiou" of length 5.
Example 3:

Input: word = "a"
Output: 0
Explanation: There is no beautiful substring, so return 0.
 

Constraints:

1 <= word.length <= 5 * 105
word consists of characters 'a', 'e', 'i', 'o', and 'u'.


#### Solutions

1. ##### greedy approach

```c++
class Solution {
public:
    int longestBeautifulSubstring(string word) {
        vector<int> index(126, -1);
        int ci = 0;
        for (auto c : {'a', 'e', 'i', 'o', 'u'})
            index[c] = ci++;
        
        int i = 0, res = 0;
        while (i < word.size()) {
            // find the starting character 'a'
            if (word[i] == 'a') {
                int j = i + 1;
                // ensure character[j] >= character[j - 1]
                while (j < word.size() 
                && index[word[j]] <= index[word[j - 1]] + 1 
                && index[word[j]] >= index[word[j - 1]])
                    j++;
                if (word[j - 1] == 'u')
                    res = max(j - i, res);
                i = j;
            }
            else
                i++;
        }
        return res;
    }
};
```