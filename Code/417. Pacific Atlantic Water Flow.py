class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        pac = self.pacificWater(matrix)
        atl = self.atlanticWater(matrix)
        m = len(matrix)
        n = len(matrix[0])
        res = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] == 1 and atl[i][j] == 1:
                    res.append([i, j])
        return res
        
        
    def pacificWater(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        pacific = [[0] * n for _ in range(m)]
        for i in range(m):
            pacific[i][0] = 1
        for j in range(n):
            pacific[0][j] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific[i][j] = 1
                elif pacific[i - 1][j] == 1 and matrix[i][j] >= matrix[i - 1][j]:
                    pacific[i][j] = 1
                elif pacific[i][j - 1] == 1 and matrix[i][j] >= matrix[i][j - 1]:
                    pacific[i][j] = 1
        return pacific
    
    def atlanticWater(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        atl = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 or j == n - 1:
                    atl[i][j] = 1
                elif atl[i + 1][j] == 1 and matrix[i][j] >= matrix[i + 1][j]:
                    atl[i][j] = 1
                elif atl[i][j + 1] == 1 and matrix[i][j] >= matrix[i][j + 1]:
                    atl[i][j] = 1
        return atl