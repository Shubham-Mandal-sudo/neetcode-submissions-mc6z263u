class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = list()
        for i in s:
            if i.isalnum():
                temp.append(i.lower())
        if temp == temp[::-1]:
            return True
        else:
            return False
        