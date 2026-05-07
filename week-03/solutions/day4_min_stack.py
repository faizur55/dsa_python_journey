# Min Stack — LeetCode #155
# https://leetcode.com/problems/min-stack/
# All operations: O(1) · Space: O(n)

class MinStack:
    def __init__(self):
        self.main = []
        self.mins = []

    def push(self, val):
        self.main.append(val)
        if self.mins:
            self.mins.append(min(val, self.mins[-1]))
        else:
            self.mins.append(val)

    def pop(self):
        self.main.pop()
        self.mins.pop()

    def top(self):
        return self.main[-1]

    def getMin(self):
        return self.mins[-1]
