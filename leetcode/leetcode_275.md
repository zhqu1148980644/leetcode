---
title: H Index II
date: 2021-01-04
---
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?


#### Solutions

- Simplified version of `problem 274`.

1. ##### greedy O(n)

```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        for (int i = 0; i < n; i++) {
            if (i + 1 > citations[n - i - 1])
                return i;
        }

        return citations.size();
    }
};
```

2. ##### binary search O(log(n))

- Use binary search to find the index of the first element in the trailing part.

```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        // hi must be n, for case [0] should return 0
        int lo = 0, hi = n;
        while (lo < hi) {
            int mid = lo + ((hi - lo) >> 1);
            if (citations[mid] >= n - mid) {
                hi = mid;
            }
            else {
                lo = mid + 1;
            }
        }
        return n - lo;
    }
};
```