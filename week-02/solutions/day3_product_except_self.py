# Product of Array Except Self — LeetCode #238
# https://leetcode.com/problems/product-of-array-except-self/
# Time: O(n) · Space: O(1)

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        return answer
