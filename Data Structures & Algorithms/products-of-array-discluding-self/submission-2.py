class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zcount = 0
        product = 1
        for i in nums:
            if i == 0:
                zcount += 1
            else:
                product *= i
        res = list()
        if zcount > 1:
            return [0,]*len(nums)
        flag = bool(zcount)
        for i in nums:
            if flag:
                if i == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(product//i)
        return res