# Two Sum II — LeetCode #167
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Time: O(n) · Space: O(1)

class Solution:
    def twoSum(self, numbers, target):
        L, R = 0, len(numbers) - 1
        while L < R:
            total = numbers[L] + numbers[R]
            if total == target:
                return [L + 1, R + 1]
            elif total < target:
                L += 1
            else:
                R -= 1
