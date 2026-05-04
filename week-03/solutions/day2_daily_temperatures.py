# Daily Temperatures — LeetCode #739
# https://leetcode.com/problems/daily-temperatures/
# Time: O(n) · Space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
