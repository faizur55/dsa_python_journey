# Kth Largest Element — LeetCode #215
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Time: O(n log k) · Space: O(k)

import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
