# K Closest Points to Origin — LeetCode #973
# https://leetcode.com/problems/k-closest-points-to-origin/
# Time: O(n log n) · Space: O(n)

import heapq

class Solution:
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result
