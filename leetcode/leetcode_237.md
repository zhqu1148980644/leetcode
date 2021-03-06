---
title: Delete Node in a Linked List
date: 2021-01-04
---
#### Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

 

```
Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
```

 

#### Note:

-    The linked list will have at least two elements.
-    All of the nodes' values will be unique.
-    The given node will not be the tail and it will always be a valid node of the linked list.
-    Do not return anything from your function.

#### Solutions

1. ##### swap node value


```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        ListNode * del = node->next;
        node->next = node->next->next;
        delete del;
    }
};
```

Or

```cpp
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode * del = node->next;
        // copy the value of the next node.
        *node = *(node->next);
        // remember to delete the next node.
        delete del;
    }
};
```