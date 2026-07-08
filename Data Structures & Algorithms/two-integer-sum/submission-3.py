class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i, num in enumerate(nums):
            if num in temp:
                return [temp[num],i]
            else:
                temp[target-num] = i
                