class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -1001
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            temp = nums[i]
            res = max(temp, res)
            for j in range(i+1,len(nums)):
                temp = nums[j] + temp
                res = max(temp, res)
        return res