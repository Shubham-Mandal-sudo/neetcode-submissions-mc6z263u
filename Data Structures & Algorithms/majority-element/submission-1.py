class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = Counter(nums)
        return max(temp, key=temp.get)