---
title: 1776. Car Fleet II
date: 2021-03-01
---

# 1776. Car Fleet II

There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.

 

Example 1:

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
Example 2:

Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]
 

Constraints:

1 <= cars.length <= 105
1 <= positioni, speedi <= 106
positioni < positioni+1


#### Solutions

1. ##### Mono stack O(n)

- While checking cars backwards in distance,
- if the next cars's speed is larger than the current car's, then all cars before will not collide with the next car.
    - because fleet's speed will be constraint by the slowest car. 
- in the opposite case, the current car will collide with the next car after a speculated time `t` only if the next car have not been collide with next-next car before time `t`.
- This process can be simulated by a monotonically decreasing stack.

```c++
class Solution {
public:
    vector<double> getCollisionTimes(vector<vector<int>>& cars) {
        int n = cars.size();
        // set to INT_MAX instead of -1, otherwise need more check in while condition
        vector<double> res(n, INT_MAX);
        stack<int> s;

        auto time = [&](int ci, int cj) {
            return double(cars[cj][0] - cars[ci][0]) / (cars[ci][1] - cars[cj][1]);
        };

        for (int i = n - 1; i >= 0; i--) {
            while (s.size() 
            && (cars[s.top()][1] >= cars[i][1] || time(i, s.top()) > res[s.top()]))
                s.pop();
            if (s.size())
                res[i] = time(i, s.top());
            s.push(i);
        }

        for (auto & n : res)
            if (n == INT_MAX)
                n = -1;

        return res;
    }
};
```


2. ##### priority queue

```c++

```
