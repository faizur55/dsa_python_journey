# Meeting Rooms II — LeetCode #253
# https://leetcode.com/problems/meeting-rooms-ii/
# Time: O(n log n) · Space: O(n)

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])  # sort by start
        heap = []   # tracks end times of rooms

        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heapreplace(heap, end)  # reuse room
            else:
                heapq.heappush(heap, end)     # new room

        return len(heap)
