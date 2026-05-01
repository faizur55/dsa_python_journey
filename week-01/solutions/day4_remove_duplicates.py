# Remove Duplicates from Sorted Array — LeetCode #26
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Time: O(n) · Space: O(1)

class Solution:
    def removeDuplicates(self, nums):
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
