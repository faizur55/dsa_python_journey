# First Unique Character — LeetCode #387
# https://leetcode.com/problems/first-unique-character-in-a-string/
# Time: O(n) · Space: O(1)

from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        freq = Counter(s)
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        return -1
