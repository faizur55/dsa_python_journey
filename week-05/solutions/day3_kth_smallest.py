# Kth Smallest in BST — LeetCode #230
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Time: O(h+k) · Space: O(h)

class Solution:
    def kthSmallest(self, root, k):
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val

            current = current.right
