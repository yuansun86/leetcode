class Solution:
    def __init__(self):
        self.count = 0
        
    def totalNQueens(self, n: int) -> int:
        self.backtracking(n, [])
        return self.count
            
        
    
    def backtracking(self, n, path):
        if len(path) == n:
            self.count += 1
            return
        i = len(path)
        for j in range(n):
            if self.isValid(i, j, path):
                path.append(j)
                self.backtracking(n, path)
                path.pop()
        
    
    def isValid(self, i, j, path):
        if not path:
            return True
        for x, y in enumerate(path):
            if j == y:
                return False
            if abs(i-x) == abs(j-y):
                return False
        return True