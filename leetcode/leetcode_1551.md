---
title: 1551. Minimum Operations to Make Array Equal
date: 2021-01-04
---
# 1551. Minimum Operations to Make Array Equal
You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.

 

Example 1:

Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
Example 2:

Input: n = 6
Output: 9
 

Constraints:

1 <= n <= 10^4


#### Solutions

##### 1. math

- Move items toward the center
- if n is odd: sequence of steps are: 2 4 6 8 ...
- else                              : 1 2 4 6 ...

```cpp
class Solution {
public:
    int minOperations(int n) {
        if (n <= 1) return 0;
        int num = n / 2;
        // n * a1 + d * (n * (n - 1)) / 2
        return num * (1 + (n & 1)) + (num - 1) * num;
    }
};
```