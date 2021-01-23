---
title: 5647. Decode XORed Permutation
date: 2021-01-24
---

# 5647. Decode XORed Permutation

There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].

Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.

 

Example 1:

Input: encoded = [3,1]
Output: [1,2,3]
Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
Example 2:

Input: encoded = [6,5,4,6]
Output: [2,4,1,5,3]
 

Constraints:

3 <= n < 105
n is odd.
encoded.length == n - 1


#### Solutions

- It's obvious that the whole array can be fetched iteratively by xor operations as long as we have the `first/last` number).

1. ##### bit operation

- For example: array: `[a, b, c, d]`, encoded: `[a ^ b, b ^ c, c ^ d]`
- We can get the last number `d` through the below formula:
    - `d == a ^ b ^ c ^ d ^ (d) ^ (c ^ d) ^ (b ^ d) ^ (a ^ d)`
    - and `a ^ d == suffix xor of the encoded array` 


```c++
class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        int n = encoded.size() + 1;
        int all = 0;
        for (int i = 1; i <= n; i++)
            all ^= i;
        int suffix = 0;
        for (int i = n - 2; i >= 0; i--) {
            suffix ^= encoded[i];
            all ^= suffix;
        }
        
        // now all equals to the last number.
        vector<int> res = {all};
        for (int i = n - 2; i >= 0; i--) {
            res.push_back(res.back() ^ encoded[i]);
        }

        return {res.rbegin(), res.rend()};
    }
};
```