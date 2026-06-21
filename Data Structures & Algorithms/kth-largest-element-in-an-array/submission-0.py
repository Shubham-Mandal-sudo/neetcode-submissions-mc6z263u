class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k-1):
            temp = max(nums)
            nums.remove(temp)
        return max(nums)