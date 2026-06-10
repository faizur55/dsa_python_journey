# Merge Intervals — LeetCode #56
# https://leetcode.com/problems/merge-intervals/
# Time: O(n log n) · Space: O(n)

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = result[-1][1]

            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])

        return result
