---
title: 5635. Construct the Lexicographically Largest Valid Sequence
data:
---

# 5635. Construct the Lexicographically Largest Valid Sequence

Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
 

Constraints:

1 <= n <= 20

#### Solutions

1. ##### dfs by recursion

```c++
class Solution {
public:
    vector<int> nums;
    vector<bool> used;
    bool solve( int i, int n) {
        if (i >= nums.size()) return true;
        // has been settled, move to the next position
        if (nums[i] != 0) return solve(i + 1, n);
        for (int cur = n; cur >= 1; cur--) {
            // skip used number
            if (used[cur]) continue;
            int diff = cur != 1 ? cur : 0;
            // check if the paired position is available
            if (i + diff < nums.size() && nums[i + diff] == 0) {
                nums[i] = cur;
                nums[i + diff] = cur;
                used[cur] = true;
                if (solve(i + 1, n))
                    return true;
                else {
                    nums[i] = nums[i + diff] = 0;
                    used[cur] = false;
                }
            }
        }
        return false;
    }
    vector<int> constructDistancedSequence(int n) {
        nums = vector<int>(2 * n - 1);
        used = vector<bool>(n + 1);
        solve(0, n);
        return nums;
    }
};
```