---
title: 5652. Swapping Nodes in a Linked List
date:
---

# 5652. Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
Example 3:

Input: head = [1], k = 1
Output: [1]
Example 4:

Input: head = [1,2], k = 1
Output: [2,1]
Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100


#### Solutions

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        int len = 0;
        ListNode * tmp = head;
        while (tmp && ++len)
            tmp = tmp->next;

        auto node = [&](int k) {
            ListNode * cur = head;
            for (int i = 1; i < k; i++)
                cur = cur->next;
            return cur;
        };

        auto left = node(k);
        auto right = node(len - k + 1);
        swap(left->val, right->val);

        return head;
    }
};
```

or. reference: https://leetcode-cn.com/circle/discuss/aozkiz/view/hLT7uA/

```c++
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        auto a = head, b = head, p = head;
        for(int i = 1; p; i += 1){
            if(i < k) a = a->next;
            if(i > k) b = b->next;
            p = p->next;
        }
        swap(a->val, b->val);
        return head;
    }
};
```