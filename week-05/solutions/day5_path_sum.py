# Path Sum — LeetCode #112
# https://leetcode.com/problems/path-sum/
# Time: O(n) · Space: O(h)

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0

        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))
