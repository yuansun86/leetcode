class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        numbers = list(set(nums))
        numbers.sort()
        count = collections.Counter(nums)
        points = {}
        for number in count:
            points[number] = number * count[number]
        res = 0
        dp = [0] * (len(numbers) + 1)
        for i in range(len(numbers)):
            number = numbers[i]
            if i == 0:
                dp[i + 1] = points[number]
            else:
                prev_number = numbers[i - 1]
                if prev_number == number - 1:
                    dp[i + 1] = max(dp[i - 1], dp[i - 2]) + points[number]
                else:
                    dp[i + 1] = max(dp[i], dp[i - 1]) + points[number]
        return max(dp)
                