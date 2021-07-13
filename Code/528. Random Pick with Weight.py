class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        for weight in w:
            if not self.prefix:
                self.prefix.append(weight)
            else:
                self.prefix.append(self.prefix[-1] + weight)

    def pickIndex(self) -> int:
        self.total = self.prefix[-1]
        choice = random.randrange(1, self.total + 1)
        left = 0
        right = len(self.prefix) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.prefix[mid] >= choice:
                right = mid
            else:
                left = mid
        if self.prefix[left] >= choice:
            return left
        else:
            return right
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()