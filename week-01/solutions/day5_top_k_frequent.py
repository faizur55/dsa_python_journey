# Top K Frequent Elements — LeetCode #347
# https://leetcode.com/problems/top-k-frequent-elements/
# Time: O(n log n) · Space: O(n)

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        result = []
        obj = Counter(nums)
        for num, freq in obj.most_common(k):
            result.append(num)
        return result
