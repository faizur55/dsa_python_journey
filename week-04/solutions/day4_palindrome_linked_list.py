# Palindrome Linked List — LeetCode #234
# https://leetcode.com/problems/palindrome-linked-list/
# Time: O(n) · Space: O(1)

class Solution:
    def isPalindrome(self, head):
        # Step 1 — find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2 — reverse second half
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Step 3 — compare both halves
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
