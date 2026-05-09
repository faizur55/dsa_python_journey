# Asteroid Collision — LeetCode #735
# https://leetcode.com/problems/asteroid-collision/
# Time: O(n) · Space: O(n)

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for num in asteroids:
            if num > 0:
                stack.append(num)
            else:
                while stack and stack[-1] > 0 and stack[-1] < -num:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(num)
                elif stack[-1] == -num:
                    stack.pop()
        return stack
