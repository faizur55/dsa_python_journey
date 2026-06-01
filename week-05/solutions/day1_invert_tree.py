# Invert Binary Tree — LeetCode #226
# https://leetcode.com/problems/invert-binary-tree/
# Time: O(n) · Space: O(h)

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
