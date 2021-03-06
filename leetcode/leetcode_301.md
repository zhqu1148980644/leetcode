---
title: Remove Invalid Parentheses
date: 2021-01-04
---
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]

#### Solutions

1. ##### bfs

```cpp
class Solution {
public:
    inline bool valid(const string & s) {
        int l = 0;
        for (auto c : s) {
            if (!(c == '(' || c == ')'))
                continue;
            if (c == '(')
                l++;
            else if (l)
                l--;
            else return false;
        }
        return l == 0;
    }
    vector<string> removeInvalidParentheses(string s) {
        unordered_set<string> visited;
        visited.insert(s);
        deque<string> q; q.push_back(s);
        if (valid(s)) return {s};

        bool found = false;
        vector<string> res;
        while (q.size() && !found) {
            int size = q.size();
            while (size--) {
                auto cur = move(q.front()); q.pop_front();
                for (int i = 0; i < cur.size(); i++) {
                    string tmp = cur.substr(0, i) + cur.substr(i + 1);
                    if (visited.count(tmp)) continue;
                    if (valid(tmp)) {
                        found = true;
                        res.push_back(tmp);
                    }
                    visited.insert(tmp);
                    if (!found) q.push_back(tmp);
                }
            }
        }
        
        return res;
    }
};
```

2. ##### dfs with pruning

- refrence: https://leetcode-cn.com/problems/remove-invalid-parentheses/solution/dfsjian-zhi-4ms-by-gfy/
- Use dfs to build the string with the proper number of `(/)` deleted, and maintains two variables(curl, curr) representing the curent string's unmatched `(/)`.(Normally the validation are processed after the whole string has been built)
    - Their are two pruning operations:
        - return if `curr > curl`.
        - return if the number of `(/)` needs to be deleted has been decremented to under zero.

```cpp
class Solution {
public:
    string cur;
    // must use hashmap
    unordered_set<string> res;
    // rd/ld means howmany (/) needs to be deleted
    // curl/curr represents the number of unmatched (/) in cur
    void dfs(string & s, int ld, int rd, int curl, int curr, int st) {
        if (st == s.size()) {
            if (curl == 0 && curr == 0)
                res.insert(cur);
        }
        else {
            if (!(s[st] == '(' || s[st] == ')')) {
                cur += s[st];
                dfs(s, ld, rd, curl, curr, st + 1);
                cur.pop_back();
            }
            else {
                // delete the current (/)
                if (ld && s[st] == '(')
                    dfs(s, ld - 1, rd, curl, curr, st + 1);
                if (rd && s[st] == ')')
                    dfs(s, ld, rd - 1, curl, curr, st + 1);
                // retain the current (/)
                if (s[st] == '(') curl++;
                else if (curl) curl--; 
                else curr++;
                if (curr <= curl) {
                    cur += s[st];
                    dfs(s, ld, rd, curl, curr, st + 1);
                    cur.pop_back();
                }
            }
        }
    }

    vector<string> removeInvalidParentheses(string s) {
        int l = 0, r = 0;
        for (auto c : s) {
            if (!(c == '(' || c == ')'))
                continue;
            else if (c == '(') l++;
            else if (l) l--;
            else r++;
        }
        if (l == 0 && r == 0) return {s};
        dfs(s, l, r, 0, 0, 0);
        
        vector<string> vs;
        for (auto & s : res) vs.push_back(move(s));
        return vs;
    }
};
```