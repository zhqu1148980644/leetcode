---
title: 5664. Building Boxes
date: 2021-01-24
---

# 5664. Building Boxes

You have a cubic storeroom where the width, length, and height of the room are all equal to n units. You are asked to place n boxes in this room where each box is a cube of unit side length. There are however some rules to placing the boxes:

You can place the boxes anywhere on the floor.
If box x is placed on top of the box y, then each side of the four vertical sides of the box y must either be adjacent to another box or to a wall.
Given an integer n, return the minimum possible number of boxes touching the floor.

 

Example 1:



Input: n = 3
Output: 3
Explanation: The figure above is for the placement of the three boxes.
These boxes are placed in the corner of the room, where the corner is on the left side.
Example 2:



Input: n = 4
Output: 3
Explanation: The figure above is for the placement of the four boxes.
These boxes are placed in the corner of the room, where the corner is on the left side.
Example 3:



Input: n = 10
Output: 6
Explanation: The figure above is for the placement of the ten boxes.
These boxes are placed in the corner of the room, where the corner is on the back side.
 

Constraints:

1 <= n <= 109


#### Solutions

- The best solution is to place the boxes in the way of `example 3`.

1. ##### greedy O(n^1/2)

- reference: https://leetcode-cn.com/problems/building-boxes/solution/fang-zhi-he-zi-zhong-gui-zhong-ju-de-si-wfjiu/

```c++
class Solution {
public:
    int minimumBoxes(int n) {
        // full
        int cells = 0, row = 1;
        while (cells + ((row + 1) * row / 2) <= n) {
            cells += (row + 1) * row / 2;
            row++;
        }

        row -= 1;
        int area = (row + 1) * row / 2, inc = 0;
        // append new box in the last row
        while (cells < n) {
            area++;
            cells += 1 + inc;
            inc++;
        }

        return area;
    }
};
```

2. ##### math with binary search O(log(n))

- Denotes `n` as the number of levels(equals to the lenght of the last row in the bottom). Then the maximum number of boxes can be formed is:
- `n * (n + 1) * (n + 2) / 6 == (x + 1) * x / 2 + (x + 2) * (x + 1) / 2 + ... (n + 1) * n / 2`
- Unlike the first solution, we use binary search to the find the base number of leaves.

```c++
class Solution {
public:
    size_t numbox(size_t level) {
        return level * (level + 1) * (level + 2) / 6;
    }
    int minimumBoxes(int n) {
        // full
        size_t lo = 1, hi = n;
        while (lo < hi) {
            size_t mid = lo + ((hi - lo) >> 1);
            if (numbox(mid) <= n)
                lo = mid + 1;
            else
                hi = mid;
        }

        size_t level = lo - 1, boxes = numbox(level);
        lo = 0; hi = level + 1;
        // append new boxes in the last row
        while (lo < hi) {
            size_t mid = lo + ((hi - lo) >> 1);
            if (boxes + (mid + 1) * mid / 2 < n)
                lo = mid + 1;
            else
                hi = mid;
        }

        return (level + 1) * level / 2 + lo;
    }
};

```