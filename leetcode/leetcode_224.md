---
title: 224. Basic Calculator
date: 2021-03-13
---

# 224. Basic Calculator

Given a string s representing an expression, implement a basic calculator to evaluate it.

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.

#### Solutions

1. ##### stack

- When meeting a '(' start a new calculation point.

```c++
class Solution {
public:
    int calculate(string s) {
        s = "(" + s + ")";
        stack<int> nums;
        stack<char> op;
        int num = 0;
        for (auto c : s) {
            if (isdigit(c)) {
                num = num * 10 + (c - '0'); 
            }
            else if (c == '+' || c == '-' || c == ')') {
                auto prevop = op.top(); op.pop();
                nums.top() += (prevop == '+' ? 1 : -1) * num;
                num = 0;
                if (c == ')') {
                    num = nums.top(); nums.pop();
                }
                else
                    op.push(c);
            }
            else if (c == '(') {
                // start a new calculation
                nums.push(0); op.push('+');
            }
        }

        return num;
    }
};
```

or

```c++
class Solution {
public:
    int calculate(string s) {
        int res = 0, sign = 1, num = 0;
        stack<int> st;
        for (auto c : s) {
            if (isdigit(c)) {
                num = num * 10 + (c - '0');
            }
            else if (c == '(') {
                st.push(res);
                st.push(sign);
                res = 0, sign = 1;
            }
            else if (c == '+' || c == '-') {
                res += sign * num;
                num = 0;
                sign = c == '+' ? 1 : -1;
            }
            else if (c == ')') {
                res += sign * num;
                sign = st.top(); st.pop();
                res = st.top() + sign * res; st.pop();
                sign = 1; num = 0;
            }
        }

        return res + sign * num;
    }
};
```