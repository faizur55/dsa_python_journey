# Group Anagrams — LeetCode #49
# https://leetcode.com/problems/group-anagrams/
# Time: O(n·k log k) · Space: O(nk)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())
