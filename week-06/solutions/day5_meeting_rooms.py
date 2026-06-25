# Meeting Rooms — LeetCode #252 (Premium)
# Logic: sort by start, check consecutive overlap
# Time: O(n log n) · Space: O(1)

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True
