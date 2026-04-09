class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        z = 0
        for i in nums:
            if(i == 0):
                z = z+1
            else:
                p = p*i
        res = []
        if z == 0:
            for i in nums:
                res.append(p//i)
        else:
            for i in nums:
                if i == 0 and z == 1:
                    res.append(p)
                else:
                    res.append(0)

        return res 