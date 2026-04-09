class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = Counter(nums)
        for i in list(temp.values()):
            if i != 1:
                return True
        return False