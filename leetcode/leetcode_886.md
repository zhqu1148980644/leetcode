---
title: Possible Bipartition
date: 2021-01-04
---
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Constraints:

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].


#### Solutions

1. ##### dfs

- Try to color adjacent pair of nodes with difference colors.

```cpp
class Solution {
public:
    enum Color {UNCOLORED, RED, GREEN};
    unordered_map<int, vector<int>> g;
    bool color(vector<Color> & colors, int cur) {
        // not colored yet, start with RED
        if (colors[cur] == UNCOLORED)
            colors[cur] = RED;
        // neighors' color
        Color neic = colors[cur] == RED ? GREEN : RED;
        for (auto out : g[cur]) {
            if (colors[out] == UNCOLORED) {
                colors[out] = neic;
                if (!color(colors, out))
                    return false;
            }
            else if (colors[out] != neic)
                return false;
        }
        return true;
    }

    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        for (auto & e : dislikes) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }

        vector<Color> colors(N + 1, UNCOLORED);
        for (auto & e : dislikes)
            if (!color(colors, e[0]))
                return false;

        return true;
    }
};

```

2. ##### bfs

```cpp
class Solution {
public:
    enum Color {UNCOLORED, RED, GREEN};
    unordered_map<int, vector<int>> g;
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        for (auto & e : dislikes) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }

        vector<Color> colors(N + 1, UNCOLORED);
        for (auto & e : dislikes) {
            if (colors[e[0]] != UNCOLORED)
                continue;
            queue<int> q; q.push(e[0]);
            while (!q.empty()) {
                auto cur = q.front(); q.pop();
                if (colors[cur] == UNCOLORED)
                    colors[cur] = RED;
                Color neic = colors[cur] == RED ? GREEN : RED;
                for (auto out : g[cur]) {
                    if (colors[out] == UNCOLORED) {
                        colors[out] = neic;
                        q.push(out);
                    }
                    else if (colors[out] != neic)
                        return false;
                }
            }
        }

        return true;
    }
};

```


3. ##### Union Find

- Connect disliked people into the same group, then check if there are any inconsistency.

```cpp
struct UnionFind {
    vector<int> sizes, nodes;
    UnionFind(int size) : sizes(size, 1), nodes(size) {
        iota(nodes.begin(), nodes.end(), 0);
    }
    int find(int node) {
        return nodes[node] == node ? node : find(nodes[node]);
    }
    bool merge(int node1, int node2) {
        int f1 = find(node1), f2 = find(node2);
        if (f1 == f2) return false;
        if (sizes[f1] > sizes[f2])
            swap(f1, f2);
        sizes[f2] += sizes[f1];
        nodes[f1] = f2;
        return true;
    }
    bool connected(int node1, int node2) {
        return find(node1) == find(node2);
    }
};
class Solution {
public:
    enum Color {UNCOLORED, RED, GREEN};
    unordered_map<int, vector<int>> g;
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        for (auto & e : dislikes) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        UnionFind uf(N + 1);
        for (auto & e : dislikes) {
            int cur = e[0];
            for (auto out : g[cur]) {
                // if already being within the same group and also they are disliked
                // need at least three groups to cater for
                if (uf.connected(cur, out))
                    return false;
                // connect disliked people into one group
                uf.merge(g[cur][0], out);
            }
        }

        return true;
    }
};

```


4. ##### Union Find

- Borrowed from others.

```cpp
struct UnionFind {
    vector<int> sizes, nodes;
    UnionFind(int size) : sizes(size, 1), nodes(size) {
        iota(nodes.begin(), nodes.end(), 0);
    }
    int find(int node) {
        return nodes[node] == node ? node : find(nodes[node]);
    }
    bool merge(int node1, int node2) {
        int f1 = find(node1), f2 = find(node2);
        if (f1 == f2) return false;
        if (sizes[f1] > sizes[f2])
            swap(f1, f2);
        sizes[f2] += sizes[f1];
        nodes[f1] = f2;
        return true;
    }
    bool connected(int node1, int node2) {
        return find(node1) == find(node2);
    }
};
class Solution {
public:
    enum Color {UNCOLORED, RED, GREEN};
    unordered_map<int, vector<int>> g;
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        UnionFind uf(2 * N + 1);
        for (auto & e : dislikes) {
            int cur = e[0], out = e[1];
            if (uf.connected(cur, out))
                return false;
            // use array[N: 2N + 1) to connect disliked people
            uf.merge(cur, out + N);
            uf.merge(cur + N, out);
        }

        return true;
    }
};

```