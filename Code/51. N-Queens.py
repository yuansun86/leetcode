class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        self.backtracking(n, [], results)
        res = []
        for pattern in results:
            temp = []
            for i in range(n):
                row = []
                for j in range(n):
                    if j == pattern[i]:
                        row.append('Q')
                    else:
                        row.append('.')
                temp.append(''.join(row))
            res.append(temp)
        return res
            
        
    
    def backtracking(self, n, path, results):
        if len(path) == n:
            results.append(path[:])
            return
        i = len(path)
        for j in range(n):
            if self.isValid(i, j, path):
                path.append(j)
                self.backtracking(n, path, results)
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
        