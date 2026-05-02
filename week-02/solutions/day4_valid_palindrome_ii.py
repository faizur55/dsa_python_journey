# Valid Palindrome II — LeetCode #680
# https://leetcode.com/problems/valid-palindrome-ii/
# Time: O(n) · Space: O(1)

class Solution:
    def validPalindrome(self, s):
        def is_palindrome(L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True

        L, R = 0, len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return (is_palindrome(L+1, R) or
                        is_palindrome(L, R-1))
            L += 1
            R -= 1
        return True
