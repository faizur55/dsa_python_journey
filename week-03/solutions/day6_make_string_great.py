# Make The String Great — LeetCode #1544
# https://leetcode.com/problems/make-the-string-great/
# Time: O(n) · Space: O(n)

class Solution:
    def makeGood(self, s):
        stack = []
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
