# Reorder List — LeetCode #143
# https://leetcode.com/problems/reorder-list/
# Time: O(n) · Space: O(1)

class Solution:
    def reorderList(self, head):
        # Step 1 — find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2 — reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # Step 3 — merge alternately
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
