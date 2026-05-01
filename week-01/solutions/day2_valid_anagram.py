# Valid Anagram — LeetCode #242
# https://leetcode.com/problems/valid-anagram/
# Time: O(n) · Space: O(1)

from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
