# Reverse Linked List (Recursive) — LeetCode #206
# https://leetcode.com/problems/reverse-linked-list/
# Time: O(n) · Space: O(n) — call stack

class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head
