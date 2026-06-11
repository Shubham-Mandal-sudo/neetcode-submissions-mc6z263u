class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i in range(len(nums)):
            req = target - nums[i]
            if req in temp:
                return list([temp[req],i])
            temp[nums[i]] = i
        