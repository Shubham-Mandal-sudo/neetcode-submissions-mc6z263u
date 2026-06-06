class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(int(n)):
            count += 0^int(n%2)
            n /= 2
        return count