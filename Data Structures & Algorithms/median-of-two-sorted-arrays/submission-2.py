class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numsf = list()
        p1 = p2 = 0
        m = len(nums1) 
        n = len(nums2)
        temp = (m+n - 1)//2
        while(p1 < m and p2 < n and p1+p2 <= temp+1):
            if (nums1[p1] < nums2[p2]):
                numsf.append(nums1[p1])
                p1 += 1
            else:
                numsf.append(nums2[p2])
                p2 += 1
        while(p1 < m and p1+p2 <= temp+1):
            numsf.append(nums1[p1])
            p1 += 1
        while(p2 < n and p1+p2 <= temp+1):
            numsf.append(nums2[p2])
            p2 += 1
        if ((m+n) % 2 == 0):
            return (numsf[temp] + numsf[temp+1])/2
        else:
            return numsf[temp]
