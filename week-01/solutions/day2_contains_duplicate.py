# Contains Duplicate — LeetCode #217
# https://leetcode.com/problems/contains-duplicate/
# Time: O(n) · Space: O(n)

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
