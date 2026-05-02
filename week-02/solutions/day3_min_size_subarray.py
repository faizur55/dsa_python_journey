# Minimum Size Subarray Sum — LeetCode #209
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Time: O(n) · Space: O(1)

class Solution:
    def minSubArrayLen(self, target, nums):
        L = 0
        current_sum = 0
        min_len = float('inf')
        for R in range(len(nums)):
            current_sum += nums[R]
            while current_sum >= target:
                min_len = min(min_len, R - L + 1)
                current_sum -= nums[L]
                L += 1
        return 0 if min_len == float('inf') else min_len
