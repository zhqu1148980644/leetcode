---
title:  Validate Stack Sequences
date: 2021-01-04
---
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

```
Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
```

 

#### Note:

-    0 <= pushed.length == popped.length <= 1000
-    0 <= pushed[i], popped[i] < 1000
-    pushed is a permutation of popped.
-    pushed and popped have distinct values.


#### 提示：

-    0 <= pushed.length == popped.length <= 1000
-    0 <= pushed[i], popped[i] < 1000
-    pushed 是 popped 的排列。


##### Solutions

1. ##### simulation O(n) S(1)

- prerequisites: all elements are `unique`.
- Emulate the process of pushing and popping, whenever the current top of stack equals to the head of current popped sequence, pop the top element otherwise the head element wil change.
- The space complexity is `O(1)` when we use inplace stack.

```cpp
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> s;
        int i = 0;
        for (auto & val : pushed) {
            s.push(val);
            while (!s.empty() && s.top() == popped[i]) {
                s.pop();
                i++;
            }
        }

        return s.empty();

    }
};
```

- In place

```cpp
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int st = 0, i = 0;
        for (auto n : pushed) {
            pushed[st++] = n;
            while (st && pushed[st - 1] ==  popped[i]) {
                st--; i++;
            }
        }

        return st == 0;
    }
};
```