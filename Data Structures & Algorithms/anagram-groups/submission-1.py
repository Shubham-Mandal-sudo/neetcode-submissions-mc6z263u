class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        loc = list()
        count = 0
        res = list()
        for i in strs:
            temp = dict(Counter(i))
            y = 9999
            for index, j in enumerate(loc):
                if temp == j:
                    y = index
            if y != 9999:
                res[y].append(i)
            else:
                res.append([i,])
                loc.append(temp)
                count += 1
        return res