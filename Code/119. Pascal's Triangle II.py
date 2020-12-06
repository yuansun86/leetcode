class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1) # final result will be 1 at each side
        for i in range(rowIndex):
            for j in range(i, 0, -1):
            	# in place calculation substition, starting from behind
                result[j] = result[j] + result[j - 1]
        return result