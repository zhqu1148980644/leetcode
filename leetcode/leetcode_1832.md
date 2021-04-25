---
title: 1832. Check if the Sentence Is Pangram
date: 2021-04-10
---

# 1832. Check if the Sentence Is Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.


#### Solutions

```c++
class Solution {
public:
    bool checkIfPangram(string sentence) {
        if (sentence.size() < 26)
            return false;

        vector<bool> meet(26);
        for (auto c : sentence)
            meet[c - 'a'] = true;

        return all_of(meet.begin(), meet.end(), [](auto f) { return f == true;});
    }
};
```