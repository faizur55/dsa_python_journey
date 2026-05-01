# Jewels and Stones — LeetCode #771
# https://leetcode.com/problems/jewels-and-stones/
# Time: O(j+n) · Space: O(j)

class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)
        return sum(1 for s in stones if s in jewel_set)
