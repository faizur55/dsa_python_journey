# Range Sum Query — LeetCode #303
# https://leetcode.com/problems/range-sum-query-immutable/
# Time: O(n) build · O(1) query · Space: O(n)

class NumArray:
    def __init__(self, nums):
        n = len(nums)
        self.prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            self.prefix[i] = self.prefix[i-1] + nums[i-1]

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
