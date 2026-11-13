class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        temp = dict(sorted(c.items(), key=lambda item: item[1], reverse = True))
        return list(temp.keys())[:k]