---
title: Gray Code
date: 2021-01-04
---
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].


#### Solutions

1. ##### math

- reference: https://leetcode-cn.com/problems/gray-code/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/



```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res = {0};
        int head = 1;
        for (int i = 1; i <= n; i++) {
            // two parts
            // '0' + bin(digit) in the         last level
            // '1' + bin(digit) in the reverse(last level)
            for (int j = res.size() - 1; j >= 0; j--)
                res.push_back(res[j] + head);
            head <<= 1;
        }
        return res;
    }
};
```