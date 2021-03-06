---
title: Sell Diminishing Valued Colored Balls
date: 2021-01-04
---
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.

 

Example 1:


Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110
Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.
 

Constraints:

1 <= inventory.length <= 105
1 <= inventory[i] <= 109
1 <= orders <= min(sum(inventory[i]), 109)


##### Solutions

1. ##### straight forward with priority queue

- Gets TLE

```cpp
class Solution {
public:
    int maxProfit(vector<int>& inventory, int orders) {
        priority_queue<int> pq(inventory.begin(), inventory.end());
        
        long res = 0;
        while (orders > 0) {
            int num = pq.top(); pq.pop();
            int num1 = pq.size() ? pq.top() : 0;
            int used = max(min(num - num1, orders), 1);
            res += ((long)num + num - used + 1) * used / 2;
            res %= 1000000007;
            orders -= used;
            if (num - used > 0)
                pq.push(num - used);
        }
        return res;
    }
};
```


2. ##### binary search O(nlog(n))

- Use binary search to find the minimum score `mid` with `number of scores >= mid` >= `orders`.
    - In orders to make `number of scores == mid`, Only a part of numbers in the column with the minimum score will be used.


```
1 2 3 4 5 6                 use 1

1 2 3 4 5 6 7 8 9 10        use 5

1 2 3 4 5 6 7 8 9 10        use 6
        |

For orders = 12, the minimum cost column is 5, with only a single 5 is used.
```


```cpp
class Solution {
public:
    int maxProfit(vector<int>& inventory, int orders) {
        sort(inventory.rbegin(), inventory.rend());
        int lo = 1, hi = inventory[0];
        // find the unfull(maybe) column with the minimum cost.
        while (lo < hi) {
            long long mid = lo + ((hi - lo) >> 1);
            long long numgt = 0;
            for (auto num : inventory) {
                if (num < (mid + 1)) break;
                numgt += max(0ll, num - (mid + 1) + 1);
            }
            if (numgt >= orders)
                lo = mid + 1;
            else
                hi = mid;
        }
        // columns are fully used
        long long res = 0;
        for (auto n : inventory) {
            if (n <= lo) break;
            int used = n - lo;
            res += ((long long)n + n - used + 1) * used / 2;
            orders -= used;
        }
        // the last column is partially used
        // numbers in the column of the minimum cost
        res = (res + (long long)orders * lo);
        
        return res % 1000000007;
    }
};
```