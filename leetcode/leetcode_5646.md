---
title: 5646. Minimum Number of People to Teach
date: 2021-01-24
---

# 5646. Minimum Number of People to Teach

On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

There are n languages numbered 1 through n,
languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 

Example 1:

Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.
Example 2:

Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
Output: 2
Explanation: Teach the third language to users 1 and 2, yielding two users to teach.
 

Constraints:

2 <= n <= 500
languages.length == m
1 <= m <= 500
1 <= languages[i].length <= n
1 <= languages[i][j] <= n
1 <= u​​​​​​i < v​​​​​​i <= languages.length
1 <= friendships.length <= 500
All tuples (u​​​​​i, v​​​​​​i) are unique
languages[i] contains only unique values


#### Solutions

1. ##### straight forward O(mn)

- Check for all languages.
- Preprocess friendships to filter out connected pairs.

```c++
class Solution {
public:
    int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
        vector<unordered_set<int>> m = {{}};
        for (auto & lv : languages)
            m.emplace_back(lv.begin(), lv.end());
        
        // preprocess to filter connected pairs.
        int nf = friendships.size();
        vector<bool> valid(nf);
        for (int i = 0; i < nf; i++) {
            int p1 = friendships[i][0], p2 = friendships[i][1];
            for (auto l1 : m[p1])
                if (m[p2].count(l1)) {
                    valid[i] = true;
                    break;
                }
        }
        
        // check for all languages
        int res = INT_MAX;
        for (int l = 1; l <= n; l++) {
            int nump = 0;
            for (int i = 0; i < nf; i++) {
                // sckip connected pairs.
                if (valid[i]) continue;
                int p1 = friendships[i][0], p2 = friendships[i][1];
                if (!m[p1].count(l)) {
                    nump++;
                    m[p1].insert(l);
                }
                if (!m[p2].count(l)) {
                    nump++;
                    m[p2].insert(l);
                }
            }
            res = min(res, nump);
        }

        return res; 
    }
};

```