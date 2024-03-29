---
title: 1574. Shortest Subarray to be Removed to Make Array Sorted
date: 2021-01-04
---
# 1574. Shortest Subarray to be Removed to Make Array Sorted
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

A subarray is a contiguous subsequence of the array.

Return the length of the shortest subarray to remove.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
Example 4:

Input: arr = [1]
Output: 0
 

Constraints:

1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9


#### Solutions


1. ##### binary seach O(nlog(n))

```cpp
class Solution {
public:
    bool ok(int len, vector<int> & arr, vector<int> & dec) {
        if (len == arr.size()) return true;
        for (int i = 0; i <= arr.size() - len; i++) {
            // ensure the left part has no reverse pair
            int left = !dec[i] && (!i || i + len == arr.size() || arr[i + len] >= arr[i - 1]);
            // ensure the right part has no reverse [air]
            int right = i + len + 1 >= arr.size() || dec[i + len + 1] == dec.back();
            if (left && right)
                return true; 
        }
        return false;
    }
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size(); if (n <= 1) return 0;
        int numdec = 0;
        vector<int> dec(n + 1);
        for (int i = 1; i < n; i++) {
            dec[i + 1] = numdec += arr[i] < arr[i - 1];
        }

        int lo = 0, hi = arr.size();
        while (lo < hi) {
            int mid = lo + ((hi - lo) / 2);
            if (!ok(mid, arr, dec))
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }
};

```


2. ##### greedy approach O(n)

- Find the first and the last reversing point, then try to compose the final array using full part of prefix or suffix demarcated by these two points.

```cpp
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        if (arr.size() <= 1) return 0;
        int l, r;
        for (l = 0; l < (int)arr.size() - 1; l++) {
            if (arr[l] > arr[l + 1]) break;
        }
        if (l == arr.size() - 1) return 0;
        for (r = arr.size() - 1; r > 0; r--) {
            if (arr[r] < arr[r - 1]) break;
        }
        // two possibilities
        int len1, tmpl = l;
        while (tmpl >= 0 && arr[tmpl] > arr[r]) tmpl--;
        len1 = r - tmpl - 1;
        int len2, tmpr = r;
        while (tmpr < arr.size() && arr[tmpr] < arr[l]) tmpr++;
        len2 = tmpr - l - 1;

        return min(len1, len2);        
    }
};
```