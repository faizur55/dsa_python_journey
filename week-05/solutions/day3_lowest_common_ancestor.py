# Lowest Common Ancestor BST — LeetCode #235
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Time: O(h) · Space: O(1)

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
