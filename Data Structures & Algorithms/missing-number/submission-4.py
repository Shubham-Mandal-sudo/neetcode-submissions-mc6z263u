class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return i+1