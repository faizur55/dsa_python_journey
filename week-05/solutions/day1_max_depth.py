# Maximum Depth of Binary Tree — LeetCode #104
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Time: O(n) · Space: O(h)

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        left_depth  = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
