# Binary Tree Maximum Path Sum — LeetCode #124
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Time: O(n) · Space: O(h)

class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def solve(node):
            if not node:
                return 0

            left_gain  = max(0, solve(node.left))
            right_gain = max(0, solve(node.right))

            path = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, path)

            return node.val + max(left_gain, right_gain)

        solve(root)
        return self.max_sum
