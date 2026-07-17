class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minnow = prices[0]
        res = 0
        for i in range(1,len(prices)):
            if prices[i] <= minnow:
                minnow = prices[i]
            else:
                res = max(res, (prices[i]-minnow))
        return res