# Valid Parentheses — LeetCode #20
# https://leetcode.com/problems/valid-parentheses/
# Time: O(n) · Space: O(n)

class Solution:
    def isValid(self, s):
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char in mapping:
                if not stack:
                    return False
                if stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
