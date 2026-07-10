class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            target = -(nums[i])
            low = i + 1
            high = len(nums)-1
            while(high > low):
                if(high == i):
                    high -= 1
                elif(low == i):
                    low += 1
                elif(nums[high]+nums[low] == target):
                    res.add(tuple(sorted([nums[i],nums[low],nums[high]])))
                    high -= 1
                    low += 1
                elif(nums[high]+nums[low] > target):
                    high -= 1
                else:
                    low += 1
        result = list()
        for i in res:
            result.append(list(i))
        return result