class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        powers = set()
        for i in range(32):
            powers.add(2 ** i)
        return n in powers