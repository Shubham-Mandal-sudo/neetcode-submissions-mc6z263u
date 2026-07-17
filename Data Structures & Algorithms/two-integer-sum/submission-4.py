class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i in range(len(nums)):
            if nums[i] in temp.keys():
                return [temp[nums[i]],i]
            else:
                temp[target-nums[i]] = i
        