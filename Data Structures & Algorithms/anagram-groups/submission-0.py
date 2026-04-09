class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = []
        flag = []
        for i in range(len(strs)):
            count.append(Counter(strs[i]))
            flag.append(True)
        result = []
        for i in range(len(strs)):
            if flag[i]:
                temp = [strs[i],]
                flag[i] = False
                for j in range(i+1,len(strs)):
                    if count[i] == count[j]:
                        temp.append(strs[j])
                        flag[j] = False
                result.append(temp)
        return result