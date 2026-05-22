# Copy List with Random Pointer — LeetCode #138
# https://leetcode.com/problems/copy-list-with-random-pointer/
# Time: O(n) · Space: O(n)

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        old_to_new = {}
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            if current.next:
                old_to_new[current].next = old_to_new[current.next]
            if current.random:
                old_to_new[current].random = old_to_new[current.random]
            current = current.next

        return old_to_new[head]
