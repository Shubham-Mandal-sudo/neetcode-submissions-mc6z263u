class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -9999
        subset = 0
        low = 0
        high = 0
        while(high < len(nums)):
            subset += nums[high]
            res = max(subset, res)
            high += 1
            if (subset < 0):
                low = high 
                subset = 0
        return res