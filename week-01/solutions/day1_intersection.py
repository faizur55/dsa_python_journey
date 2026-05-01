# Intersection of Two Arrays — LeetCode #349
# https://leetcode.com/problems/intersection-of-two-arrays/
# Time: O(n+m) · Space: O(n)

class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        result = set()
        for x in nums2:
            if x in set1:
                result.add(x)
        return list(result)
