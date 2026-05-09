# Top K Frequent Words — LeetCode #692
# https://leetcode.com/problems/top-k-frequent-words/
# Time: O(n log n) · Space: O(n)

from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        freq = Counter(words)
        sorted_words = sorted(
            freq.keys(),
            key=lambda word: (-freq[word], word)
        )
        return sorted_words[:k]
