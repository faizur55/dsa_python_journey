# Majority Element — LeetCode #169
# https://leetcode.com/problems/majority-element/
# Approach 1: Counter — Time: O(n) · Space: O(n)
# Approach 2: Boyer-Moore — Time: O(n) · Space: O(1)

from collections import Counter

class Solution:
    # Approach 1 — Counter
    def majorityElement_v1(self, nums):
        freq = Counter(nums)
        n = len(nums)
        for num, count in freq.items():
            if count > n // 2:
                return num

    # Approach 2 — Boyer-Moore Voting (optimal)
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
