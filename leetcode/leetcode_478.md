---
title: Generate Random Point in a Circle
date: 2021-01-04
---
Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:

input and output values are in floating-point.
radius and x-y position of the center of the circle is passed into the class constructor.
a point on the circumference of the circle is considered to be in the circle.
randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
Example 1:

Input: 
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
Example 2:

Input: 
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.



#### Solutions

1. ##### reject sampling

```cpp
class Solution {
public:
    double xc, yc, radius;
    mt19937 gen{random_device{}()};
    uniform_real_distribution<double> und{0, 1};

    Solution(double radius, double x_center, double y_center) 
    : xc(x_center), yc(y_center), radius(radius) {

    }
    
    vector<double> randPoint() {
        auto x0 = xc - radius;
        auto y0 = yc - radius;
        while (true) {
            // ranomd generation in square with width of 2radius
            auto x = x0 + und(gen) * 2 * radius;
            auto y = y0 + und(gen) * 2 * radius;
            // discard samples outside the circle
            if (sqrt(pow(x - xc, 2) + pow(y - yc, 2)) <= radius)
                return {x, y};
        }
    }
};
```

2. ##### another method

- Not understood, check the official answer: https://leetcode-cn.com/problems/generate-random-point-in-a-circle/solution/zai-yuan-nei-sui-ji-sheng-cheng-dian-by-leetcode/