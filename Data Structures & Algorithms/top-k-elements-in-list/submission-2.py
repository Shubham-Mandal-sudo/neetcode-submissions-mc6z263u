class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = Counter(nums)
        stemp = dict(sorted(temp.items(), key = lambda i: i[1], reverse = True))
        return list(stemp.keys())[:k]
