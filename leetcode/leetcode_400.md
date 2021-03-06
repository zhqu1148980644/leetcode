---
title:  Nth Digit
date: 2021-01-04
---
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

#### Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

```
Example 1:

Input:
3

Output:
3

Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
```


#### Solutions

1. ##### straight forward

- Just count the number of digits per number when `n` is within `0-9, 10-99 or 100-999, ...`.

```cpp
class Solution {
public:
    int findNthDigit(int n) {
        int cnt = 1, num_digit = 1;
        long base = 1;
        while (true) {
            long nextcnt = cnt + (base * 10 - base) * num_digit;
            if (nextcnt > n)
                break;
            cnt = nextcnt;
            num_digit++; base *= 10;
        }
        n -= cnt;
        base += n / num_digit;
        n -= (n / num_digit) * num_digit;
        return to_string(base)[n] - '0';
    }
};
```

Or

```cpp
class Solution {
public:
    int findNthDigit(int n) {
        int num_digit = 1;
        long base = 1;
        while (n > base * 9 * num_digit) {
            n -= 9 * base * num_digit;
            num_digit++;
            base *= 10;
        }
        n -= 1;
        base += n / num_digit;
        n -= (n / num_digit) * num_digit;
        return to_string(base)[n] - '0';
    }
};
```