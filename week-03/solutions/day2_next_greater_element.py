# Next Greater Element I — LeetCode #496
# https://leetcode.com/problems/next-greater-element-i/
# Time: O(n+m) · Space: O(n)

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                val = stack.pop()
                next_greater[val] = num
            stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1
        return [next_greater[num] for num in nums1]
