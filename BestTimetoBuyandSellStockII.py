# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# since we are allowed to buy and sell unlimited number of stocks
# every time there is an upward trend , we buy and sell

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        for i in range(len(prices)-1):
            m+= prices[i+1]-prices[i] if (prices[i+1]>prices[i]) else 0
        return m