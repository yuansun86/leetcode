class Solution:

    def __init__(self, nums: List[int]):
        self.numbers = collections.defaultdict(list)
        for i, number in enumerate(nums):
            self.numbers[number].append(i)

    def pick(self, target: int) -> int:
        candidates = self.numbers[target]
        return random.choice(candidates)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)