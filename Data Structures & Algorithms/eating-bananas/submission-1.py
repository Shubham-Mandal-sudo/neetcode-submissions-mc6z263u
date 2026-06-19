class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        while(high != low):
            mid = (high+low)//2
            count = 0
            for i in piles:
                count += math.ceil(i/mid)
            if count > h:
                low = mid + 1
            else:
               high = mid  
        return high