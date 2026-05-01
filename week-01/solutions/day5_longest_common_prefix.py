# Longest Common Prefix — LeetCode #14
# https://leetcode.com/problems/longest-common-prefix/
# Time: O(n·m) · Space: O(m)

class Solution:
    def longestCommonPrefix(self, strs):
        prefix = []
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix.append(chars[0])
            else:
                break
        return ''.join(prefix)
