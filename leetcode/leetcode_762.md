---
title: Prime Number of Set Bits in Binary Representation
date: 2021-01-04
---
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.

#### Solutions

1. ##### straight forward

```cpp
class Solution {
public:
    vector<bool> checkprime(int n) {
        vector<bool> isprime(n + 1, true);
        isprime[0] = isprime[1] = false;
        for (int i = 2; i * i <= n; i++)
            for (int j = i * i; j <= n; j += i)
                isprime[j] = false;
        return isprime;
    }
    inline int countbit(int n) {
        int res = 0;
        while (n) {
            res++;
            n &= (n - 1);
        }
        return res;
    }
    int countPrimeSetBits(int L, int R) {
        auto isprime = checkprime(32);
        int res = 0;
        while (L <= R)
            res += isprime[countbit(L++)];
        
        return res;
    }
};
```