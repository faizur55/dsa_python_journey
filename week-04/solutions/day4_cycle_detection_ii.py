# Linked List Cycle II — LeetCode #142
# https://leetcode.com/problems/linked-list-cycle-ii/
# Time: O(n) · Space: O(1)

class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
