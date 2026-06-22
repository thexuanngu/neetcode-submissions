class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_max = prices[0]
        for i in range(1, len(prices)):
            min_max = min(prices[i-1], min_max)
            profit = max(profit, prices[i] - min_max)
        return profit