class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = Counter(nums)
        sl = sorted(data, key=data.get, reverse=True) 
        return sl[:k]