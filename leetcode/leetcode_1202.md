---
title: 1202. Smallest String With Swaps
date:
---

# 1202. Smallest String With Swaps

You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.

#### Solutions

- Similar to problem `5650. Minimize Hamming Distance After Swap Operations`

1. ##### UnionFind

- Use UnionFind to find all connected swapping groups than sort characters in each group independently.

```c++
struct UnionFind {
    vector<int> nodes;
    UnionFind(int size) : nodes(size) {
        iota(nodes.begin(), nodes.end(), 0);
    }
    int find(int node) {
        return nodes[node] == node ? node : (nodes[node] = find(nodes[nodes[node]]));
    }
    void merge(int n1, int n2) {
        int f1 = find(n1), f2 = find(n2);
        if (f1 != f2)
            nodes[f1] = f2;
    }
};
class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int n = s.size();

        UnionFind uf(n);
        for (auto & p : pairs)
            uf.merge(p[0], p[1]);
        

        unordered_map<int, vector<int>> groups;
        for (int i = 0; i < n; i++)
            groups[uf.find(i)].push_back(i);

        for (auto & [g, indexes] : groups) {
            string cs;
            for (auto i : indexes)
                cs += s[i];
            // or use count sort in O(n) time
            sort(cs.begin(), cs.end());
            for (int i = 0; i < cs.size(); i++)
                s[indexes[i]] = cs[i];
        }

        return s;
    }
};
```