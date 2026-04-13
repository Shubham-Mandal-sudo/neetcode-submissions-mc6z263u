class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        l = len(nums)
        high = len(nums)-1

        if nums[low]<nums[high]: return nums[low]
        while(high > low):
            mid = (high + low)//2
            if nums[(mid-1+l)%l]> nums[mid]: return nums[mid]
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
            prev = mid
        return nums[low]
                