class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0,]*len(temperatures)
        stk = list()
        for i in range(len(temperatures)):
            while(stk and stk[-1][0] < temperatures[i]):
                res[stk[-1][1]] = i - stk[-1][1]
                stk.pop()
            stk.append([temperatures[i],i])
        return res
