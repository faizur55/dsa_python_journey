# Sort Array By Parity — LeetCode #905
# https://leetcode.com/problems/sort-array-by-parity/
# Time: O(n) · Space: O(1)

class Solution:
    def sortArrayByParity(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] % 2 == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums
