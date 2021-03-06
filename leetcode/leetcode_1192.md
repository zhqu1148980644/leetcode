---
title: Critical Connections in a Network
date: 2021-01-04
---
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.

#### Solutions

1. ##### dfs

- reference: https://zxi.mytechroad.com/blog/graph/leetcode-1192-critical-connections-in-a-network/
- reference: https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/DFS-detailed-explanation-O(orEor)-solution
- Edges within a cycle are not critical edges. 
    - During the dfs search, after traversed nodes are indexed by their visiting order, the end node of a cycle(compared to the first visited node in the cycle) will visit the root node(with lower rank), thus finding himself within a cycle. 
    - To make all parent be  noticed too, this end node can return the lowest rank in neighbors back to the parent's call, by this way, all parents within the cycle will be inferred that there is a node with `rank <= theirs`. Thus all nodes within a cycle can be detected.

```cpp
class Solution {
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<vector<int>> g(n), res;
        vector<int> ranks(n, INT_MAX);

        for (auto & e : connections) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }

        int r = 0;
        function<int(int, int)> tarjan = [&](int cur, int pa) {
            int rank = ranks[cur] = ++r;
            for (auto out : g[cur]) {
                if (out == pa) continue;
                // add into result only if the outnode is traversed the first time
                if (ranks[out] == INT_MAX) {
                    int minrank = tarjan(out, cur);
                    if (ranks[cur] < minrank)
                        res.push_back({cur, out});
                    rank = min(rank, minrank);
                }
                else
                    // used for the end of a cycle finding the root
                    rank = min(rank, ranks[out]);
            }
            // return the minimum rank scanned in dfs
            // if there is a cycle, all nodes in a cycle will return the rank of the root.
            return rank;
        };
        // since all nodes are connected(this problem), randomly choose a starting point
        tarjan(0, -1);
        return res;
    }
};
```