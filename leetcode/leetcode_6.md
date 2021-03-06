---
title: ZigZag Conversion
date: 2021-01-04
---
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I


#### Solutions

1. ##### math

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1) return s;
        string res;
        int n = s.size(), maxdis = numRows * 2 - 2, dis = maxdis;
        // fill the results by rows
        // dis represents the distance between the next character in the same row and the current character.
        for (int i = 0; i < numRows; i++) {
            int r = i;
            while (r < n) {
                if (r < n)
                    res += s[r];
                r += dis;
                // for the first and the last row, there is no diagonal element.
                if (r < n && (dis != 0 && dis != maxdis))
                    res += s[r];
                r += (maxdis - dis);
            }
            dis -= 2;
        }
        return res;
    }
};
```


- An elegant solution from the official answer
- The idea is to put characters in a zigzag way while traversing the string.

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1) return s;
        vector<string> rows(numRows);
        int row = 0, godown = -1;
        for (auto c : s) {
            rows[row] += c;
            // change rowindex up and down
            if (row == 0 || row == numRows - 1)
                godown *= -1;
            row += godown;
        }

        string res;
        for (auto & r : rows)
            res += r;
        return res;
    }
};
```