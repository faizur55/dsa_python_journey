# Flatten Multilevel Doubly Linked List — LeetCode #430
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Time: O(n) · Space: O(1)

class Solution:
    def flatten(self, head):
        if not head:
            return head

        current = head
        while current:
            if current.child:
                child = current.child
                next_node = current.next

                current.next = child
                child.prev = current
                current.child = None

                tail = child
                while tail.next:
                    tail = tail.next

                tail.next = next_node
                if next_node:
                    next_node.prev = tail

            current = current.next

        return head
