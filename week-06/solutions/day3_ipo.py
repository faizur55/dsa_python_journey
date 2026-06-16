# IPO — LeetCode #502
# https://leetcode.com/problems/ipo/
# Time: O(n log n) · Space: O(n)

import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = sorted(zip(capital, profits))
        available = []
        i = 0

        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(available, -projects[i][1])
                i += 1

            if not available:
                break

            w += -heapq.heappop(available)

        return w
