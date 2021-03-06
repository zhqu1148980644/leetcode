---
title: Matchsticks to Square
date: 2021-01-04
---
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

#### Solutions

1. ##### dfs

- A special case(k == 4) for `problem 698 Partition to K Equal Sum Subsets`

```cpp
class Solution {
public:
    bool makesquare(vector<int>& nums) {
        if (!nums.size()) return false;
        size_t total = accumulate(nums.begin(), nums.end(), size_t{0});
        
        int k = 4;
        if (total % k) return false;
        size_t target = total / k, len = nums.size();
        int allused = (1 << len) - 1;
        // search from the largest to the smallest.
        sort(nums.rbegin(), nums.rend());
        if (nums[0] > target) return false;

        function<bool(int, int, int)> solve = [&](int state, int sum, int st) {
            if (state == allused) return true;
            int max = target - (sum % target);
            for (int i = st; i < len; i++) {
                if (state & (1 << i) || nums[i] > max)
                    continue;
                // if this subset is fullfilled, start a new search from the beginning.
                if (solve(state | (1 << i), sum + nums[i], nums[i] == max ? 0 : i + 1))
                    return true;
            }
            return false;
        };

        return solve(0, 0, 0);

    }
};
```