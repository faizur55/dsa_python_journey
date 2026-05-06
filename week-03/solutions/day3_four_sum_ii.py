# Four Sum II — LeetCode #454
# https://leetcode.com/problems/4sum-ii/
# Time: O(n²) · Space: O(n²)

from collections import Counter

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        ab = Counter(a + b for a in nums1 for b in nums2)
        return sum(ab[-(c + d)] for c in nums3 for d in nums4)
