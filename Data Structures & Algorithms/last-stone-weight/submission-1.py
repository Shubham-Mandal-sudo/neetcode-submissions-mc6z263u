class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            stones.sort()
            a = stones.pop()
            b = stones.pop()
            c = abs(a-b)
            if(c):
                stones.append(c)
        if(stones):
            return stones[0]
        else:
            return 0
        