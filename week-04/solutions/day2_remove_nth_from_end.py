# Remove Nth Node From End — LeetCode #19
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Time: O(n) · Space: O(1)

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
