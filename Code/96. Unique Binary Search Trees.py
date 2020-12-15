class Solution:
    def numTrees(self, n: int) -> int:
        table = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            temp = 0
            for j in range(i):
                temp += table[j] * table[i - j - 1]
            table[i] = temp
        return table[-1]