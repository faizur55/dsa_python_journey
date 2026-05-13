# Reverse Linked List — LeetCode #206
# https://leetcode.com/problems/reverse-linked-list/
# Time: O(n) · Space: O(1)

class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
