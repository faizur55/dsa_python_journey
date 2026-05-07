# Find All Anagrams in a String — LeetCode #438
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Time: O(n) · Space: O(1)

from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        result = []
        p_count = Counter(p)
        window = Counter(s[:len(p)])

        if window == p_count:
            result.append(0)

        for i in range(len(p), len(s)):
            window[s[i]] += 1
            left = s[i - len(p)]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == p_count:
                result.append(i - len(p) + 1)

        return result
