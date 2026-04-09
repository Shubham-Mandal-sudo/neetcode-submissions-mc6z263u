class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temps = Counter(s)
        tempt = Counter(t)
        if(temps == tempt):
            return True
        else:
            return False
        