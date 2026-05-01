# Single Number — LeetCode #136
# https://leetcode.com/problems/single-number/
# Time: O(n) · Space: O(1)

class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
