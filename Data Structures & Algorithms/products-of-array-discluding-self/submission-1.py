class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        pos = []
        for i in range(len(nums)):
            if nums[i] == 0:
                pos.append(i)
            else:
                p *= nums[i]
        if len(pos) > 1:
            return [0]*len(nums)
        elif len(pos) == 1:
            res = [0]*len(nums)
            res[pos[0]] = p
            return res
        else:
            res = []
            for i in nums:
                res.append(p//i)
            return res

