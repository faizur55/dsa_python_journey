# Car Pooling — LeetCode #1094
# https://leetcode.com/problems/car-pooling/
# Time: O(n) · Space: O(1)

class Solution:
    def carPooling(self, trips, capacity):
        stops = [0] * 1001

        for passengers, start, end in trips:
            stops[start] += passengers
            stops[end]   -= passengers

        current = 0
        for stop in stops:
            current += stop
            if current > capacity:
                return False

        return True
