---
title: 5661. Latest Time by Replacing Hidden Digits
date: 2021-01-24
---

# 5661. Latest Time by Replacing Hidden Digits

You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

 

Example 1:

Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
Example 2:

Input: time = "0?:3?"
Output: "09:39"
Example 3:

Input: time = "1?:22"
Output: "19:22"
 

Constraints:

time is in the format hh:mm.
It is guaranteed that you can produce a valid time from the given string.


#### Solutions

1. ##### straight forward

```c++
class Solution {
public:
    string maximumTime(string time) {
        char c1 = time[0], c2 = time[1], c3 = time[3], c4 = time[4];
        if (c1 == '?' && c2 == '?') {
            c1 = '2'; c2 = '3';
        }
        else if (c1 == '?')
            c1 = c2 <= '3' ? '2' : '1';
        else if (c2 == '?')
            c2 = c1 == '2' ? '3' : '9';
        
        if (c3 == '?') c3 = '5';
        if (c4 == '?') c4 = '9';

        return {c1, c2, ':', c3, c4};
    }
};
```

2. ##### check for all combinations

- borrowed from others.

```c++
class Solution {
public:
    string maximumTime(string time) {
        for (int h = 23; h >= 0; h--)
            for (int m = 59; m >= 0; m--) {
                string curt = time;
                curt[0] = h / 10 + '0';
                curt[1] = h % 10 + '0';
                curt[3] = m / 10 + '0';
                curt[4] = m % 10 + '0';
                bool valid = true;
                for (int i = 0; i < 5; i++) {
                    if (time[i] != '?' && time[i] != curt[i]) {
                        valid = false;
                        break;
                    }
                }
                if (valid)
                    return curt;
            }
        return "00:00";
    }
};
```