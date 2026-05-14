# Middle of Linked List — LeetCode #876
# https://leetcode.com/problems/middle-of-the-linked-list/
# Time: O(n) · Space: O(1)

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
