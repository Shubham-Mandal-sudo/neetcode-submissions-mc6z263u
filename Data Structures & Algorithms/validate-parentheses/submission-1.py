class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        data = {'(':')','{':'}','[':']'}
        for i in s:
            if i in list(data.keys()):
                stack.append(i)
            else:
                if stack and i == data[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
        if stack:
            return False
        else:
            return True
        