# Longest Repeating Character Replacement — LeetCode #424
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Time: O(n) · Space: O(1)

from collections import Counter

class Solution:
    def characterReplacement(self, s, k):
        count = Counter()
        L = 0
        max_len = 0
        max_freq = 0
        for R in range(len(s)):
            count[s[R]] += 1
            max_freq = max(max_freq, count[s[R]])
            while (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1
            max_len = max(max_len, R - L + 1)
        return max_len
