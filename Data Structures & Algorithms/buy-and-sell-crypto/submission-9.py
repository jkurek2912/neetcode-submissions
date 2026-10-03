class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
            while r < len(prices) and prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
        return maxProfit