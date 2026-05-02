# Continuous Subarray Sum — LeetCode #523
# https://leetcode.com/problems/continuous-subarray-sum/
# Time: O(n) · Space: O(n)

class Solution:
    def checkSubarraySum(self, nums, k):
        seen = {0: -1}
        current_sum = 0
        for i, num in enumerate(nums):
            current_sum += num
            remainder = current_sum % k
            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i
        return False
