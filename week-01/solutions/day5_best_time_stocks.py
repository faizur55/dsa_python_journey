# Best Time to Buy and Sell Stock — LeetCode #121
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time: O(n) · Space: O(1)

class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            profit_today = price - min_price
            if profit_today > max_profit:
                max_profit = profit_today
            if price < min_price:
                min_price = price
        return max_profit
