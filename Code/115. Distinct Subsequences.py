class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # O(m ** 2 * n)
        # dp[i][j] means the number distinct subsequence of s[0~i] which equals t[0~j] and s[i] == t[j]
        if s == t:
            return 1
        if len(s) == len(t):
            return 0
        m = len(s)
        n = len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] != t[j - 1]:
                    dp[i][j] = 0
                else:
                    temp = 0
                    for k in range(i):
                        temp += dp[k][j - 1]
                    dp[i][j] = temp
        res = 0
        for i in range(m + 1):
            res += dp[i][n]
        return res