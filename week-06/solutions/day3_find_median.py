# Find Median From Data Stream — LeetCode #295
# https://leetcode.com/problems/find-median-from-data-stream/
# addNum: O(log n) · findMedian: O(1)

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []   # max heap (lower half)
        self.large = []   # min heap (upper half)

    def addNum(self, num):
        heapq.heappush(self.small, -num)

        if self.small and self.large and \
           -self.small[0] > self.large[0]:
            heapq.heappush(self.large,
                          -heapq.heappop(self.small))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large,
                          -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small,
                          -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
