# Kth Largest in Stream — LeetCode #703
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Time: O(log k) per add · Space: O(k)

import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
