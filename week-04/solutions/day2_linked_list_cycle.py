# Linked List Cycle — LeetCode #141
# https://leetcode.com/problems/linked-list-cycle/
# Time: O(n) · Space: O(1)

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
