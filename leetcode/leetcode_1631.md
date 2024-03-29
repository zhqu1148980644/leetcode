---
title: 1631. Path With Minimum Effort
date: 2021-01-04
---
# 1631. Path With Minimum Effort
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106


#### Solutions


1. ##### dijkstra

- Shortest path problem.

```cpp
class Solution {
public:
#define node(x, y) ((x) * n + (y))
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();

        vector<bool> visited(m * n, false);
        vector<int> mindis(m * n, INT_MAX);
        mindis[0] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.emplace(0, 0);
        
        int target = m * n - 1;
        int dirs[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        while (pq.size()) {
            auto [dis, cur] = pq.top(); pq.pop();
            int x = cur / n, y = cur % n;
            if (visited[cur]) continue;
            if (cur == target) break;
            visited[cur] = true;
            for (auto & d : dirs) {
                int nx = x + d[0], ny = y + d[1];
                int next = node(nx, ny);
                if (nx < 0 || ny < 0 || nx >= m || ny >= n || visited[next])
                    continue;
                int ndis = max(dis, abs(heights[nx][ny] - heights[x][y]));
                if (ndis < mindis[next]) {
                    mindis[next] = ndis;
                    pq.emplace(ndis, next);
                }
            }
        }
        
        return mindis[target];
    }
};
```

2. ##### binary search with bfs search

- reference: https://leetcode-cn.com/problems/path-with-minimum-effort/solution/zui-xiao-ti-li-xiao-hao-lu-jing-by-zerotrac2/

```cpp

```


3. ##### UnionFind O(n2)

- reference: https://leetcode-cn.com/problems/path-with-minimum-effort/solution/zui-xiao-ti-li-xiao-hao-lu-jing-by-zerotrac2/
- Sort all edges in ascending order by their absolute difference between two adjacent nodes.
- Then starting from the edge with the lowest weight, iteratively connect two adjacent nodes untill the source `node(0, 0)` and the destination `node(m - 1, n -1)` are connected. At this time, the weight of the current edge is the final answer.


```cpp
struct UnionFind {
    vector<int> nodes;
    UnionFind(int size) : nodes(size) {
        iota(nodes.begin(), nodes.end(), 0);
    }
    int find(int node) {
        return nodes[node] == node ? 
            node : (nodes[node] = find(nodes[node]));
    }
    bool merge(int node1, int node2) {
        int f1 = find(node1), f2 = find(node2);
        if (f1 == f2) return false;
        nodes[f1] = f2;
        return true;
    }
};
class Solution {
public:
#define node(x, y) ((x) * n + (y))
    int minimumEffortPath(vector<vector<int>>& heights) {
        int dirs[2][2] = {{1, 0}, {0, 1}};
        int m = heights.size(), n = heights[0].size();
        // find all edges and sort them by their weight(absolute difference between adjacent nodes)
        vector<tuple<int, int, int>> edges;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                for (auto & d : dirs) {
                    int x = i + d[0], y = j + d[1];
                    if (x == m || y == n) continue;
                    edges.emplace_back(
                        abs(heights[i][j] - heights[x][y]), 
                        node(i, j), 
                        node(x, y)
                    );
                }
            }
        
        sort(edges.begin(), edges.end());
        UnionFind uf(m * n);
        int src = 0, tgt = m * n - 1;
        // from the edge with the lowest weight, till src and tgt are connected.
        for (auto [w, x, y] : edges) {
            if (uf.merge(x, y) && uf.find(src) == uf.find(tgt))
                return w;
        }

        return 0;
    }
};
```
