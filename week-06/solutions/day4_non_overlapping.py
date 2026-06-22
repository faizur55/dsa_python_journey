# Non-overlapping Intervals — LeetCode #435
# https://leetcode.com/problems/non-overlapping-intervals/
# Time: O(n log n) · Space: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])  # sort by END
        removed = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:  # overlap!
                removed += 1                # remove current
            else:
                prev_end = intervals[i][1]  # no overlap → update

        return removed
