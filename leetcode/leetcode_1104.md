---
title: Path In Zigzag Labelled Binary Tree
date: 2021-01-04
---
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

 

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6


#### Solutions

1. ##### bit operations

- For a given node with value `n`, the parent node equals to:
    - right shift n by 1
    - reverse bits after the leftmost 1 bit.

```cpp
class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        // pos is the position of the leftmost 1 bit.
        int pos = 0;
        for (int i = 0; i < 30; i++)
            if (label & (1 << i))
                pos = i;
    
        vector<int> res;
        while (pos >= 0) {
            res.push_back(label);
            // reverse bits
            label = (label >> 1) ^ ((1 << pos) - 1);
            // preserve the leftmost 1 bit.
            if(--pos >= 0) label |= (1 << pos);
        }

        reverse(res.begin(), res.end());
        return res;
    }
};
```