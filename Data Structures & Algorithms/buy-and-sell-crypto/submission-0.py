class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        h = 0
        profit = h-l
        while(h < len(prices)):
            if (prices[h] > prices[l]):
                profit = max(profit, (prices[h]-prices[l]))
            else:
                l = h
            h = h+1
        return profit
        