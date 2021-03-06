---
title:  Count All Valid Pickup and Delivery Options
date: 2021-01-04
---
Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

 

```
Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

Example 3:

Input: n = 3
Output: 90
```

 

#### Constraints:

-    1 <= n <= 500


#### Solutions


1. ##### dynamic programmig

- Suppose `dp[n - 1] = n`, there are `2 * (n - 1) + 1` insert positions in the previous permutaion. we need to insert the current pair of `Dn` and `Pn` into these positions.
    - DP are inserted into a single position, ie: Dn and Pn are adjacent. there are `C(numpos, 1)` situations.
    - DP are inserted into two different position, there are `C(numpos, 2) ` situations.
    - Thus `dp[n] = dp[n - 1] * (C(numpos, 1) + C(numpos, 2))`.


```cpp
class Solution {
public:
    int countOrders(int n) {
        long prev = 1;
        for (int i = 2; i <= n; i++) {
            long pos = (i - 1) * 2 + 1;
            long cur = prev * (pos + pos * (pos - 1) / 2);
            prev = cur % 1000000007;
        }
        return prev;
    }
};
```