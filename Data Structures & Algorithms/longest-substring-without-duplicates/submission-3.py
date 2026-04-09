class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        res = 0
        lookup = dict()
        low = 0
        for i in range(len(s)):
            if s[i] in list(lookup.keys()):
                if lookup[s[i]] >= low:
                    res = max(res,count)
                    low = lookup[s[i]]+1
                    count = i-low
            count = count + 1
            lookup[s[i]] = i
        res = max(res,count)
        return res