# Ransom Note — LeetCode #383
# https://leetcode.com/problems/ransom-note/
# Time: O(n+m) · Space: O(1)

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        return not (Counter(ransomNote) - Counter(magazine))
