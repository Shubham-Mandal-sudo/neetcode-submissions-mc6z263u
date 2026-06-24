class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        negetive = False
        if(x < 0):
            x = -x
            negetive = True
        
        while(x):
            temp = x%10
            x = x//10
            res = res*10 + temp
        if(negetive):
            res = -res
        if((-2**31) <= res <= (2**31 - 1)):
            return res
        else:
            return 0