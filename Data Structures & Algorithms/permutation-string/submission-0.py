class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        low = 0
        high = len(s1)-1
        cmp = Counter(s1)
        while(high<len(s2)):
            temp = s2[low:high+1]
            if(Counter(temp) == cmp):
                return True
            low = low + 1
            high = high + 1
        return False
        