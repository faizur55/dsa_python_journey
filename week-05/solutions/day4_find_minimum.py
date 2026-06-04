# Find Minimum in Rotated Array — LeetCode #153
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Time: O(log n) · Space: O(1)

class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
