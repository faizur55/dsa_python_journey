# Maximum Vowels in Substring — LeetCode #1456
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Time: O(n) · Space: O(1)

class Solution:
    def maxVowels(self, s, k):
        vowels = set('aeiou')
        window_count = sum(1 for c in s[:k] if c in vowels)
        max_count = window_count
        for i in range(k, len(s)):
            window_count += (s[i] in vowels)
            window_count -= (s[i-k] in vowels)
            max_count = max(max_count, window_count)
        return max_count
