---
title: 24 Game
date: 2021-01-04
---
#### You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

```
Example 1:

Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24

Example 2:

Input: [1, 2, 1, 2]
Output: False
```

#### Note:

-    The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
-    Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
-    You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

#### Solutions

1. ##### backtrack with dfs

```cpp
class Solution {
public:
    vector<char> operations = {'+', '-', '*', '/'};
    bool solve(vector<double> nums) {
        if (nums.size() == 1)
            return abs(nums[0] - 24) < 1e-7;
    
        for (int i = 0; i < nums.size(); i++)
            for (int j = 0; j < nums.size(); j++) {
                if (i == j) continue;
                vector<double> newnums;
                for (int k = 0; k < nums.size(); k++)
                    if (k != i && k != j) newnums.push_back(nums[k]);
                newnums.push_back(0);
                double n1 = nums[i], n2 = nums[j];
                for (auto & op : operations) {
                    if (((op == '+' || op == '*') && i > j)
                        || (op == '/' && n2 == 0))
                        continue;
                    double res;
                    switch (op) {
                        case ('+'): res = n1 + n2; break;
                        case ('-'): res = n1 - n2; break;
                        case ('*'): res = n1 * n2; break;
                        case ('/'): res = n1 / n2; break;
                    }
                    newnums.back() = res;
                    if (solve(newnums))
                        return true;
                }

            }
        return false;
    }
    bool judgePoint24(vector<int>& nums) {
        return solve(vector<double>(nums.begin(), nums.end()));
    }
};
```

- Python version
- Borrowed from stephan

```python
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        return any(self.judgePoint24([res] + rest)
                    for a, b, *rest in itertools.permutations(nums)
                    for res in {a + b, a - b, a * b, b and a / b})
```


2. ##### deque

- reference: https://leetcode-cn.com/problems/24-game/solution/c-shuang-duan-dui-lie-de-miao-yong-36xing-you-jie-/
- Use deque to save time for constantly rebuilding vectors.

```cpp
class Solution {
public:
    bool gen(deque<double> & q, double res) {
        q.push_back(res);
        bool find = solve(q);
        q.pop_back();
        return find;
    }
    bool solve(deque<double> & q) {
        if (q.size() == 1)
            return abs(q.front() - 24) <= 1e-5;
        // must save size
        int size = q.size();
        // 2 * C(n, 2) = n * (n - 1)
        for (int i = 0; i < size; i++) {
            double a = q.front(); q.pop_front();
            for (int j = 1; j < size; j++) {
                double b = q.front(); q.pop_front();
                if (gen(q, a + b)
                || gen(q, a - b)
                || gen(q, a * b)
                || (b ? gen(q, a / b) : 0))
                    return true;
                q.push_back(b);
            }
            q.push_back(a);
        }
        return false;
    }
    bool judgePoint24(vector<int>& nums) {
        deque<double> dq(nums.begin(), nums.end());
        return solve(dq);
    }
};
```