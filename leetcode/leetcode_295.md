---
title:  Find Median from Data Strea
date: 2021-01-04
---
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,

```
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.

 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```
 

#### Follow up:

-    If all integer numbers from the stream are between 0 and 100, how would you optimize it?
-    If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?


#### Solutions

1. ##### heap

- Use max heap to record the first half of elements and min heap to record the last half of elements.
- Then the midian can be quickly calculated in `O(log(n))` time.
- During the process of adding numbers, we need to ensure the balance between two heaps.

```cpp
class MedianFinder {
    priority_queue<int, vector<int>, less<int>> lo;
    priority_queue<int, vector<int>, greater<int>> hi;
public:
    /** initialize your data structure here. */
    MedianFinder() {
        lo.push(INT_MIN);
        hi.push(INT_MAX);
    }
    
    void addNum(int num) {
        if (lo.size() == hi.size()) {
            if (num <= lo.top())
                lo.push(num);
            else
                hi.push(num);
        }
        else {
            if (lo.size() > hi.size()) {
                if (num <= lo.top()) {
                    hi.push(lo.top());
                    lo.pop(); lo.push(num);
                }
                else
                    hi.push(num);
            }
            else {
                if (num < hi.top())
                    lo.push(num);
                else {
                    lo.push(hi.top());
                    hi.pop(); hi.push(num);
                }
            }
        }
    }
    
    double findMedian() {

        if (lo.size() == hi.size())
            return (double)(lo.top() + hi.top()) / 2;
        else if (lo.size() > hi.size())
            return lo.top();
        else
            return hi.top();
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```


- Or another version.
- Borrowed from official answer.


```cpp
class MedianFinder {
    priority_queue<int, vector<int>, less<int>> lo;
    priority_queue<int, vector<int>, greater<int>> hi;
public:
    /** initialize your data structure here. */
    MedianFinder() {
    }
    
    void addNum(int num) {
        lo.push(num);
        hi.push(lo.top());
        lo.pop();
        if (lo.size() < hi.size()) {
            lo.push(hi.top());
            hi.pop();
        }
    }
    
    double findMedian() {
        if (lo.size() == hi.size())
            return (double)(lo.top() + hi.top()) / 2;
        else
            return lo.top();
    }
};
```


2. ##### binary search tree

```cpp
class MedianFinder {
public:
    multiset<int> s;
    multiset<int>::iterator mid;
    /** initialize your data structure here. */
    MedianFinder() {

    }
    
    void addNum(int num) {
        int size = s.size();
        s.insert(num);
        if (size == 0)
            mid = s.begin();
        else {
            if (num < *mid)
                mid = (size & 1) ? prev(mid) : mid;
            else
                mid = (size & 1) ? mid : next(mid);
        }
    }
    
    double findMedian() {
        if (s.size() & 1)
            return *mid;
        else {
            return (*mid + *next(mid)) / 2.0;
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```