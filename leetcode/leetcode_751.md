---
title: IP to CIDR
date: 2021-01-04
---
Given a start IP address ip and a number of ips we need to cover n, return a representation of the range as a list (of smallest possible length) of CIDR blocks.

A CIDR block is a string consisting of an IP, followed by a slash, and then the prefix length. For example: "123.45.67.89/20". That prefix length "20" represents the number of common prefix bits in the specified range.

Example 1:
Input: ip = "255.0.0.7", n = 10
Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
Explanation:
The initial ip address, when converted to binary, looks like this (spaces added for clarity):
255.0.0.7 -> 11111111 00000000 00000000 00000111
The address "255.0.0.7/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just this one address.

The address "255.0.0.8/29" specifies all addresses with a common prefix of 29 bits to the given address:
255.0.0.8 -> 11111111 00000000 00000000 00001000
Addresses with common prefix of 29 bits are:
11111111 00000000 00000000 00001000
11111111 00000000 00000000 00001001
11111111 00000000 00000000 00001010
11111111 00000000 00000000 00001011
11111111 00000000 00000000 00001100
11111111 00000000 00000000 00001101
11111111 00000000 00000000 00001110
11111111 00000000 00000000 00001111

The address "255.0.0.16/32" specifies all addresses with a common prefix of 32 bits to the given address,
ie. just 11111111 00000000 00000000 00010000.

In total, the answer specifies the range of 10 ips starting with the address 255.0.0.7 .

There were other representations, such as:
["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
but our answer was the shortest possible.

Also note that a representation beginning with say, "255.0.0.7/30" would be incorrect,
because it includes addresses like 255.0.0.4 = 11111111 00000000 00000000 00000100 
that are outside the specified range.
Note:
ip will be a valid IPv4 address.
Every implied address ip + x (for x < n) will be a valid IPv4 address.
n will be an integer in the range [1, 1000].

#### Solutions

1. ##### straight forward

- reference: https://liuyang89116.gitbook.io/my-leetcode-book/post_chapter_2_math/bit-manipulation/problem-751-ip-to-cidr
- In summary, the problem requires us to convert `[startip: startip + n - 1]` into minimum number of CIDRs with the constraint that all ips within a CIDR needs to be within the given range.
    - With out these two constraints, it's easy to get the minimum/maximum number of ICDRs, for example:
    - `0.0.0.0/1` is enough to cover all ips, 1 is the number of ICDRs.
    - `ip/32`, n is the maximum number of ICDRs
- Note that the problem requires all ips within a CIDR are within the given range `[startip: startip + n]`.

```cpp
class Solution {
public:
    // convert 0.0.0.255 to 255
    long iptolong(string & ip) {
        long res = 0;
        istringstream ss(ip);
        string ds;
        while (getline(ss, ds, '.'))
            res = res * 256 + stoi(ds);
        return res;
    }
    // convert interger representation to "x.x.x.x/x"
    string ltoa(long n, int step) {
        array<int, 4> ipv = {0};
        for (int i = 0; i < 4; i++) {
            // 255 or 0x11111111 or 0xff
            ipv[i] = n & 255;
            n >>= 8;
        }
        step >>= 1;
        int numzero = 0;
        while (step && ++numzero) step >>= 1;
        return to_string(ipv[3]) + "." + to_string(ipv[2]) 
        + "." + to_string(ipv[1]) + "." + to_string(ipv[0])
        + "/" + to_string(32 - numzero);
    }
    vector<string> ipToCIDR(string ip, int n) {
        auto ipl = iptolong(ip);
        
        vector<string> res;
        while (n > 0) {
            // at least forward 1 step
            long step = max(1l, ipl & -ipl);
            while (step > n) step /= 2;
            res.push_back(ltoa(ipl, step));
            ipl += step;
            n -= step;
        }

        return res;
    }
};
```