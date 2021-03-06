---
title: Sum of Two Integers
date: 2021-01-04
---
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1


#### Solutions

1. ##### bit operation

- reference: https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-1xing-dai-ma-chao-95-by-mantoufan/

```cpp
class Solution {
public:
    int getSum(int a, int b) {
        // loop until the carry part changes to 0
        while (b) {
            // 0 + 0 == 0 ^ 0  0 + 1 == 0 ^ 1   1 + 1 == 1 ^ 1 + carry
            int sum = a ^ b;
            // store carry part in b
            b = ((unsigned int)a & b) << 1;
            a = sum;
        }
        return a;
    }
};
```