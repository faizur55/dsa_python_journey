# Subarray Sum Equals K — LeetCode #560
# https://leetcode.com/problems/subarray-sum-equals-k/
# Time: O(n) · Space: O(n)

class Solution:
    def subarraySum(self, nums, k):
        count = 0
        current_sum = 0
        seen = {0: 1}
        for num in nums:
            current_sum += num
            complement = current_sum - k
            count += seen.get(complement, 0)
            seen[current_sum] = seen.get(current_sum, 0) + 1
        return count
