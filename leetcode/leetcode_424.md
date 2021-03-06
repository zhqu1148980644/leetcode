---
title: Longest Repeating Character Replacement
date: 2021-01-04
---
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


#### Solutions

1. ##### binary search O(26 * nlog(n))

- Almost get TLE.

```cpp
class Solution {
public:
    bool valid(const string & s, int len, int k) {
        if (len > s.size()) return false;
        vector<int> count(26);
        auto ok = [&] {
            return len - *max_element(count.begin(), count.end()) <= k;
        };
        for (int i = 0; i < len; i++)
            count[s[i] - 'A']++;
        if (ok()) return true;
        for (int i = len; i < s.size(); i++) {
            count[s[i - len] - 'A']--;
            count[s[i] - 'A']++;
            if (ok()) return true;
        }
        return false;
    }
    int characterReplacement(string s, int k) {
        int n = s.size(); if (!n) return 0;
        int lo = 1, hi = s.size();

        while (lo < hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (valid(s, mid + 1, k))
                lo = mid + 1;
            else
                hi = mid;
        }

        return lo;
    }
};
```



2. ##### sliding window O(n)

```cpp

```