---
title: Smallest Sufficient Tea
date: 2021-01-04
---
In a project, you have a list of required skills req_skills, and a list of people.  The i-th person people[i] contains a list of skills that person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill.  We can represent these teams by the index of each person: for example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].

Return any sufficient team of the smallest possible size, represented by the index of each person.

You may return the answer in any order.  It is guaranteed an answer exists.

 

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
 

Constraints:

1 <= req_skills.length <= 16
1 <= people.length <= 60
1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16
Elements of req_skills and people[i] are (respectively) distinct.
req_skills[i][j], people[i][j][k] are lowercase English letters.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.


#### Solutions

1. ##### dynamic programming O(n * 2^16)

- Similar to knapsack problem.
- Since both the number of skills and the number of people are less than 64, we can use integer(bitmap) to represents included skills and people at each state.

```cpp
class Solution {
public:
    vector<int> smallestSufficientTeam(vector<string>& req_skills, vector<vector<string>>& people) {
        int idx = 0;
        unordered_map<string, int> m;
        for (auto & w : req_skills)
            m[w] = idx++;
        
        int n = m.size();
        // all skills are fullfilled
        int target = (1 << n) - 1;
        // dp[included_skills][{num_people, included_people}]
        vector<pair<int, size_t>> dp(1 << n, {0x3f3f3f3f, 0});
        dp[0] = {0, 0};
        // iterate over all people, each person may be included or not.
        for (int p = 0; p < people.size(); p++) {
            // state of current person's skills
            int skills = 0;
            for (auto & w : people[p])
                skills |= 1 << m[w];
    
            for (int s = target; s >= 0; s--) {
                if (dp[s].first == 0x3f3f3f3f || (s | skills) == s)
                    continue;
                int ns = s | skills; // use or to include this person's skills
                auto [nskill, com] = dp[s];
                // if need less people but with the same skills
                if (nskill + 1 < dp[ns].first) {
                    dp[ns] = {nskill + 1, com | (size_t{1} << p)};
                }
            }
        }
        // find selected people
        vector<int> res;
        for (int p = 0; p < people.size(); p++)
            if (dp[target].second & (size_t{1} << p))
                res.push_back(p);

        return res;
    }
};
```